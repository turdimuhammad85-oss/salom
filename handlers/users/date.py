from aiogram import Router, types, filters
import datetime
rt = Router()
@rt.message(filters.Command("date"))
async def date(msg: types.Message):
   # await msg.answer(str(msg.text))
   hozir = datetime.timedelta(hours=5) + msg.date
   soat = hozir.hour
   minut = hozir.minute
   sekund = hozir.second
   n = "hozir soat:\n"
   n += f"{soat:02}:{minut:02}:{sekund:02}\n"
   await msg.answer(n)

@rt.message(filters.Command("sana"))
async def sana(msg: types.Message):
   hozir = datetime.timedelta(hours=5) + msg.date
   yil = hozir.year
   oy = hozir.month
   kun = hozir.day
   n = "bugungi sana:\n"
   n += f"{yil}-{oy:02}-{kun:02}\n"
   await msg.answer(n)
