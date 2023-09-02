from nonebot.adapters.onebot.v11 import MessageEvent
from .depends import User, Arg, Args, NoArg, Items
from .data_source import arbeits, items

def sign_in(s: dict=User()):
    return str(s)

def list_shop():
    shop_item = [item for item in items.values() if item.on_sell]
    list_msg = "欢迎来到417寝室小卖铺，这里有：\n"
    for item in shop_item:
        list_msg += item.get_shop_des()
    return list_msg

def list_bag():
    pass

def start_arbeit():
    pass

def finish_arbeit():
    pass