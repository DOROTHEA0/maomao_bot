import time
from typing import List, Union
from nonebot_plugin_imageutils import BuildImage, Text2Image

from .data_source import arbeits, items, arbeit_time, basic_item_list
from .depends import Self, MentionedUsers, MentionedUser, Args, Arg, NoArg, Cmd
from .entities import UserState, UserInfo, Arbeit, Item, BasicItem
from .utils import weighted_random_choice, ranged_choose




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

def give_present(sender: UserInfo=Self(), arg: str=Arg()):
    user_state: UserState = sender.load_states()
    if not arg or arg not in user_state.bag:
        return ""
    item = items[arg]
    user_state.bag[arg] -= 1
    if user_state.bag[arg] <= 0:
        del user_state.bag[arg]
    user_state.affection += item.affection
    reply_list = ranged_choose(item.gift_reply_threshold, user_state.affection, item.gift_reply)
    sender.save_states(user_state)
    return weighted_random_choice(reply_list, [1 / len(reply_list) for _ in reply_list])


def start_arbeit(sender: UserInfo=Self()):
    user_state: UserState = sender.load_states()
    if user_state.arbeit_name:
        return "下班的话记得【结束打工】喵~"
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

def gacha(sender: UserInfo=Self(), command: str=Cmd()):
    def process_single_item(state: UserState, item: Union[Item, BasicItem]):
        if isinstance(item, Item):
            if item.name not in state.bag:
                state.bag[item.name] = 1
            else:
                state.bag[item.name] += 1
            return item.name + "x1\n" + item.gacha_des + "\n"
        else:
            if item.type == "btn":
                state.buttons += item.button_reward
            elif item.type == "mute":
                pass #禁言处理
            return item.get_gacha_des() + "\n"

    # 组卡池
    gacha_list = list(basic_item_list.keys()) + [name for name, item in items.items() if item.in_gacha]
    gacha_probs = [item.prob for item in basic_item_list.values()] + [item.prob_pair for item in items.values() if item.in_gacha]
    user_state = sender.load_states()
    if command in ["抽卡", "单抽"]:
        if user_state.buttons - 5 < 0:
            return "要花费五枚小纽扣才可以进行抽奖哦～【小纽扣不足】"
        user_state.buttons -= 5
        gacha_res = weighted_random_choice(gacha_list, gacha_probs)
        gacha_res = items[gacha_res] if gacha_res in items else basic_item_list[gacha_res]
        send_msg = process_single_item(user_state, gacha_res)
        sender.save_states(user_state)
        return send_msg
    else:
        if user_state.buttons - 50 < 0:
            return "要花费五十枚小纽扣才可以进行十连抽哦～【小纽扣不足】"
        user_state.buttons -= 50
        gacha_res = weighted_random_choice(gacha_list, gacha_probs, times=10)
    send_msg = "十连吗？我看看……\n"
    for i, item_name in enumerate(gacha_res):
        send_msg += str(i + 1) + "：\n"
        item = items[item_name] if item_name in items else basic_item_list[item_name]
        send_msg += process_single_item(user_state, item)
    sender.save_states(user_state)
    return send_msg


# 管理权限
def add_buttons(arg: str=Arg(), m_user: UserInfo=MentionedUser()):
    try:
        button_count = int(arg)
    except ValueError as e:
        return "要输入添加数字呢"
    user_state: UserState = m_user.load_states()
    user_state.buttons += button_count
    m_user.save_states(user_state)
    return f"添加指定用户{m_user.id}成功！"
