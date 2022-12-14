from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler
)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from bot_python import get_rates


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("ðºð¸ USD/UZS", callback_data="USD"),
            InlineKeyboardButton("ð¹ð· TRY/UZS", callback_data="TRY"),
        ],
        [
            InlineKeyboardButton("ð´ó §ó ¢ó ¥ó ®ó §ó ¿EUR/UZS", callback_data="EUR"),
            InlineKeyboardButton("ð°ð¿ KZT/UZS", callback_data="KZT"),
        ],
         [
            InlineKeyboardButton("ð·ðº RUB/UZS", callback_data="RUB"),
        ],
       
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Hello,{update.message.from_user.first_name} \nSelect your currency :",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.message.delete()
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("ðºð¸ USD/UZS", callback_data="USD"),
            InlineKeyboardButton("ð¹ð· TRY/UZS", callback_data="TRY"),
        ],
        [
            InlineKeyboardButton("ð´ó §ó ¢ó ¥ó ®ó §ó ¿EUR/UZS", callback_data="EUR"),
            InlineKeyboardButton("ð°ð¿ KZT/UZS", callback_data="KZT"),
        ],
         [
            InlineKeyboardButton("ð·ðº RUB/UZS", callback_data="RUB"),
        ],
       
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    rate = get_rates()[query.data]["Rate"]
    await query.message.reply_text(text=f"1 {query.data} is {rate} UZS", reply_markup=reply_markup)


app = (
    ApplicationBuilder().token("5561854394:AAFLPi2MFoxQaaIXdoLXf3yjvXveHsS_SFU").build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()  # bot telegram for usd dolr kursi
