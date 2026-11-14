from aiogram import Router, types
rt = Router()
@rt.message(F.document)
async def chatphoto(msg: types.Message):
   await msg.answer("chatphoto")