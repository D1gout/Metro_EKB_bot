import logging

from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN


class ParamList:
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

    st1_update = InlineKeyboardButton('Ботаническая (1)', callback_data='st1_update')
    st2_update = InlineKeyboardButton('Чкаловская (2)', callback_data='st2_update')
    st3_update = InlineKeyboardButton('Геологическая (3)', callback_data='st3_update')
    st4_update = InlineKeyboardButton('Площадь 1905 года (4)', callback_data='st4_update')
    st5_update = InlineKeyboardButton('Динамо (5)', callback_data='st5_update')
    st6_update = InlineKeyboardButton('Уральская (6)', callback_data='st6_update')
    st7_update = InlineKeyboardButton('Машиностроителей (7)', callback_data='st7_update')
    st8_update = InlineKeyboardButton('Уралмаш (8)', callback_data='st8_update')
    st9_update = InlineKeyboardButton('Проспект космонавтов (9)', callback_data='st9_update')

    st1_button = InlineKeyboardMarkup().add(st1_update)
    st2_button = InlineKeyboardMarkup().add(st2_update)
    st3_button = InlineKeyboardMarkup().add(st3_update)
    st4_button = InlineKeyboardMarkup().add(st4_update)
    st5_button = InlineKeyboardMarkup().add(st5_update)
    st6_button = InlineKeyboardMarkup().add(st6_update)
    st7_button = InlineKeyboardMarkup().add(st7_update)
    st8_button = InlineKeyboardMarkup().add(st8_update)
    st9_button = InlineKeyboardMarkup().add(st9_update)

    station_buttons = InlineKeyboardMarkup() \
        .add(st1).add(st2).add(st3).add(st4).add(st5).add(st6).add(st7).add(st8).add(st9)
