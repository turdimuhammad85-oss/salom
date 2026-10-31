from aiogram import Router, types, F
rt = Router()
@rt.message(F.location)
async def location(msg: types.Message):
   await msg.answer("bu location")