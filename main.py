import constants as keys
from telegram.ext import *
import responses as r

print("Bot started..")


def start_command(update,context):
    update.message.reply_text('Type something to get started! The commands are /start /contact /help.')


def help_command(update,context):
    update.message.reply_text('If you need help! You should ask for it on google..')


def contact_command(update,context):
    update.message.reply_text('You can contact Ayush Siloiya on Instagram! username=iam_ayush_s . Thank you.')


def handle_message(update,context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("contact", contact_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
