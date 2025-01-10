from aiogram import Router, types, F
from aiogram.filters import Command

from modules.bot_commands import forward_msg
from modules.config import GROUP_ID, CHAT_ID

router = Router()


async def get_ria_news_post(msg: types.Message):
    await forward_msg(CHAT_ID, CHAT_ID, msg.message_id, anonim=True)


async def register_generic_handlers():
    router.message.register(lambda msg: print(msg.chat.id), Command('id'))
    router.message.register(get_ria_news_post, F.forward_from_chat & (F.forward_from_chat.id == GROUP_ID) & (
                CHAT_ID == F.chat.id))
