import json
import sqlite3
from dataclasses import dataclass, asdict, field
from typing import Tuple, Callable, Union, Literal, List
from nonebot_plugin_imageutils import BuildImage


@dataclass
class Command:
    keywords: Tuple[str, ...]
    func: Callable

@dataclass
class Message:
    keyword: Tuple[str, ...]
    pattern: str
    func: Callable

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
    name: str
    affection: int
    description: str
    price: int
    on_sell: bool = True
    in_gacha: bool = False
    gacha_des: str = ""
    prob_pair: Union[float, List[Tuple[float, int]]] = 0

    def get_shop_des(self) -> str:
        return f"{self.name} 【好感度+{self.affection}】\n售价：{self.price}枚小纽扣\n说明：{self.description}\n"


@dataclass
class UserState:
    buttons: int = 0
    affection: int = 0
    bag: dict[str, int] = field(default_factory=dict)
    arbeit_start_time: int = -1
    arbeit_name: str = ""
    signed: bool = False


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

