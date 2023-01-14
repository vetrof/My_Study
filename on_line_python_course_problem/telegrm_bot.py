#telegram bot code
from aiogram import Bot, Dispatcher, executor, types

#bot init
bot = Bot(token='5531672769:AAH_HHanzMoXrb5DGdhtZ3peichEKrwNfTc')
dp = Dispatcher(bot)


#echo bot
@dp.message_handler()
async def echo(message: types.Message):
    #await message.answer(message.text)
    weather = 260
    await message.answer(weather)


#run long polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)