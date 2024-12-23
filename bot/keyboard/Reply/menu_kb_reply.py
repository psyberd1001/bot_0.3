from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
def menu_kb() -> ReplyKeyboardMarkup:
    kb_main = ReplyKeyboardBuilder()
    kb_main.button(text='Информация')
    kb_main.button(text='Расчет формулы калорий')
    kb_main.adjust(2)
    return kb_main.as_markup(resize_keyboard=True)