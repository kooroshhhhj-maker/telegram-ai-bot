import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8506814649:AAFY14S6SsIG7KC2Zr4zeYHCecsTeSygTUc"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! من بات هوش مصنوعی شما هستم 🤖"
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # فعلاً پاسخ آزمایشی
    response = f"پیام شما دریافت شد: {user_message}"

    await update.message.reply_text(response)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
