import requests
import telebot,random
from telebot import types
token = "5090894737:AAF67GlxSQiTUQoe40VqtOpvpweKY9MexIc"
def check_user(user_id):
    global tokin
    request = requests.get(
        f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@SMOKA_28&user_id={user_id}"
    ).text
    if '"status":"left"' in request or '"Bad Request: USER_ID_INVALID"' in request or '"status":"kicked"' in request or 'user not found' in request:
        return False
    else:
        return True
while True:
	try:
		bot = telebot.TeleBot(token)
		@bot.message_handler(commands=['start'])
		def start(message):
			channel = types.InlineKeyboardButton(text="Channel Developer ",url="https://t.me/SMOKA_28")
			if check_user(message.from_user.id):
	
				start = types.InlineKeyboardButton(text="start",callback_data="start")
				programmer = types.InlineKeyboardButton(text="مراسلة المطور ",url="https://t.me/smoka28")
				Keyboards = types.InlineKeyboardMarkup()
				Keyboards.row_width = 1
				button = [start,programmer]
				Keyboards.add(button[0],button[1])
				bot.reply_to(message,text=f"🌹| مرحبًا بك {message.from_user.first_name}\n في بوت المسابقات الأول علي تليجرام🏅",reply_markup=Keyboards)
			else:
				Keyboard = types.InlineKeyboardMarkup()
				Keyboard.row_width = 1
				Keyboard.add(channel)
				bot.reply_to(message,text=f"🌹| Hi {message.from_user.first_name} \nYou must subscribe to the developer's channel Then press /start",reply_markup=Keyboard)
		@bot.callback_query_handler(func=lambda call: True)
		def bot_query_handler(call):
			if call.data == "start":
				run(call.message)
			elif call.data == "islam":
				islam_get(call.message)
			elif call.data == "art":
				art_get(call.message)
			elif call.data == "mas":
				mas_get(call.message)
			elif call.data == "a3":
				a3_get(call.message)
			elif call.data == "dol":
				dol_get(call.message)
			elif call.data == "story":
				story_get(call.message)
			elif call.data == "all":
				all_get(call.message)
			elif call.data == 'False':
				f(call.message)
			elif call.data == 'True':
				t(call.message)
		def run(message):
			
			islam = types.InlineKeyboardButton(text=" ✲ علم وتاريخ اسلامي ✲ ",callback_data="islam")
			art = types.InlineKeyboardButton(text=" ✲ اداب وفنون ✲ ",callback_data="art")
			mas = types.InlineKeyboardButton(text=" ✲ منافسات رياضيه ✲ ",callback_data="mas")
			a3 = types.InlineKeyboardButton(text=" ✲ علوم ولغات وثقافه ✲ ",callback_data="a3")
			dol = types.InlineKeyboardButton(text=" ✲ دول ومدن ومعالم ✲ ",callback_data="dol")
			story = types.InlineKeyboardButton(text=" ✲ تاريخ وحضاره ✲ ",callback_data="story")
			all = types.InlineKeyboardButton(text=" ✲ معلومات عامه متنوعه ✲ ",callback_data="all")
			smoka = types.InlineKeyboardMarkup()
			smoka.row_width = 1
			button = [islam,art,mas,a3,dol,story,all]
			smoka.add(button[0],button[1],button[2],button[3],button[4],button[5],button[6])
			bot.reply_to(message,text=f"من فضلك اختر أحد أقسام البوت 🆚",reply_markup=smoka)
		def islam_get(message):
			url="https://ell3ba.com/home/getQuestions/9/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
		def f(message):
			bot.send_message(message.chat.id, "إجابتك خاطئة , ✖️")
		def t(message):
			try:
				bot.delete_message(message.chat.id, message.message_id - 2)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 3)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 4)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id + 1)
			except:
				pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 2)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 3)
				except:
					pass
				
				try:
					bot.delete_message(message.chat.id, message.message_id - 1)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 0)
				except:
					pass
			url="https://ell3ba.com/home/getQuestions/9/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			bot.send_message(message.chat.id, "إجابتك صحيحه , ✔️")
			
			
			
		def art_get(message):
			url="https://ell3ba.com/home/getQuestions/7/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
		def f(message):
			bot.send_message(message.chat.id, "إجابتك خاطئة , ✖️")
		def t(message):
			
			try:
				bot.delete_message(message.chat.id, message.message_id - 2)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 3)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 4)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id + 1)
			except:
				pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 2)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 3)
				except:
					pass
				
				try:
					bot.delete_message(message.chat.id, message.message_id - 1)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 0)
				except:
					pass
			url="https://ell3ba.com/home/getQuestions/7/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			bot.send_message(message.chat.id, "إجابتك صحيحه , ✔️")
				
		def mas_get(message):
			url="https://ell3ba.com/home/getQuestions/8/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
		def f(message):
			bot.send_message(message.chat.id, "إجابتك خاطئة , ✖️")
		def t(message):
			
			try:
				bot.delete_message(message.chat.id, message.message_id - 2)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 3)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 4)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id + 1)
			except:
				pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 2)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 3)
				except:
					pass
				
				try:
					bot.delete_message(message.chat.id, message.message_id - 1)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 0)
				except:
					pass
			url="https://ell3ba.com/home/getQuestions/8/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			bot.send_message(message.chat.id, "إجابتك صحيحه , ✔️")
				
		def a3_get(message):
			url="https://ell3ba.com/home/getQuestions/2/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
		def f(message):
			bot.send_message(message.chat.id, "إجابتك خاطئة , ✖️")
		def t(message):
			
			try:
				bot.delete_message(message.chat.id, message.message_id - 2)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 3)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 4)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id + 1)
			except:
				pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 2)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 3)
				except:
					pass
				
				try:
					bot.delete_message(message.chat.id, message.message_id - 1)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 0)
				except:
					pass
			url="https://ell3ba.com/home/getQuestions/2/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			bot.send_message(message.chat.id, "إجابتك صحيحه , ✔️")
		def dol_get(message):
			url="https://ell3ba.com/home/getQuestions/10/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
		def f(message):
			bot.send_message(message.chat.id, "إجابتك خاطئة , ✖️")
		def t(message):
			
			try:
				bot.delete_message(message.chat.id, message.message_id - 2)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 3)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 4)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id + 1)
			except:
				pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 2)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 3)
				except:
					pass
				
				try:
					bot.delete_message(message.chat.id, message.message_id - 1)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 0)
				except:
					pass
			url="https://ell3ba.com/home/getQuestions/10/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			bot.send_message(message.chat.id, "إجابتك صحيحه , ✔️")
		def story_get(message):
			url="https://ell3ba.com/home/getQuestions/5/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
		def f(message):
			bot.send_message(message.chat.id, "إجابتك خاطئة , ✖️")
		def t(message):
			
			try:
				bot.delete_message(message.chat.id, message.message_id - 2)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 3)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 4)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id + 1)
			except:
				pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 2)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 3)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id - 1)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 0)
				except:
					pass
			url="https://ell3ba.com/home/getQuestions/5/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			bot.send_message(message.chat.id, "إجابتك صحيحه , ✔️")
		def all_get(message):
			url="https://ell3ba.com/home/getQuestions/1/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
		def f(message):
			bot.send_message(message.chat.id, "إجابتك خاطئة , ✖️")
		def t(message):
			
			try:
				bot.delete_message(message.chat.id, message.message_id - 2)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 3)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id - 4)
			except:
				pass
			try:
				bot.delete_message(message.chat.id, message.message_id + 1)
			except:
				pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 2)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 3)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id - 1)
				except:
					pass
				try:
					bot.delete_message(message.chat.id, message.message_id + 0)
				except:
					pass
			url="https://ell3ba.com/home/getQuestions/1/1"
			headers={
	    'Host':'ell3ba.com',
	    'Connection':'Keep-Alive',
	    'User-Agent':'android-async-http/1.4.1 (http://loopj.com/android-async-http)',
	    'Accept-Encoding':'gzip',
	    'Authorization':'c626c5bfebb41a166dcd681c1a600fb3'
	    }
			req=requests.get(url, headers=headers).json()
			q1 = req['data'][0]['question']
			g1 = req['data'][0]['answer_1']
			g2 = req['data'][0]['answer_2']
			g3 = req['data'][0]['answer_3']
			g4 = req['data'][0]['answer_4']
			an = req['data'][0]['correct_answer']
			if an == '1':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='True')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			elif an == '2':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='True')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)			
			
			elif an == '3':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='True')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='False')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)	
			elif an == '4':
				smak = types.InlineKeyboardMarkup()
				b1 = types.InlineKeyboardButton(text=f"{g1}", callback_data='False')
				b2 = types.InlineKeyboardButton(text=f"{g2}", callback_data='False')
				b3 = types.InlineKeyboardButton(text=f"{g3}", callback_data='False')
				b4 = types.InlineKeyboardButton(text=f"{g4}", callback_data='True')
				smak.row_width = 2
				button = [b1,b2,b3,b4]
				random.shuffle(button)
				smak.add(button[0],button[1],button[2],button[3])
				bot.reply_to(message,text=f"{q1}",reply_markup=smak)
			bot.send_message(message.chat.id, "إجابتك صحيحه , ✔️")
		try:
			bot.polling(True)
		except Exception as ex:
			print(ex)
			telebot.logger.error(ex)
	except:
		continue

