from telebot import TeleBot

bot = TeleBot("7798588788:AAGKhUhgD93LndpeDpqOBKAD_mlad_vu-eU")

@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id, 'Привет я бот магазина **OneOneOneAbsolut**')
    bot.send_message(message.chat.id, 'По-твоему мнению какой _никнейм_ мне подойдет?')

@bot.message_handler(commands=['weather'])
def weather1(message):
    bot.send_message(message.chat.id, 'Нет плохой погоды, погода всегда хорошая, если правильно одеться.')

@bot.message_handler(commands=['joke'])
def joke1(message):
    bot.send_message(message.chat.id, 'Жизнь становится проще, когда понимаешь, что проще она никогда не станет.')

@bot.message_handler(commands=['wishes'])
def wishes1(message):
    bot.send_message(message.chat.id, 'Пусть добрые люди постоянно встречаются на твоем пути, делая тебя счастливым.')


@bot.message_handler(content_types=['text'])
def handle_message(message):
    textmas=message.text
    if len(textmas) >= 20:
        bot.send_message(message.chat.id, 'Такой не хочу!!! Он слишком длинный!!!')
    elif textmas[0] in ('1234567890'):
        bot.send_message(message.chat.id, 'Такой не хочу!!! Он начинается с цифры!!!')
    elif not(textmas.endswith("bot")):
        bot.send_message(message.chat.id, 'Такой не хочу!!! Он не дает знать окружающим,что я бот!!!')
    else:
        bot.send_message(message.chat.id, 'Ник одобрен!')
bot.infinity_polling()