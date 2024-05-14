from langdetect import detect
from googletrans import Translator
from twitchio.ext import commands
bot_name='botpaco0'


#print(result.text)

class Bot(commands.Bot):

    def __init__(self):
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        super().__init__(token='oauth:whf8d58dzikmj67j407ukoz05706p1', 
                         prefix='!', 
                         initial_channels=['Anni0203'])#''
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def event_ready(self):
        print("Traduccion iniciada")
        #print(f'Logged in as | {self.nick}')
        #print(f'User id is | {self.user_id}')

    async def event_message(self, message):
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Idiomadetectado = detect(message.content)
        if( message.author.is_broadcaster):
                if(Idiomadetectado != 'es'):
                    translator = Translator()
                    Traduccion = translator.translate(message.content, src='es', dest='en')
                    await message.channel.send(Traduccion.text + ' (es + > en).' )
        else:
            if(Idiomadetectado == 'en'):
                translator = Translator()
                Traduccion = translator.translate(message.content, "en", dest='es')
                await message.channel.send(Traduccion.text + ' ('+Idiomadetectado +' > es)')
        
            

                

         
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot = Bot()

bot.run()
