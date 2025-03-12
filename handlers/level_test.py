from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Router объектісін жасау
router = Router()

# Күйлерді анықтау
class LevelTest(StatesGroup):
    question1 = State()
    question2 = State()
    result = State()

# "Start Level Test" түймесін өңдеу
@router.message(lambda message: message.text == "Start Level Test")  # Text жоқ, lambda қолданылады
async def start_level_test(message: types.Message, state: FSMContext):
    await message.answer("Great! Let’s determine your English level. Here’s the first question:\n\n"
                         "What is the past tense of 'go'?\n"
                         "a) Goed\nb) Went\nc) Gone\nd) Going",
                         reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).row("a", "b", "c", "d"))
    await LevelTest.question1.set()

# Бірінші сұрақтың жауабын өңдеу
@router.message(LevelTest.question1)
async def process_question1(message: types.Message, state: FSMContext):
    await state.update_data(q1=message.text)
    await message.answer("Good! Next question:\n\n"
                         "Which word means 'happy'?\n"
                         "a) Sad\nb) Angry\nc) Joyful\nd) Tired",
                         reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).row("a", "b", "c", "d"))
    await LevelTest.question2.set()

# Екінші сұрақтың жауабын өңдеу және нәтиже
@router.message(LevelTest.question2)
async def process_question2(message: types.Message, state: FSMContext):
    await state.update_data(q2=message.text)
    user_data = await state.get_data()
    q1, q2 = user_data["q1"], user_data["q2"]
    
    score = 0
    if q1 == "b":  # "Went" дұрыс жауап
        score += 1
    if q2 == "c":  # "Joyful" дұрыс жауап
        score += 1
    
    if score == 2:
        level = "Intermediate"
    elif score == 1:
        level = "Elementary"
    else:
        level = "Beginner"
    
    await message.answer(f"Your test is complete! Your level is: {level}",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()