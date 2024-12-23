from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from faker import Faker


def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Мой хабр", url='https://habr.com/ru/users/yakvenalex/')],
        [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=yakvenalexx')],
        [InlineKeyboardButton(text="Веб приложение", web_app=WebAppInfo(url="https://tg-promo-bot.ru/questions"))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

from faker import Faker

def get_random_person():
    # Создаем объект Faker с русской локализацией
    fake = Faker('ru_RU')

    # Генерируем случайные данные пользователя
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'birth_date': fake.date_of_birth(),
        'company': fake.company(),
        'job': fake.job()
    }
    return user