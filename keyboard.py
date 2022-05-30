from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

Keyboard = InlineKeyboardMarkup()
but0 = InlineKeyboardButton(text="Поделится ботом с друзями;)", callback_data="0")
but1 = InlineKeyboardButton(text="1. Суп АВП/АК, текстури", callback_data="1")
but2 = InlineKeyboardButton(text="2. Без Лим патрони/жизнь/деньги", callback_data="2")
but3 = InlineKeyboardButton(text="3. PINGUINO BEST-HACK", callback_data="3")
but4 = InlineKeyboardButton(text="4. Mod chead 1 ", callback_data="4")
but5 = InlineKeyboardButton(text="5. RPG500, MaxHP, Max$, 100% Online", callback_data="5")
Keyboard.add(but0)
Keyboard.add(but1)
Keyboard.add(but2)
Keyboard.add(but3)
Keyboard.add(but4)
Keyboard.add(but5)

botslit = InlineKeyboardMarkup()
botslit1 = InlineKeyboardButton(text="Посмотри сюда, но не бойся:)", url="t.me/+cRl0svNw2wozYTUy")
botslit.add(botslit1)

replye = InlineKeyboardMarkup()
reply = InlineKeyboardButton("Поделится", switch_inline_query="етот бот которого я недавно нашел он видает чити, на игру которую ми играем, 2D Strike и там много разних читов, и главное их можно скачать безплатно, и очень бистро!")
replye.add(reply)

delletec = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Спасибо, за регистрацию)"))
Contact = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой номер ☎️', request_contact=True)
)
