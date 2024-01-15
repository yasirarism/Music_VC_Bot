from typing import List

from pyrogram.types import Chat, User

import cache.admins


async def get_administrators(chat: Chat) -> List[User]:
    if get := cache.admins.get(chat.id):
        return get
    administrators = await chat.get_members(filter="administrators")
    to_set = [
        administrator.user.id
        for administrator in administrators
        if administrator.can_manage_voice_chats
    ]
    cache.admins.set(chat.id, to_set)
    return await get_administrators(chat)
