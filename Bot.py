import asyncio
import logging
import sqlite3
from datetime import datetime
import CheckTime
from TimeList import TimeList

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

info = KeyboardButton('/info')
button_info = ReplyKeyboardMarkup(resize_keyboard=True).add(info)

start = KeyboardButton('/start')
button_start = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True).add(start)

restart = KeyboardButton('Обновить')
button_restart = ReplyKeyboardMarkup(resize_keyboard=True).add(restart)

link_button = InlineKeyboardMarkup().add(InlineKeyboardButton(
    'Написать мне',
    url='https://t.me/Aweyout'))

st1 = InlineKeyboardButton('Ботаническая (1)', callback_data='st1_click')
st2 = InlineKeyboardButton('Чкаловская (2)', callback_data='st2_click')
st3 = InlineKeyboardButton('Геологическая (3)', callback_data='st3_click')
st4 = InlineKeyboardButton('Площадь 1905 года (4)', callback_data='st4_click')
st5 = InlineKeyboardButton('Динамо (5)', callback_data='st5_click')
st6 = InlineKeyboardButton('Уральская (6)', callback_data='st6_click')
st7 = InlineKeyboardButton('Машиностроителей (7)', callback_data='st7_click')
st8 = InlineKeyboardButton('Уралмаш (8)', callback_data='st8_click')
st9 = InlineKeyboardButton('Проспект космонавтов (9)', callback_data='st9_click')

station_buttons = InlineKeyboardMarkup() \
    .add(st1).add(st2).add(st3).add(st4).add(st5).add(st6).add(st7).add(st8).add(st9)


@dp.callback_query_handler(lambda c: c.data == 'st1_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, f"В сторону {st2.text}\n\n"
                                                            f"{CheckTime.CheckTime(TimeList.st1_B)}",
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


@dp.callback_query_handler(lambda c: c.data == 'st2_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, f"В сторону {st1.text}\n\n"
                                                            f"{CheckTime.CheckTime(TimeList.st2_B_in_B)}\n\n\n"
                                                            f"В сторону {st3.text}\n\n"
                                                            f"{CheckTime.CheckTime(TimeList.st2_B_in_P)}",
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


@dp.callback_query_handler(lambda c: c.data == 'st3_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


@dp.callback_query_handler(lambda c: c.data == 'st4_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


@dp.callback_query_handler(lambda c: c.data == 'st5_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


@dp.callback_query_handler(lambda c: c.data == 'st6_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


@dp.callback_query_handler(lambda c: c.data == 'st7_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


@dp.callback_query_handler(lambda c: c.data == 'st8_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


@dp.callback_query_handler(lambda c: c.data == 'st9_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)


# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.answer('Мои команды', reply_markup=help_commands)


@dp.message_handler(commands=['info'])
async def process_info_command(message: types.Message):
    await message.answer('Версия 1.0.0\n\n'
                         'Бот в котором можно узнать когда приедет поезд')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(
        "Привет!",
        reply_markup=link_button)
    await message.answer(
        "Я бот который скидывает расписание\n\nВыбери свою станцию",
        reply_markup=station_buttons)


# @dp.message_handler()
# async def echo(message: types.Message):
#     if message.text == '':
#         await message.answer(TimeList(people_id),
#                              reply_markup=button_restart)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
