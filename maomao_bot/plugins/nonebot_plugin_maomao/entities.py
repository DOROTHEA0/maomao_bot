from dataclasses import dataclass
from typing import Tuple, Callable, Union, Literal

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
    institution: str
    description: str
    insufficient_des: str
    normal_ending_des: str
    abnormal_ending_des: str
    occurrence_rate: float
    normal_rate: float
    normal_reward: Union[range, int]
    abnormal_reward: Union[range, int]

    def get_info(self):
        return "【" + self.institution + "】" + "\n" + self.description


@dataclass
class Item:
    pass




@dataclass
class Shop:
    pass


@dataclass
class UserInfo:
    qq: str = ""
    group: str = ""
    name: str = ""
    gender: Literal["male", "female", "unknown"] = "unknown"
    img_url: str = ""
    # img: BuildImage = BuildImage.new("RGBA", (640, 640))
    buttons: int = 0

    def save_buttons(self):
        pass