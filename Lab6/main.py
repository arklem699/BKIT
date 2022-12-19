import telebot
from telebot import types

bot = telebot.TeleBot('5832505900:AAGB16BePAysN85w95Pwmu8bOtbZ-bJz1zE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    mess = types.KeyboardButton('Смотреть')
    markup.add(mess)
    bot.send_message(message.chat.id, "Привет, я покажу тебе все финалы ЧМ по футболу", reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text == "Смотреть":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        mess1 = types.KeyboardButton('20')
        mess2 = types.KeyboardButton('21')
        mess3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(mess1, mess2, mess3)
        bot.send_message(message.chat.id, 'ЧМ какого века тебе нужен?', reply_markup=markup)

    elif message.text == "20":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mess1 = types.KeyboardButton('1930')
        mess2 = types.KeyboardButton('1934')
        mess3 = types.KeyboardButton('1938')
        mess4 = types.KeyboardButton('1950')
        mess5 = types.KeyboardButton('1954')
        mess6 = types.KeyboardButton('1958')
        mess7 = types.KeyboardButton('1962')
        mess8 = types.KeyboardButton('1966')
        mess9 = types.KeyboardButton('1970')
        mess10 = types.KeyboardButton('1974')
        mess11 = types.KeyboardButton('1978')
        mess12 = types.KeyboardButton('1982')
        mess13 = types.KeyboardButton('1986')
        mess14 = types.KeyboardButton('1990')
        mess15 = types.KeyboardButton('1994')
        mess16 = types.KeyboardButton('1998')
        mess17 = types.KeyboardButton('Вернуться в главное меню')
        markup.row(mess1, mess2, mess3, mess4)
        markup.row(mess5, mess6, mess7, mess8)
        markup.row(mess9, mess10, mess11, mess12)
        markup.row(mess13, mess14, mess15, mess16)
        markup.row(mess17)
        bot.send_message(message.chat.id, 'ЧМ какого года тебе нужен?', reply_markup=markup)

    elif message.text == "21":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mess1 = types.KeyboardButton('2002')
        mess2 = types.KeyboardButton('2006')
        mess3 = types.KeyboardButton('2010')
        mess4 = types.KeyboardButton('2014')
        mess5 = types.KeyboardButton('2018')
        mess6 = types.KeyboardButton('Вернуться в главное меню')
        markup.row(mess1, mess2, mess3)
        markup.row(mess4, mess5)
        markup.row(mess6)
        bot.send_message(message.chat.id, 'ЧМ какого года тебе нужен?', reply_markup=markup)

    elif message.text == "1930":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1930", url="https://soccer365.ru/games/10845550"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1934":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1934", url="https://soccer365.ru/games/10845531"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1938":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1938", url="https://soccer365.ru/games/10845514"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1950":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1950", url="https://soccer365.ru/competitions/742/1950"))
        bot.send_message(message.chat.id, "Финал проходил по системе группового этапа!")
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1954":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1954", url="https://soccer365.ru/games/10845474"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1958":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1958", url="https://soccer365.ru/games/10845448"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1962":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1962", url="https://soccer365.ru/games/10845414"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1966":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1966", url="https://soccer365.ru/games/10845382"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1970":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1970", url="https://soccer365.ru/games/10845350"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1974":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1974", url="https://soccer365.ru/games/10845318"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1978":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1978", url="https://soccer365.ru/games/10845279"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1982":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1982", url="https://soccer365.ru/games/10845242"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1986":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1986", url="https://soccer365.ru/games/10845190"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1990":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1990", url="https://soccer365.ru/games/10372753/"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1994":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1994", url="https://soccer365.ru/games/10021473"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "1998":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-1998", url="https://soccer365.ru/games/10212268"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "2002":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-2002", url="https://soccer365.ru/games/10348108"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "2006":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-2006", url="https://soccer365.ru/games/10740395"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "2010":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-2010", url="https://soccer365.ru/games/10740153"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "2014":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-2014", url="https://soccer365.ru/games/10854563"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "2018":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Финал ЧМ-2018", url="https://soccer365.ru/games/12522466"))
        bot.send_message(message.chat.id, "Перейдите по ссылке", reply_markup=markup)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Смотреть'))
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, нажми на кнопку")


bot.polling(none_stop=True)