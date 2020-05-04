import telebot
import config
import requests
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

def crypto_price(name):
	rs = requests.get('https://alpari.com/ru/markets/crypto/' + name + '/')
	html = BS(rs.content, 'html.parser')
	title = html.select('.analytics-crypto-item__instrument-price-left')

	return title


def stat_24hour(name):
	rs = requests.get('https://alpari.com/ru/markets/crypto/' + name + '/')
	html = BS(rs.content, 'html.parser')
	title = html.select('.analytics-crypto-item__instrument-price-right')
	title = str(title)
	title = title.replace('[<div class="analytics-crypto-item__instrument-price-right">','')
	title = title.replace('</div><div>2.67%</div></div>]','')
	title = title.replace('<div>','')
	return title[0]


def last_news():
	URL = 'https://prometheus.ru/articles/'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content,'html.parser')
	items = soup.findAll('h2',class_= 'vcex-recent-news-entry-title-heading')
	comps = []

	for item in items:
		comps.append({
			'title' : item.find('a').text,
			'link'  : item.find('a').get('href')

			})
	check_list = {}

	for comp in comps :

		gg = comp['title']

	return comp['title']

def last_news_link():
	URL = 'https://prometheus.ru/articles/'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content,'html.parser')
	items = soup.findAll('h2',class_= 'vcex-recent-news-entry-title-heading')
	comps = []

	for item in items:
		comps.append({
			'title' : item.find('a').text,
			'link'  : item.find('a').get('href')

			})
	check_list = {}

	for comp in comps :

		gg = comp['title']

	return comp['link']

def all_links():
	URL = 'https://prometheus.ru/articles/'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content,'html.parser')
	items = soup.findAll('h2',class_= 'vcex-recent-news-entry-title-heading')
	comps = []

	for item in items:
		comps.append({
			'title' : item.find('a').text,
			'link'  : item.find('a').get('href')

			})
	check_list = []

	for comp in comps :
		return comp['link']





