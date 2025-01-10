from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties

from modules.config import TOKEN

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(
        parse_mode='HTML',
        link_preview_is_disabled=True,
        protect_content=False
    )
)