from aiogram import types
from loader import dp
from utils.GetDogPhoto import sendRequest

@dp.message_handler()
async def send_dog(message: types.Message):
    dog = sendRequest()
    await message.answer(dog)