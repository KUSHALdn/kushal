import telebot

# Aapka Original Token
API_TOKEN = '8650620955:AAGbeAnHtxhYqaGwG9XZaEhkTP7nMLds1cA'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "✅ Kushal Bhai, Bot Ekdum Sahi Chal Raha Hai!")

print("--- TESTING MODE ---")
print("Telegram bot par jaao aur /start likho...")
bot.polling()

