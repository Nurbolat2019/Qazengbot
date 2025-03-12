import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, level_test
import aiohttp
import ssl

logging.basicConfig(level=logging.INFO)

# Бот пен диспетчерді жасау
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(level_test.router)

async def main():
    # SSL контекстін жасау және сертификатты қосу
  ssl_context = ssl.create_default_context(cafile="C:/python/engbot/Unified_State_Internet_Access_Gateway.cer") # PEM файлының жолы
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context))
    
    # Ботқа сессияны орнату
    bot.session = session
    
    print("EngBot іске қосылды...")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()  # Сессияны жабу

if __name__ == "__main__":
    asyncio.run(main())


