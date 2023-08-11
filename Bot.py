import asyncio
import time
import CheckTime
from TimeList import TimeList

from aiogram import executor, types
from aiogram.utils.exceptions import BotBlocked, MessageNotModified

from params import ParamList


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st1_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st2.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st1_B)}",
                                         reply_markup=ParamList.st1_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st1_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st2.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st1_B)}",
                                              reply_markup=ParamList.st1_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st2_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st1.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st2_in_B)}\n\n\n"
                                                                      f"В сторону {ParamList.st3.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st2_in_P)}",
                                         reply_markup=ParamList.st2_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st2_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st1.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st2_in_B)}\n\n\n"
                                                   f"В сторону {ParamList.st3.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st2_in_P)}",
                                              reply_markup=ParamList.st2_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st3_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st2.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st3_in_B)}\n\n\n"
                                                                      f"В сторону {ParamList.st4.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st3_in_P)}",
                                         reply_markup=ParamList.st3_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st3_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st2.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st3_in_B)}\n\n\n"
                                                   f"В сторону {ParamList.st4.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st3_in_P)}",
                                              reply_markup=ParamList.st3_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st4_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st3.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st4_in_B)}\n\n\n"
                                                                      f"В сторону {ParamList.st5.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st4_in_P)}",
                                         reply_markup=ParamList.st4_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st4_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st3.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st4_in_B)}\n\n\n"
                                                   f"В сторону {ParamList.st5.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st4_in_P)}",
                                              reply_markup=ParamList.st4_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st5_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st4.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st5_in_B)}\n\n\n"
                                                                      f"В сторону {ParamList.st6.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st5_in_P)}",
                                         reply_markup=ParamList.st5_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st5_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st4.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st5_in_B)}\n\n\n"
                                                   f"В сторону {ParamList.st6.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st5_in_P)}",
                                              reply_markup=ParamList.st5_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st6_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st5.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st6_in_B)}\n\n\n"
                                                                      f"В сторону {ParamList.st7.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st6_in_P)}",
                                         reply_markup=ParamList.st6_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st6_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st5.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st6_in_B)}\n\n\n"
                                                   f"В сторону {ParamList.st7.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st6_in_P)}",
                                              reply_markup=ParamList.st6_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st7_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st6.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st7_in_B)}\n\n\n"
                                                                      f"В сторону {ParamList.st8.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st7_in_P)}",
                                         reply_markup=ParamList.st7_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st7_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st6.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st7_in_B)}\n\n\n"
                                                   f"В сторону {ParamList.st8.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st7_in_P)}",
                                              reply_markup=ParamList.st7_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st8_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st7.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st8_in_B)}\n\n\n"
                                                                      f"В сторону {ParamList.st9.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st8_in_P)}",
                                         reply_markup=ParamList.st8_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st8_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st7.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st8_in_B)}\n\n\n"
                                                   f"В сторону {ParamList.st9.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st8_in_P)}",
                                              reply_markup=ParamList.st8_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st9_click')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)
    try:
        await ParamList.bot.send_message(callback_query.from_user.id, f"В сторону {ParamList.st8.text}\n\n"
                                                                      f"{CheckTime.CheckTime(TimeList.st9_P)}",
                                         reply_markup=ParamList.st9_button)
    except BotBlocked:
        await asyncio.sleep(0.1)


@ParamList.dp.callback_query_handler(lambda c: c.data == 'st9_update')
async def process_callback_button(callback_query: types.CallbackQuery):
    await ParamList.bot.answer_callback_query(callback_query.id)

    try:
        await ParamList.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                              message_id=callback_query.message.message_id,
                                              text=f"Обновлено в {time.strftime('%H:%M')}\n\n"
                                                   f"В сторону {ParamList.st8.text}\n\n"
                                                   f"{CheckTime.CheckTime(TimeList.st9_P)}",
                                              reply_markup=ParamList.st9_button)
    except MessageNotModified:
        await asyncio.sleep(0.1)


# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.answer('Мои команды', reply_markup=help_commands)


@ParamList.dp.message_handler(commands=['info'])
async def process_info_command(message: types.Message):
    await message.answer('Версия 1.0.0\n\n'
                         'Бот в котором можно узнать когда приедет поезд')


@ParamList.dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(
        "Привет!",
        reply_markup=ParamList.link_button)
    await message.answer(
        "Выбери свою станцию",
        reply_markup=ParamList.station_buttons)


# @dp.message_handler()
# async def echo(message: types.Message):
#     if message.text == '':
#         await message.answer(TimeList(people_id),
#                              reply_markup=button_restart)


if __name__ == '__main__':
    executor.start_polling(ParamList.dp, skip_updates=True)
