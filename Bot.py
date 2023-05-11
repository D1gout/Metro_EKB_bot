import asyncio
import logging
import sqlite3
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

def TimeListUpdate(index):
    a = '06:05; 06:15; 06:23; 06:31; 06:38;' \
        '06:46; 06:54; 07:01; 07:08; 07:13;' \
        '07:17; 07:22; 07:26; 07:31; 07:35;' \
        '07:40; 07:44; 07:49; 07:53; 07:58;' \
        '08:02; 08:07; 08:11; 08:16; 08:20;' \
        '08:25; 08:29; 08:34; 08:38; 08:43;' \
        '08:47; 08:52; 08:56; 09:01; 09:05;' \
        '09:10; 09:14; 09:19; 09:23; 09:28;' \
        '09:32; 09:37; 09:42; 09:48; 09:53;' \
        '09:58; 10:04; 10:10; 10:16; 10:22;' \
        '10:28; 10:34; 10:40; 10:46; 10:52;' \
        '10:58; 11:04; 11:10; 11:16; 11:22;' \
        '11:30; 11:37; 11:45; 11:52; 12:00;' \
        '12:07; 13:05; 12:22; 12:30; 12:37;' \
        '12:45; 12:52; 13:00; 13:07; 13:15;' \
        '13:22; 13:30; 13:37; 13:45; 13:52;' \
        '14:00; 14:07; 14:15; 14:22; 14:30;' \
        '14:37; 14:45; 14:52; 15:00; 15:07;' \
        '15:15; 15:22; 15:30; 15:37; 15:45;' \
        '15:52; 16:00; 16:07; 16:15; 16:22;' \
        '16:30; 16:37; 16:43; 16:49; 16:55;' \
        '17:01; 17:06; 17:11; 17:15; 17:20;' \
        '17:25; 17:29; 17:34; 17:38; 17:43;' \
        '17:47; 17:52; 17:56; 18:01; 18:05;' \
        '18:10; 18:14; 18:19; 18:23; 18:28;' \
        '18:32; 18:37; 18:41; 18:46; 18:50;' \
        '18:55; 19:00; 19:05; 19:10; 19:15;' \
        '19:20; 19:25; 19:30; 19:35; 18:41;' \
        '19:47; 19:53; 19:59; 20:06; 20:13;' \
        '20:20; 20:27; 20:34; 20:41; 20:48;' \
        '20:55; 21:02; 21:10; 21:21; 21:32;' \
        '21:43; 21:54; 22:05; 22:16; 22:27;' \
        '22:38; 22:49; 23:00; 23:11; 23:22;' \
        '23:33; 23:45; 23:57; 00:09; 00:20'\
        .replace(' ', '').split(';')


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

station_buttons = InlineKeyboardMarkup()\
    .add(st1).add(st2).add(st3).add(st4).add(st5).add(st6).add(st7).add(st8).add(st9)

@dp.callback_query_handler(lambda c: c.data == 'st1_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
                               reply_markup=button_restart)
    except BotBlocked:
        await asyncio.sleep(0.1)

@dp.callback_query_handler(lambda c: c.data == 'st2_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        await bot.send_message(callback_query.from_user.id, 'Ваше направление',
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
#     await message.answer('Мои команды', reply_markup=help_comands)


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


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == '':
        await message.answer(TimeList(people_id),
                             reply_markup=button_restart)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)