import shlex
from io import BytesIO
from typing import Tuple, Literal


from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
    MessageEvent,
    MessageSegment,
    unescape,
)
from nonebot.params import CommandArg, Depends
from nonebot.typing import T_State
from nonebot.log import logger
from nonebot import require

require("nonebot_plugin_imageutils")
from nonebot_plugin_imageutils import BuildImage, Text2Image

from .entities import UserInfo
from .utils import get_user_info


def Self(only_id=True):
    async def dependency(bot: Bot, event: MessageEvent):
        try:
            group_id = str(event.group_id)
            user = UserInfo(id=event.get_user_id(), group_id=group_id)
        except AttributeError:
            user = UserInfo(id=event.get_user_id())
        if not only_id:
            await get_user_info(bot, user)
        return user
    return Depends(dependency)

def MentionedUsers(only_id=True):
    async def dependency(bot: Bot, event: GroupMessageEvent, state: T_State):
        m_users_id = [seg.data["qq"] for seg in state["_prefix"]["command_arg"] if seg.type == 'at']
        users = [UserInfo(id=i, group_id=str(event.group_id)) for i in m_users_id]
        if not only_id:
            for user in users:
                await get_user_info(bot, user)
        return users
    return Depends(dependency)

def MentionedUser():
    pass


def Arg():
    def dependency(msg: Message = CommandArg()):
        return unescape(msg.extract_plain_text().strip())
    return Depends(dependency)


def Args():
    def dependency(arg: Tuple = Arg()):
        event, arg = arg
        try:
            args = shlex.split(arg[1])
        except:
            args = arg[1].split()
        args = [a for a in args if a]
        return event, args

    return Depends(dependency)


def NoArg():
    def dependency():
        return
    return Depends(dependency)
