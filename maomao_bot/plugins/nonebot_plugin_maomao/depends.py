import shlex
from io import BytesIO
from typing import Tuple, Literal
from nonebot import require
require("nonebot_plugin_imageutils")
from nonebot_plugin_imageutils import BuildImage, Text2Image

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

from .entities import UserInfo
from .utils import get_user_info


def msg_preprocess():
    def dependency(event: MessageEvent, state: T_State):

        return

    return Depends(dependency)

def User():
    def dependency(bot: Bot, state: T_State):
        return state["SENDER"]
    return Depends(dependency)

def MentionedUsers():
    pass

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
    def dependency(arg: Literal[""] = Arg()):
        return
    return Depends(dependency)
