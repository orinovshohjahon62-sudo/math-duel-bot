from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 O'YINNI BOSHLASH",
                web_app=WebAppInfo(
                    url="https://orinovshohjahon62-sudo.github.io/MATH-DUELgame/"
                )
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "👋 <b>MATH DUEL 1VS1</b> ga xush kelibsiz!\n\n"
        "🧠 Matematik tezlik va mantiqingizni sinovdan o'tkazing.\n"
        "⚔️ Do'stlaringiz bilan 1v1 duel qiling va g'alaba qozoning!"
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()
