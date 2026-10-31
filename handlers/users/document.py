from aiogram import Router, types, F
rt = Router()
@rt.message(F.document)
async def document(msg: types.Message):
   await msg.answer("bu document")