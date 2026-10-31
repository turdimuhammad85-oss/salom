from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("help"))
async def help(msg: types.Message):
    await msg.answer("sizga nima yordam beraolaman?")
    n = "bizning barcha kamandalarimiz:\n"
    n += "/settings\n"
    n += "/info\n"
    n += "/car\n"
    n += "/fruit\n"
    n += "/rasm\n"
    n += "/id_korish\n"
    n += "/reply\n"
    n += "/delete\n"
    n += "/aniqla\n"
    n += "/date\n"
    n += "/photo\n"
    n += "/voice\n"
    n += "/animation\n"
    n += "/contact\n"
    n += "/text\n"
    n += "/document\n"

    await msg.answer(n)
