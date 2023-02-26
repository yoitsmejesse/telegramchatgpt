import telegram
from telegram.ext import Updater, MessageHandler, Filters
from transformers import pipeline

# Replace YOUR_TELEGRAM_BOT_TOKEN with your Telegram bot token
bot = telegram.Bot(token='5177333982:AAEFxbaqC9AsSOnQ95UXsLxfm8j_hHFOjec')


# Replace "microsoft/DialoGPT-medium" with the name of the GPT model you want to use
generator = pipeline('text-generation', model='microsoft/DialoGPT-medium')

# Define a function to handle incoming messages
def respond(update, context):
    # Get the incoming message
    message = update.message.text

    # Generate a response using ChatGPT
    response = generator(message)[0]['generated_text']

    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    # Set up the message handler
dispatcher.add_handler(MessageHandler(Filters.text, respond))

# Start the bot
updater.start_polling()
