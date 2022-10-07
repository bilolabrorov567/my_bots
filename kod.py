from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from bot import well

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello, \n Select your currency:")

async def currency (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    exchange =  update.message.text
    valyuta = well(exchange)
    await update.message.reply_text(valyuta)


app = ApplicationBuilder().token("5518667387:AAGihO3h4BFC86vS52VE0FteOdYU0VDn4Fs").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,currency))

app.run_polling()




