from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "Hello! Welcome to EngBot! 👋\n"
        "I’m here to help you learn English step by step. "
        "Let’s start by determining your English level. "
        "Press the button below to take a quick test!"
    )
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Start Level Test"))
    
    await message.answer(welcome_text, reply_markup=keyboard)