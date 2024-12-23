from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from venv1.bot.handlers.menu.profile import info_calor, function
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

router = Router()

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Формула расчёта", callback_data='function')],
        [InlineKeyboardButton(text="Расчет формулы калорий", callback_data='info_calor')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


@router.message(F.text == 'Рассчитать')
async def give_me_inline(message: Message):
    await message.answer('Начало пошло', reply_markup=ease_link_kb())

@router.callback_query(F.data == 'info_calor')
async def checker(call):
    await call.answer('Введите: Расчет формулы калорий', show_alert=False)
    await call.message.answer('Введите: Расчет формулы калорий')
    await info_calor()

@router.callback_query(F.data == 'function')
async def func(call: CallbackQuery):
    test1 = function()
    await call.answer('Сейчас всё будет', show_alert=False)
    await call.message.answer(test1)

@router.message(F.text == 'Информация')
async def func1(message: Message):
   await message.answer('Выберите одну из опций: ', reply_markup=ease_link_kb())


@router.message()
async def echo_handler(message: Message):
    try:
        await message.answer('Введите команду, а не случайный текст!')
    except TypeError:
        await message.answer("Nice Try!")