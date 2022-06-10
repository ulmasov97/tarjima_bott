from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

tillar = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="🇷🇺 Russian",callback_data="ru"),
				InlineKeyboardButton(text ="🇬🇧 England",callback_data="en"),
				InlineKeyboardButton(text ="🇸🇦 Arabic",callback_data="ar")
		],
		[
				InlineKeyboardButton(text ="🇹🇯 Tajik",callback_data="tg"),
				InlineKeyboardButton(text ="🇺🇦 Ukrainian",callback_data="uk"),
				InlineKeyboardButton(text ="🇻🇳 Vietnamese",callback_data="vi")
		],
		[
				InlineKeyboardButton(text ="🇪🇸 Spanish",callback_data="es"),
				InlineKeyboardButton(text ="🇸🇰 Slovak",callback_data="sv"),
				InlineKeyboardButton(text ="🇧🇬 Bulgarian",callback_data="bg")
		],
		[
				InlineKeyboardButton(text ="🇰🇷 Korean",callback_data="ko"),
				InlineKeyboardButton(text ="🇰🇿 Kazakh",callback_data="kk"),
				InlineKeyboardButton(text ="🇨🇦 Kannada",callback_data="kn")
		],
		[
				InlineKeyboardButton(text ="🇮🇹 Italian",callback_data="it"),
				InlineKeyboardButton(text ="🇩🇪 German",callback_data="de"),
				InlineKeyboardButton(text ="🇦🇲 Armenian",callback_data="hy")
		],

	],
)











