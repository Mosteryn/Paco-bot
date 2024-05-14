from twitchio.ext import commands
import twitchio.ext.sounds as sounds
from twitchio.ext import routines
from playsound import playsound
import configparser
from gtts import gTTS
from os import remove
from dotenv import load_dotenv
import random
import sys
import os
from dotenv import load_dotenv

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
load_dotenv()
config = configparser.ConfigParser()
bot_name='botpaco0'
Musica_bot = []

with open('parametros/musica.txt', 'r') as file:
            AutoPlaylist = [line.strip() for line 
                    in file]
with open('parametros/blacklis.txt', 'r') as file:
            listaNegra = [line.strip() for line 
                    in file]
#for x in AutoPlaylist:
  #print(x)
Activo = "Falso"
track = ""
Mp = False
AP = False

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Bot(commands.Bot):
    def __init__(self): 
        super().__init__(token= os.environ['TWITCH_TOKEN'], prefix=os.environ['BOT_PREFIX'],initial_channels=[os.environ['CHANNEL']])
        self.player = sounds.AudioPlayer(callback=self.player_done)
        self.player.volume = 5
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def event_ready(self):
        print("bot de musica iniciado")
        #print(f'Logged in as | {self.nick}')
        #print(f'User id is | {self.user_id}')
    async def player_done(self):
        print('Cancion terminada!')
    #async def event_message(self, message):
        #nombre = message.author.display_name
        #print(nombre)
        #if nombre in listaNegra:
            #return 
        #elif message.content[0] == "!":
            #await self.handle_commands(message)
        #else:
            #print(message.author.name , ": " , message.content)      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    @routines.routine(seconds=1.0)
    async def parametros():
        global AP
        config.read('parametros/archivo_parametros.ini')
        volumen = int(config.get('parametro', 'volumen'))
        if not volumen == bot.player.volume:
            bot.player.volume = volumen
            #print("volumen cambio a: ", volumen)
        if not str(AP) == config.get('parametro', 'autoplay'):
            if config.get('parametro', 'autoplay') == 'False': 
                AP = False
                #print("Buen desactivemos el autoplay")
            if config.get('parametro', 'autoplay') == 'True':
                AP = True
                #print("Buen activemos el autoplay")
        if config.get('parametro','stop') == 'True':
            #print("pe")
            bot.player.stop()
        if config.get('parametro','pausa') == 'True':
            if bot.player.is_paused:
                bot.player.resume()
            else:
                bot.player.pause()
    parametros.start()
    @routines.routine(seconds=5.0)
    async def music():
         global Mp
         if bot.player.is_playing == False and Musica_bot and Mp == False:
            track = await sounds.Sound.ytdl_search(Musica_bot[0])
            Musica_bot.remove(Musica_bot[0])
            bot.player.play(track)
            #print(f'reproduscamos: {track.title}')
            Mp = True
         elif AP and bot.player.is_playing == False and Mp == False:
                R = random.randint(0,len(AutoPlaylist)-1)
                #print(R)
                track = await sounds.Sound.ytdl_search(AutoPlaylist[R])
                bot.player.play(track)
                #print(f'reproduscamos: {track.title}')
                Mp = True
         else: 
              Mp = False
    music.start()
    async def mensage(self, ctx : commands.Context):
         await ctx.send()
    @commands.command()
    async def play(self, ctx: commands.Context) -> None:
        n = len(ctx.message.content)
        
        #print(n)
        if n <= 5:
            await ctx.send(f"Tenes que decirme el nombre de la cancion que queres escuchar")
        else:
            mensage = ctx.message.content[6:n]
            #print(mensage)
            #track = await sounds.Sound.ytdl_search(mensage)
            if mensage in Musica_bot:
                await ctx.send(f'La musica que pides ya esta en la lista')
            else: 
                Musica_bot.append(mensage)
                await ctx.send(f'Bueno agregemos a la lista: {track.title}' + " en la posición #" + str((len(Musica_bot))))
                #print(Musica_bot)
                AP = False
            if  not mensage in AutoPlaylist:
                #print(AutoPlaylist)
            #else:
                #print("1")
                with open('parametros/musica.txt', 'a') as archivo:
                    AutoPlaylist.append(mensage)
                    file.close()
                    archivo.write( mensage + '\n')
    @commands.command()
    async def autoplay(self, ctx: commands.Context) -> None:
        global AP 
        if ctx.author.is_mod :
             frace= "hola Buenos dias\n" + "esto es la linea 2 \n" + "esta es la linea 3"
             if (AP):
                await ctx.send(f"Bueno desactivemos el autoplay")
                AP = False
             else:
                await ctx.send(f"Bueno activemos el autoplay")
                AP = True
                #for x in AutoPlaylist:
                    #Musica_bot.append(x)
    @commands.command()
    async def comandos(self, ctx: commands.Context):
         await ctx.send("Comandos de la musica: play, autoplay, pausa, reanudar, skip")
    @commands.command()
    async def pausa(self, ctx: commands.Context) -> None:
        self.player.pause()
        await ctx.send("bueno, pungamos en pausa la musica")
    @commands.command()
    async def reanudar(self, ctx: commands.Context) -> None:
        await ctx.send("bueno, despausa la musica")
        self.player.resume()
    @commands.command()
    async def volumen(self, ctx: commands.Context) -> None:
        n = len(ctx.message.content)
        #print(n)
        if n <= 8:
            
            await ctx.send("El volumen esta en "+ str(self.player.volume) +"%")
        else:
            mensage = ctx.message.content[8:n]
            if ctx.author.is_mod:
                self.player.volume = int(mensage)
                config.set('parametro', 'volumen', mensage)
                with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                    config.write(archivo_parametros)
                await ctx.send(f"el volumense establecio en: "+ str(self.player.volume)+"%")
    @commands.command()
    async def skip(self, ctx: commands.Context) -> None:
        self.player.stop()
    @commands.command()
    async def activa(self, ctx: commands.Context) -> None:
        print(self.player.is_playing)
    @commands.command()
    async def M(self, ctx: commands.Context):
         await ctx.send("Comandos de la musica: play, autoplay, pausa, reanudar, skip")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot = Bot()
bot.run()