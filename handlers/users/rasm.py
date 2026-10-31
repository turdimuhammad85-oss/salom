from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("rasm"))
async def test(msg: types.Message):
    print(msg.from_user.id)
    await msg.answer_photo("https://www.google.com/imgres?q=mrbeas&imgurl=https%3A%2F%2Fthumb.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F4%2F47%2FMrBeast_in_2026_%2528cropped_4%2529.png%2F250px-MrBeast_in_2026_%2528cropped_4%2529.png%3Futm_source%3Den.wikipedia.org%26utm_campaign%3Dparser%26utm_content%3Dthumbnail&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMrBeast&docid=qu2c2QucsWuNwM&tbnid=vRwy_dgTqtP8IM&vet=12ahUKEwi_oJO3obuXAxXzQ_EDHXjSAjMQnPAOegUI6wEQAA..i&w=250&h=334&hcb=2&ved=2ahUKEwi_oJO3obuXAxXzQ_EDHXjSAjMQnPAOegUI6wEQAA")