@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
	item1 = types.KeyboardButton('💵Курсы криптовалют')
	item2 = types.KeyboardButton('📊Статистика за 24 часа')
	item3 = types.KeyboardButton('📰Последняя новость криптовалют')
	item4 = types.KeyboardButton('💰ICO')
	item5 = types.KeyboardButton('🆕Для новичков')

	markup.add(item1,item2,item3,item4,item5)
	gg = 'Привет, <b>' + message.from_user.first_name.title() + '</b>!\n Я - PhloIT, но ты можешь называть меня лучшим телеграм ботом  в мире криптовалют😏\n\nНу что,начнём?!😃'.format(message.from_user, bot.get_me())
	bot.send_message(message.chat.id, gg ,parse_mode='html',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def crypto_price_telegram(message):
	if message.chat.type == 'private':
		if message.text == '💵Курсы криптовалют':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Bitcoin')
			item2 = types.KeyboardButton('Ethereum')
			item3 = types.KeyboardButton('XRP')
			item4 = types.KeyboardButton('Monero')
			item5 = types.KeyboardButton('Bitcoin Cash')
			item6 = types.KeyboardButton('Dash')
			item7 = types.KeyboardButton('Litecoin')
			item8 = types.KeyboardButton('EOS')
			item9 = types.KeyboardButton('Назад ◀️')
			markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9)

			bot.send_message(message.chat.id, 'Тыкай на любую крипту внизу и моментально узнавай её курс' ,parse_mode='html',reply_markup=markup)

		if message.text == 'Bitcoin':
			bot.send_message(message.chat.id, crypto_price('bitcoin'))
		elif message.text == 'Ethereum':
			bot.send_message(message.chat.id, crypto_price('ethereum'))
		elif message.text == 'XRP':
			bot.send_message(message.chat.id, crypto_price('xrp'))
		elif message.text == 'Monero':
			bot.send_message(message.chat.id, crypto_price('monero'))
		elif message.text == 'Bitcoin Cash':
			bot.send_message(message.chat.id, crypto_price('bitcoin_cash'))
		elif message.text == 'Dash':
			bot.send_message(message.chat.id, crypto_price('dash'))
		elif message.text == 'Litecoin':
			bot.send_message(message.chat.id, crypto_price('litecoin'))
		elif message.text == 'EOS':
			bot.send_message(message.chat.id, crypto_price('eos'))
		elif message.text == 'Назад ◀️':
			bot.send_message(message.chat.id, welcome(message))


		if message.text == '📊Статистика за 24 часа':

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Динамика Bitcoin')
			item2 = types.KeyboardButton('Динамика Ethereum')
			item3 = types.KeyboardButton('Динамика XRP')
			item4 = types.KeyboardButton('Динамика Monero')
			item5 = types.KeyboardButton('Динамика Bitcoin Cash')
			item6 = types.KeyboardButton('Динамика Dash')
			item7 = types.KeyboardButton('Динамика Litecoin')
			item8 = types.KeyboardButton('Динамика EOS')
			item9 = types.KeyboardButton('Назад ◀️')
			markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9)

			bot.send_message(message.chat.id, 'Тыкай на любую крипту внизу и моментально узнай динамику курса' ,parse_mode='html',reply_markup=markup)


		if message.text == 'Динамика Bitcoin':
			gg = stat_24hour('bitcoin')
			if gg == '-' :
				bot.send_message(message.chat.id, 'Биток подсел за последние 24 часа😭⬇️')
			else :
				bot.send_message(message.chat.id, 'Биток поднялся за последние 24 часа😃🆙')
		elif message.text == 'Динамика Ethereum':
			gg = stat_24hour('ethereum')
			if gg == '-' :
				bot.send_message(message.chat.id, 'Эфир подсел за последние 24 часа😭⬇️')
			else :
				bot.send_message(message.chat.id, 'Эфир поднялся за последние 24 часа😃🆙')
		elif message.text == 'Динамика XRP':
			gg = stat_24hour('xrp')
			if gg == '-' :
				bot.send_message(message.chat.id, 'XRP подсел за последние 24 часа😭⬇️')
			else :
				bot.send_message(message.chat.id, 'XRP поднялся за последние 24 часа😃🆙')
		elif message.text == 'Динамика Monero':
			gg = stat_24hour('monero')
			if gg == '-' :
				bot.send_message(message.chat.id, 'Monero подсел за последние 24 часа😭⬇️')
			else:
				bot.send_message(message.chat.id, 'Monero поднялся за последние 24 часа😃🆙')
		elif message.text == 'Динамика Bitcoin Cash':
			gg = stat_24hour('bitcoin_cash')
			if gg == '-' :
				bot.send_message(message.chat.id, 'Bitcoin Cash подсел за последние 24 часа😭⬇️')
			else:
				bot.send_message(message.chat.id, 'Bitcoin Cash поднялся за последние 24 часа😃🆙')
		elif message.text == 'Динамика Dash':
			gg = stat_24hour('dash')
			if gg == '-' :
				bot.send_message(message.chat.id, 'Dash подсел за последние 24 часа😭⬇️')
			else:
				bot.send_message(message.chat.id, 'Dash поднялся за последние 24 часа😃🆙')
		elif message.text == 'Динамика Litecoin':
			gg = stat_24hour('litecoin')
			if gg == '-' :
				bot.send_message(message.chat.id, 'Litecoin подсел за последние 24 часа😭⬇️')
			else:
				bot.send_message(message.chat.id, 'Litecoin поднялся за последние 24 часа😃🆙')
		elif message.text == 'Динамика EOS':
			gg = stat_24hour('eos')
			if gg == '-' :
				bot.send_message(message.chat.id, 'EOS подсел за последние 24 часа😭⬇️')
			else:
				bot.send_message(message.chat.id, 'EOS поднялся за последние 24 часа😃🆙')
		elif message.text == 'Назад ◀️':
			bot.send_message(message.chat.id, welcome(message))


		if message.text == '📰Последняя новость криптовалют':
			bot.send_message(message.chat.id, last_news() + '\nСсылка : ' + last_news_link(),parse_mode='html')

		if message.text == '💰ICO':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Текущие ICO')
			item2 = types.KeyboardButton('Будущие ICO')
			item3 = types.KeyboardButton('Завершенные ICO')
			item4 = types.KeyboardButton('Назад ◀️')
			markup.add(item1,item2,item3,item4)

			sti = open('stickers/1.webp', 'rb')
			bot.send_sticker(message.chat.id, sti,reply_markup=markup)

		if message.text == 'Текущие ICO':
			bot.send_message(message.chat.id, '1)Original Protocol\n$38,100,000\nhttps://prometheus.ru/ico/origin-protocol/\n\n2)Emotiq\n11,800,000 USD/$39,000,000\nhttps://prometheus.ru/ico/emotiq-blockchain/\n\n3)Ankr Network\n15,950,000 USD/$18,700,000\nhttps://prometheus.ru/ico/ankr-network-cloud-computing/\n\n4)DREP\n$15,180,000/$19,800,000\nhttps://prometheus.ru/ico/drep/\n\n5)Quadrant Protocol\n15,000,000 USD/20,000,000 USD\nhttps://prometheus.ru/ico/quadrant-protocol/',parse_mode='html')

		if message.text == 'Будущие ICO':
			bot.send_message(message.chat.id,'1)Orchid Protocol\n$40,800,000\nhttps://prometheus.ru/ico/orchid-protocol/\n\n2)Keep network\nhttps://prometheus.ru/ico/keep-network/\n\n3)NuCypher\n$5,150,000\nhttps://prometheus.ru/ico/nucypher/\n\n4)Mattereum\nhttps://prometheus.ru/ico/mattereum/\n\n5)Lambda\n$15,000,000/$20,000,000\nhttps://prometheus.ru/ico/lambda/',parse_mode='html')

		if message.text == 'Завершенные ICO':
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("BABB", callback_data='babb')
			item2 = types.InlineKeyboardButton("TE-FOOD", callback_data='te_food')
			item3 = types.InlineKeyboardButton("Electrify.Asia", callback_data='asia')
			item4  = types.InlineKeyboardButton("Debitum Network", callback_data='networks')
			item5 = types.InlineKeyboardButton("Banca",callback_data='banca')
			item6 = types.InlineKeyboardButton("NaPoleonX",callback_data='napoleon')

			markup.add(item1,item2,item3,item4,item5,item6)

			bot.send_message(message.chat.id, 'Поехали👇', reply_markup=markup)

		if message.text == '🆕Для новичков':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
			item1 = types.KeyboardButton('Что такое блокчейн?')
			item2 = types.KeyboardButton('Что такое ICO?')
			item3 = types.KeyboardButton('Что такое трейдинг криптовалютой?')
			item4 = types.KeyboardButton('Где хранить биткоин и другие криптовалюты? В кошельке')
			item5 = types.KeyboardButton('Что такое биткоин?')
			item6 = types.KeyboardButton('Далее')
			markup.add(item1,item2,item3,item4,item5,item6)

			bot.send_message(message.chat.id,'Тут столько инфы....😮\nЕсли ты всё это прочитаешь - точно станешь про!😉',parse_mode='html',reply_markup=markup)

		if message.text =='Далее':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
			item1 = types.KeyboardButton('Что такое смарт-контракты?')
			item2 = types.KeyboardButton('Что такое криптоанархизм?')
			item3 = types.KeyboardButton('Не попаду ли я в тюрьму за биткоины?')
			item4 = types.KeyboardButton('Что такое майнинг криптовалют?')
			item5 = types.KeyboardButton('Как майнить криптовалюту')
			item6 = types.KeyboardButton('Что такое Эфириум?')
			item7 = types.KeyboardButton('Назад ◀️')

			markup.add(item1,item2,item3,item4,item5,item6,item7)

			bot.send_message(message.chat.id,'Страница 2️⃣,а количество инфы только увеличивается..',parse_mode='html',reply_markup=markup)

		if message.text == 'Что такое блокчейн?':
			bot.send_message(message.chat.id, 'Интересно, что такое блокчейн🧐\nДавай узнаем!\nТыкай - https://telegra.ph/CHto-takoe-blokchejn-05-04',parse_mode='html')
		if message.text == 'Что такое ICO?':
			bot.send_message(message.chat.id, 'ICO - великая вещь,помогающая тысячи проектам ежедневно\nДавайте же поглубже изучим данную тему\n Тыкай - https://telegra.ph/CHto-takoe-ICO-05-04',parse_mode='html')
		if message.text == 'Что такое трейдинг криптовалютой?':
			bot.send_message(message.chat.id, 'Трейдинг - очередное МММ или же что то более значимое?\nДавайте же узнаем\nТыкай -https://telegra.ph/CHto-takoe-trejding-kriptovalyutoj-05-04',parse_mode='html')
		if message.text == 'Где хранить биткоин и другие криптовалюты? В кошельке':
			bot.send_message(message.chat.id,'Конечно же в кошельке,кстати пойду хлеба куплю за пятак биткоина...Шутка\nДавайте узнаем тру инфу!\nТыкай - https://telegra.ph/Gde-hranit-bitkoin-i-drugie-kriptovalyuty-V-koshelke-05-04',parse_mode='html')
		if message.text == 'Что такое биткоин?':
			bot.send_message(message.chat.id,'Деньги из банка приколов - или всё таки нет\nДавайте же узнаем!\nТыкай - https://telegra.ph/CHto-takoe-bitkoin-05-04',parse_mode='html')
		if message.text == 'Что такое смарт-контракты?':
			bot.send_message(message.chat.id,'А я хотел контракт с Microsoft...\nТыкай - https://telegra.ph/CHto-takoe-smart-kontrakty-05-04',parse_mode='html')
		if message.text == 'Что такое криптоанархизм?':
			bot.send_message(message.chat.id,'Мать анархия да?)\n Тыкай - https://telegra.ph/CHto-takoe-kriptoanarhizm-05-04',parse_mode='html')
		if message.text == 'Не попаду ли я в тюрьму за биткоины?':
			bot.send_message(message.chat.id,'я не придумал шутки про тюрьму и биткоины xD\nВсе равно тыкай - https://telegra.ph/Ne-popadu-li-ya-v-tyurmu-za-bitkoiny-05-04',parse_mode='html')
		if message.text == 'Что такое майнинг криптовалют?':
			bot.send_message(message.chat.id,'эм,что,майнкрафт?)\nпрости я больше не буду,Тыкай - https://telegra.ph/CHto-takoe-majning-kriptovalyut-05-04',parse_mode='html')
		if message.text == 'Как майнить криптовалюту':
			bot.send_message(message.chat.id, 'Да вроде легко 10 штук 1080GTX и поехали!🤠\nНо всё не так просто,так что ТЫКАЙ - https://telegra.ph/Kak-majnit-kriptovalyutu-05-04',parse_mode='html')
		if message.text == 'Что такое Эфириум?':
			bot.send_message(message.chat.id, 'РУССКАЯ КРИПТОВАЛЮТА!!!\nТыкай,будь патритотом🇷🇺 - https://telegra.ph/CHto-takoe-EHfirium-05-04',parse_mode='html')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
        	if call.data == 'babb':
        		bot.send_message(call.message.chat.id, 'Название : BABB 👀\n\nЦель сборов : $20,000,000 USD💶\n\nТип токена: ERC20🤖\n\nЦена токена: 1 BAX = 0.0012 USD💰')
        	elif call.data == 'te_food':
        		bot.send_message(call.message.chat.id, 'Название : TE-FOOD 👀\n\nЦель сборов : $19,000,000 USD💶\n\nТип токена: ERC20🤖\n\nЦена токена: 1 TFD = 0.0391 USD💰')
        	elif call.data == 'asia':
        		bot.send_message(call.message.chat.id, 'Название : Electrify.Asia 👀\n\nЦель сборов : $30,000,000 USD💶\n\nТип токена: ERC20🤖\n\nЦена токена: 1 ELEC = 0.0800 USD💰')
        	elif call.data == 'networks':
        		bot.send_message(call.message.chat.id, 'Название : Debitum Network 👀\n\nЦель сборов : $17,200,000 USD💶\n\nТип токена: ERC223🤖\n\nЦена токена: 1 DEB = 0.13 USD💰')
        	elif call.data == 'banca':
        		bot.send_message(call.message.chat.id, 'Название : Banca 👀\n\nЦель сборов : $20,000,000 USD💶\n\nТип токена: ERC20🤖\n\nЦена токена: 1 BANCA = 0.0020 USD💰')
        	elif call.data == 'napoleon':
        		bot.send_message(call.message.chat.id, 'Название : NaPoleonX 👀\n\nЦель сборов : 18,300,000 USD💶\n\nТип токена: ERC20🤖\n\nЦена токена: 1 NPX = 0.87 USD💰')

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
