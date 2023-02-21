from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5721393251:AAEhsT674GPSmLiEGr76klhmKpl8t1fwZeI").build()
print('server start')
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
# app.add_handler(CommandHandler("reserve", reserve_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("time", time_command))

app.run_polling()