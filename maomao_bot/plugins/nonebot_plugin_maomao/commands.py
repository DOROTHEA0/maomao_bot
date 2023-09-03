from .functions import *
from .entities import Command

cmds = [
    Command(("签到", "每日签到",), sign_in),
    Command(("小卖铺", "小卖部", "商城", "商店",), list_shop),
    Command(("背包",), list_bag),
    Command(("购买", "购买商品"), buy_item),
    # Command(("送礼",), None),
    Command(("打工",), start_arbeit),
    Command(("结束打工", "下班",), finish_arbeit),
    Command(("增加纽扣", "增加小纽扣", "添加纽扣", "添加小纽扣"), add_buttons, superuser_permission=True)
]