import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Tokenni Render muhitidan xavfsiz yuklab olish
TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 O'YINNI BOSHLASH",
                web_app=WebAppInfo(url="https://orinovshohjahon62-sudo.github.io/MATH-DUELGame/")
            )
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = (
        "👋 <b>MATH DUEL 1VS1</b> ga xush kelibsiz!\n\n"
        "Matematik tezlik va mantiqingizni sinovdan o'tkazing.\n"
        "⚔️ Do'stlaringiz bilan 1v1 duel qiling va g'alaba qozoning!"
    )
    
    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=reply_markup
    )

def main():
    if not TOKEN:
        raise ValueError("XALOLIK: BOT_TOKEN yoki TOKEN topilmadi! Render sozlamalarini tekshiring.")
        
    # Bot dasturini qurish
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot ishga tushdi...")
    
    # Render (Linux) serverlarida asyncio event loop bugini oldini olish
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    loop.run_until_complete(app.run_polling(close_loop=False))

if __name__ == '__main__':
    main()

