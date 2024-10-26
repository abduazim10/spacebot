import logging


from aiogram import Bot, Dispatcher, types, executor
from config import API_TOKEN
from keyboards import start_keyboards , school_keyboards , otziv_keyboards, start_keyboards2
from aiogram.types import InputFile , MediaGroup
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN, proxy='http://proxy.server:3128')
dp = Dispatcher(bot,storage=MemoryStorage())




@dp.message_handler(commands='start')
async def welcome(message: types.Message):

    

    await message.answer(f'Assalomu aleykum {message.from_user.full_name}!' , reply_markup=start_keyboards2)
    
Oquvchilar = [
    {
        'id1' : '111111',
        'parol1':'111111',
        'coin' : '481',
        'Ism':'Abduazim',
        'Familiya':'Qayumxojayev',
        'ucheb':'Тинчлик'
    }
]

Ism = ''
Familiya ='' 
Coin =''
ucheb_center =''

class RegisterState(StatesGroup):
    ism = State()
    parol = State()

@dp.message_handler(lambda message: "Profil 👤" in message.text)
async def registration(message: types.Message):
 

    await message.answer(text="Id ni Kiriting:")
    await RegisterState.ism.set()

@dp.message_handler(state=RegisterState.ism)
async def full_name(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text)

    await message.answer(text="parol:")
    await RegisterState.parol.set()

@dp.message_handler(state=RegisterState.parol)
async def data_get(message: types.Message, state: FSMContext):
    global Ism
    global Familiya
    global Coin
    global ucheb_center
    await state.update_data(parol=message.text)
    dat = await state.get_data()  # dict
    for o in Oquvchilar:
        if o['parol1'] == dat['parol'] and o['id1'] == dat['ism']  :
            Ism = o['Ism']
            Familiya = o['Familiya']
            Coin = o['coin']
            ucheb_center = o['ucheb']
            await message.answer(f'Salom {Ism} {Familiya}!', reply_markup=start_keyboards)
            await state.finish()  
            return  
        await message.answer('Id yoki parol noto‘g‘ri!')  # Handle invalid credentials
        await state.finish()


class ReviewState(StatesGroup):
    waiting_for_review = State()

@dp.message_handler(lambda message: '✍️ Оставить отзыв' in message.text)
async def ask_for_review(message: types.Message):
    photo1 = InputFile('images/image1.png')
    await message.answer_photo(photo=photo1, caption='Напишите свой отзыв')
    

    await ReviewState.waiting_for_review.set()


@dp.message_handler(state=ReviewState.waiting_for_review)
async def handle_review(message: types.Message, state: FSMContext):

    review_text = message.text 
    photo2 = InputFile('images/image2.png')

    await message.answer_photo(photo=photo2,caption='Спасибо что помогаете нам улучшатся')


    await state.finish()

@dp.message_handler()
async def keyboards_func(message: types.Message):
    global Ism
    global Familiya
    global Coin
    global ucheb_center
    try:
        

        if message.text == '🧑‍🎓 Профиль':
            await message.answer(f'Имя: {Ism}\nФамилия: {Familiya}\nЯзык: ру\nУчебный центр: {ucheb_center}')



        elif message.text == '🪙 Мои монеты':
            await message.answer(f'Мои марс монеты: {Coin}')
        elif message.text == '💥 Space Shop':
            await message.answer(f'Для покупки продукции перейдите на https://space.marsit.uz')
        elif message.text == '🏫 О школе':
            await message.answer(f'Birortasini Tanlang:' , reply_markup=school_keyboards)
        
            
            


    except Exception as e:
        print('Error: ', e)
        await message.answer(f'Xatolik yuz berdi, iltimos qaytadan urinib ko\'ring | ERROR {e}')




@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
    call_data = call.data 
    if call_data == 'schoolm_1':
        myvideo = InputFile("videos/video1.mp4")
        await bot.send_video(chat_id=call.from_user.id , video=myvideo , caption='Философия школы')
    elif call_data == 'schoolm_2':
        media_group = MediaGroup()
        media_group.attach({"type": "video", "media": InputFile("videos/video2.mp4"), "caption": "Преподаватели"})
        media_group.attach({"type": "video", "media": InputFile("videos/video3.mp4")})
        media_group.attach({"type": "video", "media": InputFile("videos/video4.mp4")})
        media_group.attach({"type": "video", "media": InputFile("videos/video5.mp4")})

        await bot.send_media_group(chat_id=call.from_user.id, media=media_group)
    elif call_data == 'schoolm_3':
        myvideo2 = InputFile("videos/wideo6.mp4")
        await bot.send_video(chat_id=call.from_user.id , video=myvideo2 , caption='Экскурсия по школе')
    elif call_data == 'schoolm_5':
        await bot.send_message(chat_id=call.from_user.id, text='Выберите опцию:', reply_markup=otziv_keyboards)
    elif call_data == 'schoolm_4':
        media_group = MediaGroup()
        media_group.attach({"type": "video", "media": InputFile("videos/video7.mp4"), "caption": "Работы учеников \n(Ozi 4ta video edi telegram limiti bor ekan)"})
        media_group.attach({"type": "video", "media": InputFile("videos/video8.mp4")})

        await bot.send_media_group(chat_id=call.from_user.id, media=media_group)
    elif call_data == 'otziv_1':
        video11 = InputFile("videos/video11.mp4")
        await bot.send_video(chat_id=call.from_user.id , video=video11 , caption='работы детей 8-10 лет')
       
        await bot.send_media_group(chat_id=call.from_user.id, media=media_group)
    elif call_data == 'otziv_2':
        media_group = MediaGroup()
        media_group.attach({"type": "video", "media": InputFile("videos/video12.mp4"), "caption": "работы учеников 14-16 лет"})
        media_group.attach({"type": "video", "media": InputFile("videos/video13.mp4")})
        await bot.send_media_group(chat_id=call.from_user.id, media=media_group)

       





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)