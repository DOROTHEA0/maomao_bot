from .functions import *
from .entities import Command

cmds = [
    Command(("签到", "每日签到",), sign_in),
    Command(("小卖部", "商城", "商店",), list_shop),
    Command(("背包",), list_bag),
    # Command(("送礼",), None),
    Command(("打工",), start_arbeit),
    Command(("结束打工", "下班",), finish_arbeit),
    # Command(("查询saki状态",), None)
]