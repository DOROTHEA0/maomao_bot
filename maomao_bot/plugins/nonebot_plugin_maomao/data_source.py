from .entities import Arbeit, Item

arbeit_time = 3600

arbeits = {
    "咖啡馆": Arbeit(name="咖啡馆", institution="咖啡馆",  # 地点
                     description="这里是一家平平无奇的古典咖啡店，店长K是一位温和的先生，偶尔在这儿兼职挣点外快或许再合适不过……", # 工作描述
                     insufficient_des="还没到下班时间呢，再耐心等等吧！",  # 早退描述
                     normal_ending_des="yeah——下班啦！回家回家！【获得10个小纽扣】",  # 正常下班事件描述
                     abnormal_ending_des="你工作时因疏忽大意不小心将咖啡打翻，泼到了客人身上，因此本次打工的工资全部用来赔款了……（对手指）", # 不正常下班事件描述
                     occurrence_prob=0.5, normal_prob=0.6, normal_reward=10, abnormal_reward=0),  # 出现概率，正常下班事件概率，正常事件奖励(范围)，不正常事件奖励
    "教会": Arbeit(name="教会", institution="教会",
                   description="你来到了一间教堂，或许这儿只有一些志愿者工作，并不能挣到什么，但或许可以通过祷告提升一下别的什么……",
                   insufficient_des="嘘——似乎还没有结束，再等等吧……♭",
                   normal_ending_des="结束了——我们走吧✟【获得2枚小纽扣】",
                   abnormal_ending_des="在教会期间，你撞上了正在悄摸觅食的主教X，并用一碗蒸蛋征服了ta（？）【意外获得了来自教会执事M的15枚小纽扣】",
                   occurrence_prob=0.3, normal_prob=0.7, normal_reward=2, abnormal_reward=15),
    "收容所": Arbeit(name="收容所", institution="收容所",
                     description="你来到了一处非人收容所，在此处兼职或许可以大赚一笔，但存在一定量的生命危险，这对你来说真的有必要性吗？",
                     insufficient_des="我理解你想下班的心情，但是时间还没到5555……",
                     normal_ending_des="！终于结束了！！快跑啊啊啊啊！！！【获得50个小纽扣】",
                     abnormal_ending_des="因为你的管理疏忽，导致了收容的非人存在出逃，造成了巨大的损失，你在逃跑过程中丢失了20枚小纽扣……",
                     occurrence_prob=0.1, normal_prob=0.2, normal_reward=50, abnormal_reward=-20),
    "A某人的家": Arbeit(name="A某人的家", institution="？？？",
                        description="你来到了A某人的家，ta需要外出工作一段时间，于是将家里的蜘蛛委托给你照顾，意想不到的兼职……",
                        insufficient_des="A某人还没有回来，而且小蜘蛛盯得死死的，想提前偷跑应该不太可能……",
                        normal_ending_des="A某人回来啦！下班——记得和小蜘蛛说声再见♪【获得20枚小纽扣】",
                        abnormal_ending_des="因为你的行为不当，使小蜘蛛受到惊吓，跑掉了……直至A某人回来你也没能找回ta，自然是没有工资了（叹气）",
                        occurrence_prob=0.1, normal_prob=0.4, normal_reward=20, abnormal_reward=0),
}

items = {
    "创可贴": Item(name="创可贴", affection=10, price=10,
                   description="印有可爱的卡通图案，似乎能有效的抚慰伤口甚至心灵。建议囤货，以备不时之需。",
                   gacha_des="我看看…抽中了实用的【创口贴】小赚不亏喵～",
                   on_sell=True, in_gacha=True, prob_pair=0.145),
    "扑克牌": Item(name="扑克牌", affection=10, price=10,
                   description="寝室内总是会有一些扑克牌凭空消失，现已纳入417寝室十大未解之谜（其实是被猫猫从寝室热血大傻那儿偷强走了……)",
                   gacha_des="喵？抽中的是…【扑克牌】？这东西是怎么混进来的？应该不亏？",
                   on_sell=True, in_gacha=True, prob_pair=0.15),
    "高阶魔方": Item(name="高阶魔方", affection=40, price=100,
                   description="被猫猫打乱后就再也无法复原了……于是寝室的男妈妈决定背着猫猫卖了它！（送给猫猫或许会有意外收获？）",
                   gacha_des="你抽中了【高阶魔方】……喵？这怎么那么像我丢的那一个？？？",
                   on_sell=True, in_gacha=True, prob_pair=0.02),
    "沙漏": Item(name="沙漏", affection=40, price=200,
                   description="上铺的蓝发占星师纯手工制作！倒转沙漏，时间也不会回来，不过可以送给猫猫，兑换A某人的一次塔罗牌占卜……",
                   gacha_des="抽中了精致的【沙漏】☆还是很赚的！！",
                   on_sell=True, in_gacha=True, prob_pair=0.02),
    "奇怪的胶卷": Item(name="奇怪的胶卷", affection=90, price=400,
                   description="下铺的红发少年友情提供，似乎能拍下一些特殊的照片，总之猫猫很喜欢…（可兑换A某人板绘的灵魂表情包一枚)",
                   gacha_des="让我看看你抽到了什么……这！这是！【奇怪的胶卷】……可以把ta送给我吗？求求了喵～♡",
                   on_sell=True, in_gacha=True, prob_pair=0.01),
    "无色草绘": Item(name="无色草绘", affection=1, price=0,
                   description="",
                   gacha_des="哇——抽中了A某人的【无色草绘】！☆虽然不会上色，但能抽中这个也算是非常不错了★",
                   on_sell=False, in_gacha=True, prob_pair=0.004),
    "上色草绘": Item(name="上色草绘", affection=1, price=0,
                   description="",
                   gacha_des="什？！竟然抽中了A某人的【上色草绘】！☆这个概率可是非常之小呢★",
                   on_sell=False, in_gacha=True, prob_pair=0.001),
    "A某人的画": Item(name="A某人的画", affection=1, price=900,
                   description="伟大的A某人发话了，ta说你们敢攒，ta就敢画，虽然大概率只是一般摸鱼头像的那种……",
                   gacha_des="",
                   on_sell=True, in_gacha=False, prob_pair=0),
}



'''
购买商品语录
例：感谢购买——欢迎下次再来☆
购买商品失败语录
例：似乎小纽扣有些不太够呢……
送礼语录（可回复一样，可根据不同商品回复不一样。每个商品加钱可升级成随机回复或者有好感度判断的随机回复）
送商品1（创可贴）
例：很实用呢，谢谢www
送商品2（扑克牌）
例：怎么绕了一圈又回到我这了？
（高阶魔方）
例：！！！我还以为再也见不到ta了……你是天使5555……
（沙漏）
例：wow——这个好看！谢谢！！！
（A某人的画）
例：是时候监工了……
'''
