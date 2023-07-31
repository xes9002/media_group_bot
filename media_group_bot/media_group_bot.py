import logging

from aiogram import Bot, Dispatcher,executor, types

logging.basicConfig(level=logging.INFO)

Bot_token = "6153682995:AAGoKbZKFdDvJwl-JS6R_VzRsGEt3eC_8is"

bot = Bot(token=Bot_token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Assalomu aleykum")

@dp.message_handler(commands=["audio"])
async def media_handler(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile("g.ogg"), "audio1")
    media.attach_photo(types.InputFile("g.ogg"), "audio1")
    media.attach_photo(types.InputFile("g.ogg"), "audio1")
    media.attach_photo(types.InputFile("g.ogg"), "audio1")
    media.attach_photo(types.InputFile("g.ogg"), "audio1")  

    await message.answer_media_group(media=media)
    
@dp.message_handler(commands=["photo"])
async def media_handler(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile("1.jpg"), "photo1.jpg")
    media.attach_photo(types.InputFile("2.jpg"), "photo1.jpg")
    media.attach_photo(types.InputFile("3.jpg"), "photo1.jpg")
    media.attach_photo(types.InputFile("1.jpg"), "photo1.jpg")
    media.attach_photo(types.InputFile("2.jpg"), "photo1.jpg")    
    media.attach_photo(types.InputFile("2.jpg"), "photo1.jpg")    
    media.attach_photo(types.InputFile("2.jpg"), "photo1.jpg")    
    media.attach_photo(types.InputFile("2.jpg"), "photo1.jpg")    
    
if __name__ == "__main__":
    executor.start_polling(dp)
