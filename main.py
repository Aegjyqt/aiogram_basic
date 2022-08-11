from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import load_dotenv
import os

import keyboards
import messages

load_dotenv()

bot = Bot(
    token=os.getenv('BOT_TOKEN'),
    parse_mode='HTML'
)

dp = Dispatcher(bot=bot, storage=MemoryStorage())

class AboutPipeline(StatesGroup):
    next_step = State()

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, ' + messages.welcome)

@dp.message_handler(commands='about')
async def send_about(message: types.Message):
    await message.answer(messages.about_openline, reply_markup=keyboards.kb_about)
    await AboutPipeline.next_step.set()

@dp.callback_query_handler(text="button_next_pressed", state=AboutPipeline.next_step)
async def button_pressed(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        try:
            pipeline_index = data['iterator']
        except KeyError:
            data['iterator'] = 0
            pipeline_index = data['iterator']

        try:
            await call.message.answer(messages.about_list[pipeline_index], reply_markup=keyboards.kb_about)
            data['iterator'] = pipeline_index + 1
            await call.message.delete_reply_markup()
        except IndexError:
            await call.message.delete_reply_markup()
            await call.message.answer("Пайплайн пройден!")
            await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)
