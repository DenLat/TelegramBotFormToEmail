import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import BOT_TOKEN, EMAIL_USER, EMAIL_PASSWORD, EMAIL_RECEIVER

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Пожалуйста, отправьте вашу заявку.')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    send_email(user_message)
    update.message.reply_text('Ваша заявка отправлена!')

def send_email(message: str) -> None:
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = 'Новая заявка'
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()