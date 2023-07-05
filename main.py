from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import executor, types
from random import choice
import environs
from glob import glob

env = environs.Env()
env.read_env()
bot_token = env("BOT_TOKEN")
bot = Bot(token=bot_token)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Нажми '/menu' что бы получить меню")



@dp.message_handler(commands=['menu'])
async def send_menu(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Новое меню:\n")
    file_list = glob('photo_dir/*')
    file = choice(file_list)
    await bot.send_photo(chat_id=message.chat.id, photo=open(file, "rb"))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

