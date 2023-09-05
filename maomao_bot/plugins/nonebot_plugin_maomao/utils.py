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


def weighted_random_choice(items, probabilities, times=1):
    items_pair = list(zip(items, probabilities))
    res = []
    for _ in range(times):
        rand = random.random()
        for item, probability in items_pair:
            rand -= probability
            if rand <= 0:
                res.append(item)
                break
    return res[0] if times == 1 else res

def ranged_choose(bounds, num, input_list):
    assert len(bounds) == len(input_list) - 1
    selected_item = input_list[-1]
    for i, upper_bound in enumerate(bounds):
        if num < upper_bound:
            selected_item = input_list[i]
            break
    return selected_item