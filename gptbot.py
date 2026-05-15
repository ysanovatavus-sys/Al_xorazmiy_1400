from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from req import ai_chat

#qatar qostim

api = '8745752908:AAHMmHLanzs1XJ1xK64pIlJNXszKNKDvkgY'
bot = Bot(api)
dp=Dispatcher()

async def main():
    await dp.start_polling(bot)

@dp.message(Command('start'))
async def send_salem(sms:types.Message):
    await sms.answer(text=f'Salom, savolingizni yozing: -{sms.from_user.first_name}')
    
@dp.message()
async def ai_chat_answer(sms:types.Message):
    javob = await ai_chat(savol=sms.text)
    await sms.answer(text=javob)



if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
