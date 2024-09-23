import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, MessageHandler, filters
from config import BOT_TOKEN, EMAIL_USER, EMAIL_PASSWORD, EMAIL_RECEIVER
import queue

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Send me a message and i will send it to the email')

async def handle_message(update: Update, context: CallbackContext) -> None:  
    user_message = update.message.text
    try:
        send_email(user_message)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Your message has been sent!')  
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Error sending message: {}'.format(e)) 

def send_email(message: str) -> None:
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = ' New message'
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()