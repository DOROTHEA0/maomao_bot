from nonebot.adapters.onebot.v11 import Bot
from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.permission import SUPERUSER
from .reload import Reloader

reboot_matcher = on_command(cmd="重启", aliases={"重启猫猫", "reboot", "restart"}, permission=SUPERUSER, priority=1, block=True)

@reboot_matcher.handle()
async def _(bot: Bot, event: MessageEvent):
    Reloader.reload()