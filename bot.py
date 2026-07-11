import os
import asyncio
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Tokenni Render muhitidan xavfsiz yuklab olish
TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # To'g'rilangan aniq havola va keshni majburiy tozalash (?v=2)
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 O'YINNI BOSHLASH",
                web_app=WebAppInfo(url="https://orinovshohjahon62-sudo.github.io/MATH-DUELgame/?v=2")
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

# Render port so'ragani uchun soxta veb-server ochamiz (Render tinchlanishi uchun)
def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    handler = SimpleHTTPRequestHandler
    # Portni band qilamiz, shunda Render yashil (Live) bo'ladi
    with TCPServer(("0.0.0.0", port), handler) as httpd:
        httpd.serve_forever()

def main():
    if not TOKEN:
        raise ValueError("XALOLIK: BOT_TOKEN yoki TOKEN topilmadi! Render sozlamalarini tekshiring.")
    
    # Fondagi veb-serverni ishga tushirish
    server_thread = Thread(target=run_dummy_server, daemon=True)
    server_thread.start()
        
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
    
