import time
import random
from typing import  List
from nonebot.adapters.onebot.v11 import Bot

from .entities import UserInfo

async def get_user_info(bot: Bot, user: UserInfo):
    if not user.qq:
        return

    if user.group:
        info = await bot.get_group_member_info(
            group_id=int(user.group), user_id=int(user.qq)
        )
        user.name = info.get("card", "") or info.get("nickname", "")
        user.gender = info.get("sex", "")
    else:
        info = await bot.get_stranger_info(user_id=int(user.qq))
        user.name = info.get("nickname", "")
        user.gender = info.get("sex", "")


def generate_random_probability():
    seed = int(time.time())
    random.seed(seed)
    probability = random.random()
    return probability


def random_choose(lst: List, prob: List):
    pass
