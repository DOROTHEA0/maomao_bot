import nonebot
from nonebot.adapters.console import Adapter as ConsoleAdapter  # 避免重复命名
from nonebot.adapters.onebot import V11Adapter as OneBotAdapter

# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(OneBotAdapter)

nonebot.load_builtin_plugins("echo")
nonebot.load_plugins("maomao_bot/plugins")

if __name__ == "__main__":
    nonebot.run()