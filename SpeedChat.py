from twitchio.ext import commands
#from playsound import playsound
import pyttsx3
import os
from dotenv import load_dotenv
load_dotenv()
#from gtts import gTTS
#from os import remove
bot_name='botpaco0'
engine = pyttsx3.init()
engine.setProperty("rate", 150)
with open('parametros/blacklis.txt', 'r') as file:
            listaNegra = [line.strip() for line 
                    in file]
class Bot(commands.Bot):

    def __init__(self):
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        super().__init__(token= os.environ['TWITCH_TOKEN'], 
                         prefix=os.environ['BOT_PREFIX'],
                         initial_channels=[os.environ['CHANNEL']])
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def event_ready(self):
        print("SpeedChat iniciado")
        #print(f'Logged in as | {self.nick}')
        #print(f'User id is | {self.user_id}')

    async def event_message(self, message):
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        
        #chatVoz = gTTS(message.author.name + ": " + message.content, lang= "es", tld= "es")
        if not message.author.name in listaNegra and not "!" == message.content[0:1].lower():
            #print(message.author.name , ": " , message.content)
            engine.say(message.author.name + ": " + message.content)
            #chatVoz.save("sonidos/audio.mp3")
            #playsound("sonidos/audio.mp3")
            #remove("sonidos/audio.mp3")
            engine.runAndWait()
         
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot = Bot()

bot.run()