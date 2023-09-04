import re

from nonebot.plugin import PluginMetadata
from nonebot import on_command, on_regex, on_message
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.matcher import Matcher
from nonebot.params import Depends
from nonebot.plugin import PluginMetadata
from nonebot.typing import T_Handler
from nonebot import logger

from nonebot import require
require("nonebot_plugin_imageutils")

from io import BytesIO
from typing import List, Union
from .commands import cmds, dialogs, to_me_dig
from .entities import Command, Dialog, UserState, UserInfo
from .depends import IsArn, Self
from .utils import weighted_random_choice
#日常调度器
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
import sqlite3



__plugin_meta__ = PluginMetadata(
    name="猫猫",
    description="猫猫bot",
    usage="Arn的猫猫",
    extra={
        "unique_name": "maomaobot",
        "example": "/打工",
        "author": "doro",
        "version": "0.0.1",
    },
)


conn = sqlite3.connect('data/user_states.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS USER_STATE (
        id INTEGER PRIMARY KEY,
        user_data TEXT
    )
''')
conn.commit()
conn.close()

def update_signed_status():
    logger.info("每日签到更新开始>>>>>")
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, user_data FROM USER_STATE")
    rows = cursor.fetchall()
    user_states = []
    ids = []
    for row in rows:
        id, user_state = row[0], UserState(**row[1])
        user_state.signed = False
        user_states.append(user_state)
        ids.append(id)
    conn.close()
    [UserInfo(id=ids[i]).save_states(user_states[i]) for i in range(len(ids))]
    logger.info("每日签到更新完成>>>>>")


scheduler.add_job(update_signed_status, "interval", days=1, id="update_signed_status")

def handler_v11(command: Command) -> T_Handler:
    async def handle(
        #bot: Bot,
        #event: MessageEvent,
        matcher: Matcher,
        res: Union[str, BytesIO, List[BytesIO]] = Depends(command.func),
    ):
        if isinstance(res, str):
            await matcher.finish(res)
        else: #isinstance(res, BytesIO):
            await matcher.finish(MessageSegment.image(res))
    return handle

def reply_handler(dialog: Dialog) -> T_Handler:
    async def handle(
        matcher: Matcher,
        is_arn: bool = IsArn(),
        sender: UserInfo = Self()
    ):
        if dialog.reply_to_arn and is_arn:
            await matcher.finish(weighted_random_choice(dialog.reply_to_arn_content, [1 / len(dialog.reply_to_arn_content) for _ in dialog.reply_to_arn_content]))
        user_state = sender.load_states()
        for i, upper_bound in enumerate(dialog.feeling_threshold):
            if user_state.affection < upper_bound:
                await matcher.finish(weighted_random_choice(dialog.reply[i], [1 / len(dialog.reply[i]) for _ in dialog.reply[i]]))
        await matcher.finish(weighted_random_choice(dialog.reply[-1], [1 / len(dialog.reply[-1]) for _ in dialog.reply[-1]]))
    return handle


def create_matchers():
    for command in cmds:
        matcher = on_command(
            command.keywords[0], aliases=set(command.keywords), block=True, priority=10, permission=command.permission
        )
        matcher.append_handler(handler_v11(command))

    for dialog in dialogs:
        matcher = on_regex(pattern=dialog.pattern, flags=re.M, permission=dialog.permission, priority=12, block=True)
        matcher.append_handler(reply_handler(dialog))
create_matchers()

call_me_matcher = on_message(rule=to_me(), priority=12, block=True)
call_me_matcher.append_handler(reply_handler(to_me_dig))