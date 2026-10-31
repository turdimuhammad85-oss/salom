from aiogram import Router, types, filters
rt = Router()
@rt.message()
async def test(msg: types.Message):
    print(msg.from_user.id)
    # await msg.answer_dice(emoji="🎲")
    # await msg.forward(chat_id=8744975719)
    # await msg.copy_to(chat_id=8744975719)
    # await msg.pin()
    # await msg.delete()
    # await msg.answer(str(msg.text))
    # await msg.reply("qales")
    # await msg.answer_photo("https://en.wikipedia.org/wiki/MrBeast", caption="ma ukam")

