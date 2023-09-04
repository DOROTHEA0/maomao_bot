from nonebot.adapters import Event


async def ARN(event: Event):
    return event.get_user_id() == "963962002"
