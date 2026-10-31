from aiogram import Router, types, F
rt = Router()
@rt.message(F.contact)
async def contact(msg: types.Message):
   await msg.answer("bu contact")