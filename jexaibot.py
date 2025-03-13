import telebot
import google.generativeai as genai

# 🔑 Google Gemini API Key & Telegram Bot Token
GEMINI_API_KEY = "AIzaSyBXgYujq-O8szIKho-K-mH0lelH8a2k6H8"
TELEGRAM_BOT_TOKEN = "7513076537:AAF3pamvPpoWBgWigu9gpM83fhw4276mw9o"

# 🚀 API Setup
genai.configure(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# 🎭 Custom Replies
CUSTOM_REPLIES = {
    "jex": "🔥 Jex यहाँ है! तेरे हर सवाल का जवाब देने के लिए! 😎",
    "who is your father": "👑 मेरा फादर **God Jexar** है!",
    "who made you": "🚀 मुझे **God Jexar** ने बनाया है!",
}

# 💬 Google Gemini AI Chat Function
@bot.message_handler(func=lambda message: True)
def chat_with_jex(message):
    user_text = message.text.lower()

    # ⚡ Custom Replies
    if user_text in CUSTOM_REPLIES:
        bot.reply_to(message, CUSTOM_REPLIES[user_text])
        return

    # 🤖 Gemini AI से जवाब लाना
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "😢 Error: " + str(e))

# 🚀 Bot को रन करो
bot.polling()