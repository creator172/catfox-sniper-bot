import telebot

# 🔑 Bot Token डालें
BOT_TOKEN = "8037032739:AAFr5ItAgx-v6BOqxUh5v2vSqyYM_Ua9xp4"

bot = telebot.TeleBot(BOT_TOKEN)

# 🟢 Start Command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I am Catfox 🦊 — your stock market sniper assistant. Type /sniperupdate to get today's insight.")

# 🔫 Sniperupdate Command
@bot.message_handler(commands=['sniperupdate'])
def sniperupdate(message):
    bot.reply_to(message, "📌 Monday Sniper Shot:\n\n📈 *Stock:* HDFCBANK\n🎯 Entry: ₹1500\n🚀 Target: ₹1525\n🛑 Stoploss: ₹1488\n\nStrategy: Bullish RSI + Volume Breakout")

# 🔁 Infinite Loop for polling
bot.polling()
