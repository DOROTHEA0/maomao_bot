import json
import sqlite3
from dataclasses import dataclass, asdict, field
from typing import Tuple, Callable, Union, Literal, List, Optional
from nonebot_plugin_imageutils import BuildImage
from nonebot.permission import Permission
from nonebot.typing import T_PermissionChecker


@dataclass
class Command:
    keywords: Tuple[str, ...]
    func: Callable
    permission: Optional[Union[Permission, T_PermissionChecker]] = None

@dataclass
class Dialog:
    pattern: str = ""
    feeling_threshold: List[int] = field(default_factory=list)
    reply: List[List[str]] = field(default_factory=list)
    permission: Optional[Union[Permission, T_PermissionChecker]] = None
    reply_to_arn: bool = False
    reply_to_arn_content: List[str] = field(default_factory=list)

@dataclass
class Arbeit:
    name: str
    institution: str
    description: str
    insufficient_des: str
    normal_ending_des: str
    abnormal_ending_des: str
    occurrence_prob: float
    normal_prob: float
    normal_reward: Union[range, int]
    abnormal_reward: Union[range, int]

    def get_info(self):
        return "【" + self.institution + "】" + "\n" + self.description


@dataclass
class Item:
    name: str = ""
    affection: int = 0
    description: str = ""
    price: int = 0
    on_sell: bool = True
    in_gacha: bool = False
    gacha_des: str = ""
    gift_reply_threshold: List[int] = field(default_factory=list)
    gift_reply: List[List[str]] = field(default_factory=list)
    prob_pair: Union[float, List[Tuple[float, int]]] = 0

    def get_shop_des(self) -> str:
        return f"{self.name} 【好感度+{self.affection}】\n售价：{self.price}枚小纽扣\n说明：{self.description}\n"

@dataclass
class BasicItem:
    name: str = ""
    type: str = "" # btn, mute, null
    button_reward: int = 0
    mute_time: Union[range, int] = 0
    prob: float = 0.

    def get_gacha_des(self):
        if self.type == "btn":
            if self.button_reward > 5:
                return f"抽中了【小纽扣×{self.button_reward}】也算是小赚一笔了"
            else:
                return f"抽中了【小纽扣×{self.button_reward}】亏了……但不多？(￣～￣)嚼！"
        elif self.type == "mute":
            return f"恭喜——！奖励你冷静一小会儿xxxx，禁言{self.mute_time}分钟。"
        elif self.type == "null":
            return "好可惜呢，什么都没抽中……（目移）"



@dataclass
class UserState:
    buttons: int = 0
    affection: int = 0
    bag: dict[str, int] = field(default_factory=dict)
    arbeit_start_time: int = -1
    arbeit_name: str = ""
    signed: bool = False
    last_reply: str = ""


@dataclass
class UserInfo:
    id: str = ""
    group_id: str = ""
    name: str = ""
    gender: Literal["male", "female", "unknown"] = "unknown"
    img_url: str = ""
    img: BuildImage = BuildImage.new("RGBA", (640, 640))
    db_name: str = "data/user_states.db"

    def save_states(self, state: UserState):
        state = json.dumps(asdict(state))
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM USER_STATE WHERE id=?", (int(self.id),))
            count = cursor.fetchone()[0]
        except sqlite3.OperationalError:
            count = 0
        if count == 0:
            cursor.execute("INSERT INTO USER_STATE (id, user_data) VALUES (?, ?)", (int(self.id), state))
        else:
            cursor.execute("UPDATE USER_STATE SET user_data=? WHERE id=?", (state, int(self.id)))
        conn.commit()

    def load_states(self) -> UserState:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT user_data FROM USER_STATE WHERE id=?", (int(self.id),))
        row = cursor.fetchone()
        if row:
            json_data = row[0]
            loaded_data = json.loads(json_data)
            return UserState(**loaded_data)
        else:
            return UserState()

