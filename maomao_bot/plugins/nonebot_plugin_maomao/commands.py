from .functions import *
from .entities import Command, Dialog
from .permission import ARN
from nonebot.permission import SUPERUSER

cmds = [
    Command(("签到", "每日签到",), sign_in),
    Command(("小卖铺", "小卖部", "商城", "商店",), list_shop),
    Command(("背包",), list_bag),
    Command(("购买", "购买商品"), buy_item),
    Command(("送礼", "赠送"), give_present),
    Command(("打工",), start_arbeit),
    Command(("结束打工", "下班",), finish_arbeit),
    Command(("抽卡", "单抽", "十连抽", "10连抽", "10抽"), gacha),
    Command(("增加纽扣", "增加小纽扣", "添加纽扣", "添加小纽扣"), add_buttons, permission=SUPERUSER)
]

to_me_dig = Dialog(pattern="", feeling_threshold=[], reply=[["喵？谁叫我？", "咋滴啦？叫我干嘛？", "（歪头）（盯——）", "我踏马来辣！（突然出现）"]], reply_to_arn=True, reply_to_arn_content=["Arn！！我在这！！"])

dialogs = [
    Dialog(pattern=r"\b早\b", feeling_threshold=[30, 60], reply=[["早安", ], ["哦哈哟——", ], ["哦哈——今天也要开心呀！", ]]),
    Dialog(pattern=r"(?=.*画画)^.{1,4}$", feeling_threshold=[30, 60], reply=[["不画", ], ["为什么要画画", ], ["画牺牲了……", ]]),
    Dialog(pattern=r"^(呜{2,})$", feeling_threshold=[30, 60], reply=[["怎么了吗？（拍拍）", ], ["没事吧？（揉揉）", ], ["不要哭啊……（抱）", ]]),
    Dialog(pattern=r"^(哈{2,})$", feeling_threshold=[30, 60], reply=[["发生什么有趣的事吗？", ], ["怎么了怎么了？有什么好玩的没带我吗？", ], ["哈哈哈哈（不知道发生了什么但是选择跟着笑x）", ]]),
    Dialog(pattern=r"^[？?]+$", feeling_threshold=[30, 60], reply=[["？", ], ["？？", ], ["喵？", ]]),
    Dialog(pattern=r"^(醒了)$|^(我醒了)$", feeling_threshold=[30, 60], reply=[["你醒了？世界已经毁灭了", ], ["你醒了？其实这才是梦……", ], ["不，你没醒（摁下去）", ]]),
    Dialog(pattern=r"^(贴贴)$|^(贴贴猫猫)$|^(贴贴zoe)$", feeling_threshold=[30, 60], reply=[["别乱碰我……", "dame！！不贴！！", "请放尊重一点", "（躲开）"], ["这样有什么好处吗？", "也不是不行", "还是算了吧5555", "不是陌生人，应该可以贴吧……"], ["好耶——（抱住）", "我冲来！！！"]], reply_to_arn=True, reply_to_arn_content=["喵～贴贴艾因（蹭）"]),
    Dialog(pattern=r"^(晚安)$", feeling_threshold=[30, 60], reply=[["安", "夜安", "晚安"], ["晚安喵~", "哦呀斯密——", "快睡吧！", "安安安安"], ["是时候去偷吃了！要一起吗？", "美好的夜生活开始了……", "这就和枕头结婚！", "自愿被被子绑架xxxx"]], reply_to_arn=True, reply_to_arn_content=["你最好真的是去睡觉……"]),
    Dialog(pattern=r"^给你.{0,3}拳$", feeling_threshold=[30, 60], reply=[["你怎么敢的！（怒视.jpg）", "我要去告诉艾因5555……", "喵！！！！（炸毛）", "敢打我！我删你稿子！（乱戳图层）", "（跳开)（扑脸)（抓回去）"], ["呜！为什么要打我……（委屈）", "呜哇啊啊啊啊啊啊啊！！（超大声）", "（轻轻躺下)（开始碰瓷）"], ["我做错什么了吗？Q ~ Q（无助抱头）", "你打我…我要离家出走了……", "你不爱我了…那你死吧……（拿刀x）"]]),
    Dialog(pattern=r"annoi", feeling_threshold=[], reply=[["听到了熟悉的名字！！（警觉）", "你认识他吗？（盯——）", "My boy！！！！"]]),
    Dialog(pattern=r"催稿", feeling_threshold=[], reply=[["催稿？我也催催", "查询稿子进度x", "怎么办…艾因快去世了……", "（吃布丁看热闹）"]]),
    Dialog(pattern=r"^(骂我)$", feeling_threshold=[], reply=[["你竟然有这种爱好吗？（呆涩）", "你是不是脑子坏掉了……（震撼）", "我不认识你……（目移）（嫌弃）"]]),
    Dialog(pattern=r"^(撒娇)$", feeling_threshold=[30, 60], reply=[["我不要！你算哪枚小纽扣啊（避开）", ], ["喵？我很可爱，抱我——（拿刀威胁）", ], ["可以给我买胶卷吗？我想要喵～（星星眼）好不好 好不好 好不好嘛～～（拽衣角蹦跶）喵～（蹭）", ]]),
    Dialog(pattern=r"画稿", permission=ARN, reply_to_arn=True, reply_to_arn_content=["说好的画我呢？（低语）"])
]
