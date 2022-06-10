from googletrans import Translator
from config import TOKEN
import logging
from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor, types
from button import *
logging.basicConfig(level=logging.INFO)
tar = Translator()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply("Salom! \nMen tarjimon botman \nTarjima qilinmoqchi bo'lgan so'zizni kiriting",parse_mode='HTML')



@dp.message_handler()
async def echo(message: types.Message):
	global soz
	soz = message.text
	await message.answer("Tilni tanlang❕",parse_mode='HTML',reply_markup=tillar)





@dp.callback_query_handler(text="ru")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="ru")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="en")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="en")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="ar")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="ar")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="tg")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="tg")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="uk")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="uk")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="vi")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="vi")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="es")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="es")
	await call.message.answer(display.text)		

@dp.callback_query_handler(text="sv")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="sv")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="bg")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="bg")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="ko")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="ko")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="kk")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="kk")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="kn")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="kn")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="it")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="it")
	await call.message.answer(display.text)	

@dp.callback_query_handler(text="de")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="de")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="hy")
async def russian(call: CallbackQuery):
	display=tar.translate(soz,dest="hy")
	await call.message.answer(display.text)		




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






# # Birinchi ko'rinish
# tarj = Translator()
# natija = tarj.translate("salom",dest="ru")
# print(natija)


# Ikkinchi ko'rinish

# tarj = Translator()
# suz = input("So'z kiriting: ")
# natija = tarj.translate(suz,dest="ru")
# print(natija.text)

# Uchinchi ko'rinish

# tarj = Translator()
# suz = input("So'z kiriting: ")
# til = input("Tarjima qilmoqchi bo'lgan tilni kiriting: ")
# natija = tarj.translate(suz,dest=til)
# print(natija.text)