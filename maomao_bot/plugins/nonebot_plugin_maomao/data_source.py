from .entities import Command, Arbeit
from .functions import *


commands = [
    Command(("签到", "每日签到",), sign_in),
    Command(("小卖部", "商城", "商店",), list_shop),
    #Command(("送礼",), None),
    Command(("打工", ), start_arbeit),
    Command(("结束打工", "下班",), finish_arbeit),
    #Command(("查询saki状态",), None)
]

arbeits = [
    Arbeit("咖啡馆",                                                                                  # 地点
           "这里是一家平平无奇的古典咖啡店，店长K是一位温和的先生，偶尔在这儿兼职挣点外快或许再合适不过……",           # 工作描述
           "还没到下班时间呢，再耐心等等吧！",                                                             # 早退描述
           "yeah——下班啦！回家回家！【获得10个小纽扣】",                                                   # 正常下班事件描述
           "你工作时因疏忽大意不小心将咖啡打翻，泼到了客人身上，因此本次打工的工资全部用来赔款了……（对手指）",        # 不正常下班事件描述
           0.5, 0.6, range(10, 15), 0),                                                             # 出现概率，正常下班事件概率，正常事件奖励(范围)，不正常事件奖励
    Arbeit("教会",
           "你来到了一间教堂，或许这儿只有一些志愿者工作，并不能挣到什么，但或许可以通过祷告提升一下别的什么……",
           "嘘——似乎还没有结束，再等等吧……♭",
           "结束了——我们走吧✟【获得2枚小纽扣】",
           "在教会期间，你撞上了正在悄摸觅食的主教X，并用一碗蒸蛋征服了ta（？）【意外获得了来自教会执事M的15枚小纽扣】",
           0.3, 0.7, 2, 15),
    Arbeit("收容所",
           "你来到了一处非人收容所，在此处兼职或许可以大赚一笔，但存在一定量的生命危险，这对你来说真的有必要性吗？",
           "我理解你想下班的心情，但是时间还没到5555……",
           "！终于结束了！！快跑啊啊啊啊！！！",
           "因为你的管理疏忽，导致了收容的非人存在出逃，造成了巨大的损失，你在逃跑过程中丢失了20枚小纽扣……",
           0.1, 0.2, 50, -20),
    Arbeit("？？？",
           "你来到了A某人的家，ta需要外出工作一段时间，于是将家里的蜘蛛委托给你照顾，意想不到的兼职……",
           "A某人还没有回来，而且小蜘蛛盯得死死的，想提前偷跑应该不太可能……",
           "A某人回来啦！下班——记得和小蜘蛛说声再见♪【获得20枚小纽扣】",
           "因为你的行为不当，使小蜘蛛受到惊吓，跑掉了……直至A某人回来你也没能找回ta，自然是没有工资了（叹气）",
           0.1, 0.4, 20, 0),
]

