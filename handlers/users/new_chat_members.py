from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.new_chat_members)
async def new_chat_members(message: Message):
    for user in message.new_chat_members:
        await message.answer(f"Guruhga xush kelibsiz, {user.full_name}")