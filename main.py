from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import admin, callback, extra, client, fsmAdminMentor
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

extra.register_handlers_extra(dp)
fsmAdminMentor.register_handlers_fsm(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)