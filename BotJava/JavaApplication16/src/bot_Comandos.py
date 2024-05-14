from twitchio.ext import commands
from twitchio.ext import routines
import pyaudio
import wave
import random
import os
import pyttsx3
from dotenv import load_dotenv
load_dotenv()
with open('parametros/Bola8.txt', 'r') as file:
            boll8 = [line.strip() for line 
                    in file]
engine = pyttsx3.init()
engine.setProperty("rate", 150)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot_name='botpaco0'
track = ""
cont = 0


import requests

def cambiar_categoria_twitch(id_canal, id_categoria, oauth_token):
    url = f"https://api.twitch.tv/helix/channels?broadcaster_id={id_canal}"
    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Client-Id": "<tu-client-id>",
        "Content-Type": "application/json"
    }
    data = {
        "game_id": id_categoria
    }
    response = requests.patch(url, headers=headers, json=data)
    return response.json()

# Ejemplo de uso
# cambiar_categoria_twitch("<id-del-canal>", "<id-de-la-categoria>", "<tu-token-de-oauth>")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Bot(commands.Bot):
    

    def __init__(self):
        super().__init__(token= os.environ['TWITCH_TOKEN'], prefix=os.environ['BOT_PREFIX'],initial_channels=[os.environ['CHANNEL']])
        

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def event_ready(self):
        
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def player_done(self):
        print('Finished playing song!')

    async def event_message(self, message):
        print(message.author.name , ": " , message.content)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if "custom-reward-id=" in message.raw_data: 
            if "custom-reward-id=5e76d158-a1c2-4bcb-a197-b6f2c0595d6d" in message.raw_data:
                
                await message.channel.send("en seguida Vamos con" + message.content)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        if message.echo:
            return
        if  "hola" in message.content.lower()  or  "buenas" in message.content.lower()  or  "hello" in message.content.lower():
            await self.reproducir_sonido('sonidos/buenas.wav')
        if  "gg" in message.content.lower():
                await self.reproducir_sonido('sonidos/gg.wav')
        #if "pt" in message.content.lower() or "gil" in message.content.lower():
            
           #await self.reproducir_sonido('sonidos/ptm.wav')
        if "sensual" in message.content.lower() or "sexi" in message.content.lower() :
            await self.reproducir_sonido('sonidos/sensual.mp3')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        await self.handle_commands(message)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def test(self, ctx: commands.Context):
        #  mensage = "/clear"
        #  print(mensage)
        #  await ctx.send(mensage)
        #print(ctx.author.raw_data)
        respuesta = cambiar_categoria_twitch("521644868", "minecraft", "whf8d58dzikmj67j407ukoz05706p1")
        print(respuesta)
    @commands.command()
    async def apoyo(self, ctx: commands.Context):
        await ctx.send(f'Podes ayudarme mediante este link: https://linktr.ee/mosteryn')
    @commands.command()
    async def comandos(self, ctx: commands.Context):
          await ctx.send("Comandos: uptime, bola8, facha, subs, viewers, followage, followers, memide, amor, love, ruleta, duelo, coscorron, ds, buenas, corre, susto, tocktock, M")
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def susto(self, ctx: commands.Context):
            r = random.randint(1,2)
            await self.reproducir_sonido('sonidos/susto'+ str(r) +'.wav')
    @commands.command()
    async def p(self, ctx: commands.Context):
            await ctx.send("/mod bigniumCH")
    @commands.command()
    async def coscorron(self, ctx: commands.Context,search: str):
            await ctx.send(f"{ctx.author.name} Mando a mimir a {search} de un coscorron")
            await self.reproducir_sonido('sonidos/coscorron.wav')
    @commands.command()
    async def corre(self, ctx: commands.Context):
            await self.reproducir_sonido('sonidos/corree.mp3')
    @commands.command()
    async def tocktock(self, ctx: commands.Context):
            await self.reproducir_sonido('sonidos/tocktock.wav')
    @commands.command()
    async def ds(self, ctx: commands.Context):
        await ctx.send("Este es nuestro canal de discord para todos los panas!!! https://discord.com/invite/B3m62jnjrz")
    @commands.command()
    async def so(self, ctx: commands.Context,search: str):
            n = len(ctx.message.content)
            mensage = ctx.message.content
            await ctx.send('Siguan a https://www.twitch.tv/' + search )
    @commands.command()
    async def memide(self, ctx: commands.Context):
            R = random.randint(2,30)
            await ctx.send(f"A @{ctx.author.name} le mide: " + str(R)+ "cm")
            if R >20:
                  await self.reproducir_sonido('sonidos/Memide.wav')
    @commands.command()
    async def amor(self, ctx: commands.Context,search: str):
            n = len(ctx.message.content)
            mensage = ctx.message.content
            R = random.randint(0,100)
            if search == "" or search == " ":
                await ctx.send(f"para este comando es necesario que menciones a alguien")
            else:

                await ctx.send(f"El amor entre @{ctx.author.name} y {search} es de: "+ str(R)+ "% <3")
                if R >90:
                    print("hola")
                    await self.reproducir_sonido('sonidos/sensual.mp3')
                print(n)
    @commands.command()
    async def ruleta(self, ctx: commands.Context):
         R = random.randint(0,6)
         if R == 6 :
              await ctx.send(f"{ctx.author.name} Jaló el gatillo y... Boooom!!!")
         else:
              await ctx.send(f"{ctx.author.name} jaló el gatillo y... la bala no fue disparada.") 
    @commands.command()
    async def bola8(self, ctx: commands.Context):
            n =len(boll8)
            if n <= 6:
                  await ctx.send(f"Para usar este comando, tenes que preguntar algo")
            else:
                R = random.randint(0,n-1)
                await ctx.send(boll8[R])
                if R >20:
                    await self.reproducir_sonido('sonidos/Memide.wav')

    
    
    @commands.command()

    
    async def facha(self, ctx: commands.Context):
            n = len(ctx.message.content)
            mensage = ctx.message.content
            R = random.randint(0,100)
            await ctx.send(f"{ctx.author.name}tiene una facha de: 62%")
            if R >90:
                await self.reproducir_sonido('sonidos/sensual.mp3')
                print(n)

    @commands.command()
    async def title(self, ctx: commands.Context):
            n = len(ctx.message.content)
            mensage = ctx.message.content[7:n]
            engine.say(ctx.author.name + " a cambiado el titulo a: " + mensage)
            #chatVoz.save("sonidos/audio.mp3")
            #playsound("sonidos/audio.mp3")
            #remove("sonidos/audio.mp3")
            engine.runAndWait()
    @commands.command()
    async def game(self, ctx: commands.Context):
            n = len(ctx.message.content)
            mensage = ctx.message.content[5:n]
            engine.say(ctx.author.name + " a cambiado la categoria a: " + mensage)
            #chatVoz.save("sonidos/audio.mp3")
            #playsound("sonidos/audio.mp3")
            #remove("sonidos/audio.mp3")
            engine.runAndWait()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    async def reproducir_sonido(self, archivo):
        wf = wave.open(archivo, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        chunk_size = 1024
        data = wf.readframes(chunk_size)

        while data:
            stream.write(data)
            data = wf.readframes(chunk_size)

        stream.stop_stream()
        stream.close()

        p.terminate()
bot = Bot()


bot.run()