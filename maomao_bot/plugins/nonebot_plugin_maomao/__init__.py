from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.matcher import Matcher
from nonebot.params import Depends
from nonebot.plugin import PluginMetadata
from nonebot.typing import T_Handler

from io import BytesIO
from typing import List, Union

from .commands import cmds
from .entities import Command
#日常调度器
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

# import sqlite3 数据库
# conn = sqlite3.connect('bot_database.db')
# conn.close()

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

def create_matchers():
    for command in cmds:
        matcher = on_command(
            command.keywords[0], aliases=set(command.keywords), block=True, priority=12
        )
        matcher.append_handler(handler_v11(command))

create_matchers()