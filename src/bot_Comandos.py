from twitchio.ext import commands
import playsound
import random
import pygame

from funciones import *

import os
import pyttsx3
import configparser
from dotenv import load_dotenv
from plyer import notification
load_dotenv()
with open('parametros/Bola8.txt', 'r') as file:
            boll8 = [line.strip() for line 
                    in file]
engine = pyttsx3.init()
engine.setProperty("rate", 150)

config = configparser.ConfigParser()
config.read('parametros/archivo_parametros.ini')
with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
    config.write(archivo_parametros)
CHANNEL= config.get('parametro', 'channel')

pygame.init()
pygame.mixer.init()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Espectadores = []
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Bot(commands.Bot):
    

    def __init__(self):
        super().__init__(token= os.environ['TWITCH_TOKEN'],
                          prefix=os.environ['BOT_PREFIX'],
                          initial_channels=[CHANNEL])
        

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def event_ready(self):
        
        print("Comandos iniciado")

        notification.notify(
            title="¡Ya esta iniciado los Comandos!",
            message="¡Ya se conecto correctamente con " + CHANNEL,
            app_name="PacoBot"
        )

    async def player_done(self):
        print('Finished playing song!')

    async def event_message(self, message):
        nick = message.author.name
        print(nick , ": " , message.content)
        
        if not nick in Espectadores:

            Espectadores.append(nick)
            

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
        if "sensual" in message.content.lower() or "sexi" in message.content.lower() :
            await self.reproducir_sonido('sonidos/sensual.mp3')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        await self.handle_commands(message)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    async def addcommand(self, ctx):
        parts = ctx.message.content.split(' ', 2)
        if len(parts) < 3:
            await ctx.send('Uso: !addcommand <comando> <respuesta>')
            print("p1")
            return
        print("p2")
        command = parts[1]
        response = parts[2]
        await ctx.send(agregar_linea(command,response))
    @commands.command()
    async def p(self, ctx: commands.Context):
            await ctx.send("/mod Nightbot")

    @commands.command()
    async def coscorron(self, ctx: commands.Context):
            Espectador= Espectadores[random.randint(0,len(Espectadores)-1)]
            n = len(ctx.message.content)
            Nombre = '' + ctx.message.content[10: n]
            
            if '@' in Nombre:
                  Nombre = Nombre [2:]
            if n == 10 :
                
                await ctx.send(f"{ctx.author.name} Mando a mimir a {Espectador} de un coscorron")
                await self.reproducir_sonido('sonidos/coscorron.wav')
            else:

                    await ctx.send(f"{ctx.author.name} Mando a mimir a {Nombre} de un coscorron")
                    await self.reproducir_sonido('sonidos/coscorron.wav')
    @commands.command()

    async def nalgueada(self, ctx: commands.Context):
            Espectador= Espectadores[random.randint(0,len(Espectadores)-1)]
            n = len(ctx.message.content)
            Nombre = '' + ctx.message.content[10: n]
            
            if '@' in Nombre:
                  Nombre = Nombre [2:]
            if n == 10 :
                
                await ctx.send(f"{ctx.author.name} le dio una nalgueada a {Espectador}")
            else:
                    await ctx.send(f"{ctx.author.name} le dio una nalgueada a {Nombre}")
    
    @commands.command()
    async def casamiento(self, ctx: commands.Context):
            Espectador= Espectadores[random.randint(0,len(Espectadores)-1)]
            n = len(ctx.message.content)
            Nombre = '' + ctx.message.content[11: n]
            
            if '@' in Nombre:
                  Nombre = Nombre [2:]
            if n == 11 :
                
                await ctx.send(f"{ctx.author.name} se caso con {Espectador}")
            else:
                    await ctx.send(f"{ctx.author.name} se caso con {Nombre}")
    
    @commands.command()
    async def beso(self, ctx: commands.Context):
            Espectador= Espectadores[random.randint(0,len(Espectadores)-1)]
            n = len(ctx.message.content)
            Nombre = '' + ctx.message.content[4: n]
            
            if '@' in Nombre:
                  Nombre = Nombre [2:]
            if n == 4 :
                
                await ctx.send(f"{ctx.author.name} le a robado un beso a {Espectador}")
            else:
                    await ctx.send(f"{ctx.author.name} le a robado un beso a {Nombre}")
                    
    @commands.command()
    async def corre(self, ctx: commands.Context):
            await self.reproducir_sonido('sonidos/corree.wav')
    @commands.command()
    async def tocktock(self, ctx: commands.Context):
            await self.reproducir_sonido('sonidos/tocktock.wav')
    @commands.command()
    async def ds(self, ctx: commands.Context):
        await ctx.send("Este es nuestro canal de discord para todos los panas!!! https://discord.com/invite/B3m62jnjrz")
        await ctx.send("Este es nuestro canal de discord para todos los Anni!!! https://discord.gg/kXrEjAU")
    @commands.command()
    async def dc(self, ctx: commands.Context):
        await ctx.send("Este es nuestro canal de discord para todos los panas!!! https://discord.com/invite/B3m62jnjrz")
        await ctx.send("Este es nuestro canal de discord para todos los Anni!!! https://discord.gg/kXrEjAU")
    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send("Este es nuestro canal de discord para todos los panas!!! https://discord.com/invite/B3m62jnjrz")
        await ctx.send("Este es nuestro canal de discord para todos los Anni!!! https://discord.gg/kXrEjAU")

    @commands.command()
    async def so(self, ctx: commands.Context,search: str):
            n = len(ctx.message.content)
            n = search[:1]
            if ( n == "@"):
                  await ctx.send('Siguan a https://www.twitch.tv/' + search[1:])
            else: 
                  await ctx.send('Siguan a https://www.twitch.tv/' + search)
            
    @commands.command()
    async def memide(self, ctx: commands.Context):
            R = random.randint(2,30)
            await ctx.send(f"A @{ctx.author.name} le mide: " + str(R)+ "cm")
            if R >20:
                  await self.reproducir_sonido('sonidos/Memide.wav')
    @commands.command()
    async def amor(self, ctx: commands.Context,search: str):
            n = len(ctx.message.content)
            R = random.randint(0,100)
            if search == "" or search == " ":
                await ctx.send("para este comando es necesario que menciones a alguien")
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
            engine.runAndWait()
    @commands.command()
    async def game(self, ctx: commands.Context):
            n = len(ctx.message.content)
            mensage = ctx.message.content[5:n]
            engine.say(ctx.author.name + " a cambiado la categoria a: " + mensage)
            engine.runAndWait()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    async def reproducir_sonido(self, archivo):
        config.read('parametros/archivo_parametros.ini')
        volumen = float(config.get('parametro','volumenc' ))
        archivo_audio = archivo  
        sound = pygame.mixer.Sound(archivo_audio)
        sound.set_volume(volumen/100)
        sound.play()
    
bot = Bot()


bot.run()