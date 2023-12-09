from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def senc_echo(message:Message):
    await message.answer(f'"Извините, но я не понимаю команду {message.text}. Пожалуйста, попробуйте еще раз или воспользуйтесь командой /help для получения дополнительной информации о доступных командах' )