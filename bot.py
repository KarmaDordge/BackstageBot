from pickle import TRUE
import telebot

token=""

startString = """Немного о BACKSTAGE:

Чем Вы можете заняться в нашем антикафе… 
Да чем пожелаете! А мы лишь предложим пару вариантов:

	
\U00002734 Поиграть в настольные игры
\U00002734 Посидеть в интернете - WiFi у нас бесплатный!
\U00002734 Познакомиться с новыми интересными людьми
\U00002734 Почитать комиксы
\U00002734 Поиграть в приставку
\U00002734 Обсудить выставку за чашечкой халявного чая:)
"""
adress = "пр. Ленина, 22/2, Магадан, Магаданская обл., 685000 \n 89248515115"

contact = """
Если Вы хотите провести мероприятие (лекция, мастер-класс, семинар и т.д.), 
оставить отзыв или пожелание или в случае спорной ситуации, 
Вы можете написать в Инстаграм, 
ВК или телеграм или позвонить 
по номеру+7 924 851 51 15. Вам ответят!

https://instagram.com/backstage.mgdn

https://vk.com/backstage.mgdn

https://t.me/backstage_mgdn
"""
price = """
Вход 200 рублей (в эту сумму входит первый час пребывания в антикафе). Со второго часа 1,5 рубля в минуту (90 рублей в час).

Вы можете сразу заплатить фиксированную сумму и находиться в антикафе до закрытия. По будням 500 рублей, по выходным 600 рублей.
"""

rule = """Администрация может отказать в посещении без объяснения причин.
Мы будем вынуждены отказать Вам в посещении, если:
Вы находитесь в состоянии алкогольного опьянения. От Вас пахнет алкоголем, Вас пошатывает, Вы неадекватны. И да, даже если чуть-чуть.
Вы ведете себя недружелюбно/неадекватно или вели в прошлые посещения (на усмотрение администратора).
Вы нарушаете общественный порядок (на усмотрение администратора).
Вы совершаете противоправные действия (!).
"""
badbehavior = """Заниматься несанкционированной торговлей (даже если чуть-чуть).
Приносить и распивать алкоголь (в том числе приносить в себе).
Нарушать УК и АК РФ.
Уносить с собой игры, комиксы или книги. 
Лежать на гамаке или диване в обуви.
Пить чай, кофе, употреблять еду на игровых столах (для этого есть специальные столики).
Играть в азартные игры, играть в покер (он тоже считается азартной игрой).
Курить всё, что курится (обычные сигареты, электронные сигареты, вейпы, кальяны и т.д.) в непредназначенных для этого местах (в помещениях, снаружи вблизи входов и окон).
Ругаться матом, говорить матом и петь матом тоже не стоит (во всяком случае так, чтобы слышали другие).
Находиться в местах, предназначенных только для персонала (стойка администратора, например).
Проводить политические, религиозные, ЗОЖ и т.д. агитации, которые могут задеть чувства администратора.
Оспаривать решения администратора (даже если он бука!).
Посещение уборных двумя или более людьми (ваше посещение уборной группой от двух более человек будет расценено как митинг и будет разогнано).
"""

sanction = """Потеря и/или поломка Вашей пластиковой карты. Штраф - 200 рублей (задний карман джинс они не любят!).
Находиться на территории антикафе более 10 минут не записанным. Штраф от 200 до 1000 рублей.
"""

bot = telebot.TeleBot(token)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('О нас \U0001F3EC', 'Контакты \U00002712')
keyboard1.row('Стоимость \U0001F4B2', 'Правила \U0001F514')
keyboard1.row('Настолки \U0001F0CF')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Запрещено', 'Штрафы')
keyboard2.row('Основное меню')
@bot.message_handler(commands=["start"])
def start(message):
    
    bot.send_message(message.chat.id, startString, reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'о нас \U0001F3EC':
        markup = telebot.types.InlineKeyboardMarkup()
        yamap= telebot.types.InlineKeyboardButton(text='Яндекс-карта', url='https://yandex.ru/profile/169470164093')
        gglmap= telebot.types.InlineKeyboardButton(text='Google карты', url='https://goo.gl/maps/KrHHyzAmJCkypgp2A')
        markup.add(yamap, gglmap)
        bot.send_message(message.chat.id, adress, reply_markup=markup)
    elif message.text.lower() == 'контакты \U00002712':
        bot.send_message(message.chat.id, contact, reply_markup=keyboard1)
    elif message.text.lower() == 'стоимость \U0001F4B2':
        bot.send_message(message.chat.id, price, reply_markup=keyboard1)
    elif message.text.lower() == 'правила \U0001F514':
        bot.send_message(message.chat.id, rule, reply_markup=keyboard2)
    elif message.text.lower() == 'запрещено':
        bot.send_message(message.chat.id, badbehavior, reply_markup=keyboard2)
    elif message.text.lower() == 'штрафы':
        bot.send_message(message.chat.id, sanction, reply_markup=keyboard2)
    elif message.text.lower() == 'основное меню':
        bot.send_message(message.chat.id, startString, reply_markup=keyboard1)




bot.infinity_polling()