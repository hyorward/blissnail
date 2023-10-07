from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add('Каталог 🗂').add('Корзина 🗑').add('Контакты 📱')

markup_admin = ReplyKeyboardMarkup(resize_keyboard=True)
markup_admin.add('Каталог 🗂').add('Корзина 🗑').add('Контакты 📱').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить услугу').add('Удалить услугу').add('Изменить услугу').add('Сделать рассылку')

catalog_list = InlineKeyboardMarkup(row_width=1)
catalog_list.add(InlineKeyboardButton(text='МАНИКЮР (АППАРАТ,КОМБИ,КЛАССИКА) БЕЗ ПОКРЫТИЯ НОГТЕЙ', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='МАНИКЮР + ПОКРЫТИЕ ГЕЛЬ-ЛАК', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='СНЯТИЕ ГЕЛЬ-ЛАКА', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='МАНИКЮР + СНЯТИЕ + ПОКРЫТИЕ ГЕЛЬ-ЛАК', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='ФРАНЦУЗСКИЙ МАНИКЮР ГЕЛЬ-ЛАК + МАНИКЮР', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='ПОКРЫТИЕ НОГТЕЙ ЛАКОМ', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='СНЯТИЕ ЛАКА С НОГТЕЙ', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='НАРАЩИВАНИЕ НОГТЕЙ, КОРОТКИЕ / ДЛИННЫЕ', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='НАРАЩИВАНИЕ НОГТЕЙ (ФРАНЦУЗСКИЙ МАНИКЮР), КОРОТКИЕ / ДЛИННЫЕ', url='https://milou-salon.ru/'),
                 InlineKeyboardButton(text='НАРАЩИВАНИЕ 1 НОГОТЬ', url='https://milou-salon.ru/'))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAM-ZSFTRW85SHQfYXKZEe2UAfnq6KMAAtwFAAI_lcwK8V_szGQXFZcwBA')
    await message.answer(f' <em>{message.from_user.first_name}, добро пожаловать в онлайн-салон маникюра <b>"BLISS"</b>! </em>', reply_markup=markup, parse_mode="html")
    if message.from_user.id == int(os.getenv('ADMIN_ID_1')) or message.from_user.id == int(os.getenv('ADMIN_ID_2')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=markup_admin)


@dp.message_handler(commands=['id'])
async def admin_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')


@dp.message_handler(text='Каталог 🗂')
async def catalog(message: types.Message):
    await message.answer(f'<em>В данный момент каталог пуст(</em>', parse_mode="html", reply_markup=catalog_list)


@dp.message_handler(text='Корзина 🗑')
async def cart(message: types.Message):
    await message.answer(f'<em>Корзина пуста!</em>', parse_mode="html")


@dp.message_handler(text='Контакты 📱')
async def contacts(message: types.Message):
    await message.answer(f'<em>По всем вопросам обращайтесь к нашему администратору: @miytiiiii</em>', parse_mode="html")


@dp.message_handler(text='Админ-панель')
async def admin(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID_1')) or message.from_user.id == int(os.getenv('ADMIN_ID_2')):
        await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)
    else:
        await message.reply('Я вас не понимаю.')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я вас не понимаю.')


if __name__ == '__main__':
    executor.start_polling(dp)