import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from api_requests import add_user


API_TOKEN = '5341761088:AAGApvhSlpyem6dbUj7G5uwe570-O--wiSE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    login = State()
    user_id = State()
    password = State()


@dp.message_handler(commands=['registration'])
async def cmd_start(message: types.Message):
    await Form.login.set()
    await message.reply("send your login \nor send /cancel to exit from registration")


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('ОК')


@dp.message_handler(state=Form.login)
async def process_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text

    await Form.next()
    await message.reply("send your user_id \nor send /cancel to exit from registration")


@dp.message_handler(state=Form.user_id)
async def process_user_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text

    await Form.next()
    await message.reply("send your password \nor send /cancel to exit from registration")


@dp.message_handler(state=Form.password)
async def process_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
        response = await add_user(data.as_dict())
        await message.reply(response)
    await state.finish()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm registration bot!\nPlease use /get_info to got your user_id and login.")


@dp.message_handler(commands=['get_info'])
async def register(message: types.Message):
    await message.reply(f"user_id: {message['from'].id}, \nlogin: {message['from'].username} \n\nnow user "
                        f"/registration to create user")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
