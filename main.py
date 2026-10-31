import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
    TelegramUnauthorizedError,
)
from aiogram.types import sticker

from config.settings import BOT_TOKEN
from handlers.users import contact
from handlers.users.test import rt as test
from handlers.users.start import rt as start
from handlers.users.help import rt as help
from handlers.users.rasm import rt as rasm
from handlers.users.id_korish import rt as id_korish
from handlers.users.reply import rt as reply
from handlers.users.delete import rt as delete
# from handlers.users.aniqla import rt as aniqla
from handlers.users.date import rt as date
from handlers.users.photo import rt as photo
from handlers.users.voice import rt as voice
from handlers.users.animation import rt as animation
from handlers.users.contact import rt as contact
from handlers.users.text import rt as text
from handlers.users.document import rt as document
from handlers.users.sticer import rt as sticer
from handlers.users.dice import rt as dice
from handlers.users.location import rt as location

dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)
    dp.include_router(start)
    dp.include_router(help)
    dp.include_router(location)
    dp.include_router(dice)
    dp.include_router(sticker)
    dp.include_router(document)
    dp.include_router(text)
    dp.include_router(contact)
    dp.include_router(animation)
    dp.include_router(voice)
    dp.include_router(photo)
    dp.include_router(date)
    # dp.include_router(aniqla)
    dp.include_router(delete)
    dp.include_router(reply)
    dp.include_router(id_korish)
    dp.include_router(rasm)
    dp.include_router(test)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga yo'q")
    except TelegramUnauthorizedError:
        print("token xato!")
