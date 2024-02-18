import asyncio
import logging
from CreateGame import CreateGame
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from GetFlag import GetFlagImageURL
from Top import AddScore, GetTop
from dotenv import load_dotenv
import os
import Memory

load_dotenv()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
PROXY_URL = "http://proxy.server:3128"
bot = Bot(token=os.getenv('TOKEN'))
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def start_game(message: types.Message):
    Memory.Register(str(message.from_user.id), message.from_user.full_name)
    game = CreateGame(5)
    question = f"Какая из эти стран - {game['answer'][2]}?"
    await message.answer(f"{question}")

    print(game['answer'][0])
    i = 1
    for country in game['countries']:
        if game['answer'][0] == country[0]:
            game['answer'].append(str(i))
            Memory.SetAnswer(str(message.from_user.id), f"{game['answer'][0]};{i}")
        country.append(i)
        await bot.send_photo(message.chat.id, GetFlagImageURL(country[1]), caption=f"{country[0]} - {i}")
        i += 1



@dp.message(lambda message: not message.text.startswith('/'))
async def cmd_answer(message: types.Message):
    answer = Memory.GetAnswer(str(message.from_user.id))
    answer = answer.split(';')

    if message.text.lower() == answer[0].lower() or message.text == answer[1]:
        AddScore(str(message.from_user.id))
        await message.reply(f"Верно! Это {answer[0]}")
    else:
        await message.reply(f"Неверно! Правильный ответ- {answer[0]}")

    number = Memory.SetCurrentGame(str(message.from_user.id))
    if number == 10:
        await bot.send_message(message.chat.id, f"Вы набрали {Memory.GetCurrentScore(str(message.from_user.id))}/10")
        Memory.SetCurrentGame(str(message.from_user.id), reset=True)
    else:
        await start_game(message)



@dp.message(Command('top'))
async def show_top(message: types.Message):
    top = GetTop()
    answer = 'Топ игроков: \n'
    for user in top:
        answer += f"{user[0]} - {user[1]} \n"
    await message.reply(answer)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
