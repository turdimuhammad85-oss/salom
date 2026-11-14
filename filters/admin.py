from aiogram import types, filters
from config.settings import ADMINS

class AdminFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message):
        return str(msg.from_user.id) in ADMINS
