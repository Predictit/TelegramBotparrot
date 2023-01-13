import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['start'])
def welcome(message):
    sti = open(r'C:\Users\Turushkin\AppData\Roaming\Telegram Desktop\photo.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)