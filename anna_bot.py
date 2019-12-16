import telebot, json, urllib, flask, anna_bot_lib

bot = telebot.TeleBot(anna_bot_lib.mytoken, threaded = True)
adress = "http://api.openweathermap.org/data/2.5/weather?"
bot.remove_webhook()
bot.set_webhook(anna_bot_lib.server+anna_bot_lib.apitoken)
server = Flask(__name__) #конструктор классов

@bot.message_handler(commands=['start'])
def greeting (message):
    bot.send_message(message.from_user.id,"Hallo, schreib mir die Stadt auf Englisch")

@bot.message_handler()
def check (message):
    if isinstance(str(message.text),str):

        #http://api.openweathermap.org/data/2.5/weather?appid=0f259e3a3072fddd06df9002fa039340&q=Khabarovsk

        request = adress+"appid="+anna_bot_lib.api+"&q="+str(message.text)+"&units=metric"
        data1 = urllib.urlopen(request)
        data2 = data1.read().decode()

        try:
            data3 = json.loads(data2)
            bot.send_message(message.from_user.id, data3["main"]["temp"])
        except:
            bot.send_message(message.from_user.id, "Keine Stadt gefunden")
    else:
        bot.send_message(message.from_user.id, "Versuchen Sie noch mal")

def askforhumidity(message):
    bot.send_message(message.from_user.id,"Möchten Sie noch die Feuchtigkeit wissen?")

    if message.text.lowercase == "ja" :
        bot.send_message(message.from_user.id, data3["main"]["humidity"])
    else:
        bot.send_message(message.from_user.id, "Ok :)")
