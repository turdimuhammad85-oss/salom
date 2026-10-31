from aiogram import Router, types, F
rt = Router()
@rt.message(F.sticker)
async def sticer(msg: types.Message):
   await msg.answer("bu sticker")