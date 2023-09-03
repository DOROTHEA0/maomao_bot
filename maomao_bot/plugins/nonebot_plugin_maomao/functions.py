import time
from typing import List
from nonebot_plugin_imageutils import BuildImage, Text2Image

from .data_source import arbeits, items
from .depends import Self, MentionedUsers, MentionedUser, Args, Arg, NoArg
from .entities import UserState, UserInfo, Arbeit
from .utils import weighted_random_choice


arbeit_time = 3600

def sign_in(sender: UserInfo=Self()):
    user_state: UserState = sender.load_states()
    if user_state.signed:
        return "你好像来了不止一次？失忆了吗？（歪头）"
    user_state.signed = True
    rand_button = weighted_random_choice([7, 8, 9, 10], [0.25, 0.25, 0.25, 0.25])
    rand_affection = weighted_random_choice([1, 2], [0.5, 0.5])
    user_state.buttons += rand_button
    user_state.affection += rand_affection
    sender.save_states(user_state)
    return f"记下啦！今天也是美好的一天☆（增加{rand_affection}点好感，增加{rand_button}枚小纽扣)"


def list_shop():
    shop_item = [item for item in items.values() if item.on_sell]
    list_msg = "欢迎来到417寝室小卖铺，这里有：\n"
    for item in shop_item:
        list_msg += item.get_shop_des()
    return list_msg

def list_bag(sender: UserInfo=Self()):
    send_msg = "背包\n"
    user_state: UserState = sender.load_states()
    send_msg += f"你拥有：{user_state.buttons}枚小纽扣\n"
    send_msg += "礼物有：\n"
    if len(user_state.bag) == 0:
        send_msg += "空的呢~\n"
    else:
        for item_name, count in user_state.bag.items():
            send_msg += f"{item_name}{count}个\n"
    return send_msg


def buy_item(sender: UserInfo=Self(), arg: str=Arg()):
    if arg not in items or not items[arg].on_sell:
        return "似乎没有这个商品呢……"
    selected_item = items[arg]
    user_state: UserState = sender.load_states()
    if user_state.buttons - selected_item.price < 0:
        return "似乎小纽扣有些不太够呢……"
    user_state.buttons -= selected_item.price
    if selected_item.name not in user_state.bag:
        user_state.bag[selected_item.name] = 1
    else:
        user_state.bag[selected_item.name] += 1
    sender.save_states(user_state)
    return "感谢购买——欢迎下次再来☆"

def start_arbeit(sender: UserInfo=Self()):
    user_state: UserState = sender.load_states()
    if user_state.arbeit_name:
        return "下班的话记得【#结束打工】喵~"
    arbs = list(arbeits.values())
    probs = [arb.occurrence_prob for arb in arbs]
    random_arbeit: Arbeit = weighted_random_choice(arbs, probs)
    user_state.arbeit_name = random_arbeit.name
    user_state.arbeit_start_time = int(time.time())
    sender.save_states(user_state)
    return random_arbeit.get_info()



def finish_arbeit(sender: UserInfo=Self()):
    user_state: UserState = sender.load_states()
    if not user_state.arbeit_name:
        return "结束？你还没开始呢（盯——)\n要打工的话，记得输入【打工】喵~"
    arbeit: Arbeit = arbeits[user_state.arbeit_name]
    if int(time.time()) - user_state.arbeit_start_time < arbeit_time:
        return arbeit.insufficient_des
    normal_result = weighted_random_choice([True, False], [arbeit.normal_prob, 1 - arbeit.normal_prob])
    if normal_result:
        send_msg = arbeit.normal_ending_des
        user_state.buttons += arbeit.normal_reward
    else:
        send_msg = arbeit.abnormal_ending_des
        user_state.buttons += arbeit.abnormal_reward
    user_state.arbeit_name = ""
    sender.save_states(user_state)
    return send_msg


# 管理权限
def add_buttons(sender: UserInfo=Self(), arg: str=Arg(), m_user: UserInfo=MentionedUser()):
    try:
        button_count = int(arg)
    except ValueError as e:
        return "要输入添加数字呢"
    if m_user is not None:
        user_state: UserState = m_user.load_states()
        user_state.buttons += button_count
        m_user.save_states(user_state)
        return f"添加指定用户{m_user.id}成功！"
    else:
        user_state: UserState = sender.load_states()
        user_state.buttons += button_count
        sender.save_states(user_state)
        return "添加成功！"
