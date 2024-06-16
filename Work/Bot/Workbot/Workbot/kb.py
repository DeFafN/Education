from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu_but = [
    [InlineKeyboardButton(text = "Про успех", callback_data = "succes"),
    InlineKeyboardButton(text = "Про участие в мероприятии", callback_data = "event")],
    [InlineKeyboardButton(text = "Про апдейт в процессах / инструментах", callback_data = "process"),
    InlineKeyboardButton(text = "Про необычный кейс", callback_data = "case")],
    [InlineKeyboardButton(text = "Про важное личное событие", callback_data = "personal_event")]
    ]
menu = InlineKeyboardMarkup(inline_keyboard = menu_but)

second_menu_but = [
    [InlineKeyboardButton(text = "Да", callback_data = "yes"),
    InlineKeyboardButton(text = "С коллегой", callback_data = "colleague")],
    [InlineKeyboardButton(text = "Другое", callback_data = "other")]
    ]
second_menu = InlineKeyboardMarkup(inline_keyboard = second_menu_but)

speed_menu_but = [
    [InlineKeyboardButton(text="Да", callback_data = "yes"),
    InlineKeyboardButton(text="Нет", callback_data = "no")],
    ]
speed_menu = InlineKeyboardMarkup(inline_keyboard = speed_menu_but)

need_help_menu_but = [
    [InlineKeyboardButton(text = "Есть готовый текст", callback_data = "have_text"),
    InlineKeyboardButton(text = "Есть текст, нужна помощь в редактуре", callback_data = "need_edit")],
    [InlineKeyboardButton(text = 'Нужна помощь в написании', callback_data = "need_help")]
    ]
need_help_menu = InlineKeyboardMarkup(inline_keyboard = need_help_menu_but)