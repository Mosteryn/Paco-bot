from twitchio.ext import commands
import tkinter as tk
import tkinter as ttk
import tkinter.font as tkFont
import threading
import os
import configparser
import asyncio
from dotenv import load_dotenv
from plyer import notification
from src.funciones import *

import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 150)
with open('src/parametros/blacklis.txt', 'r') as file:
            listaNegra = [line.strip() for line 
                    in file]
load_dotenv()

config = configparser.ConfigParser()
config.read('src/parametros/archivo_parametros.ini')
with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
    config.write(archivo_parametros)

CHANNEL = config.get('parametro', 'channel')

class ChatBot(commands.Bot):
    

    def __init__(self, app):
        super().__init__(token=os.environ['TWITCH_TOKEN'],
                         prefix=os.environ['BOT_PREFIX'],
                         initial_channels=[CHANNEL])
        self.app = app

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return

        await self.handle_commands(message)
        config.read('src/parametros/archivo_parametros.ini')
        onoff_speed= config.get('parametro','onoff_speed' )
        volumen = cargarVolumenS()
        
        
        self.app.update_chat(message.author.name, message.content, message.author.color)
        if not message.author.name in listaNegra and not "!" == message.content[0:1].lower() and onoff_speed =="true":
            
            
            engine.setProperty("volume", volumen /100)
            engine.say(message.author.name + ": " + message.content)
            engine.runAndWait()
    async def send_message(self, channel, message):
        await self.get_channel(channel).send(message)
class ChatApp:
    def __init__(self, root):
        
        self.root = root
        #self.root.title("Twitch Chatbot")
        self.spedchatCheck = "false"
        self.estado_boton = False

        self.label = tk.Label(root, text="Twitch Chatbot")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.text_frame = tk.Frame(root)
        self.text_frame.grid(row=1, column=0)

        self.custom_font = tkFont.Font(family="Helvetica", size=12)

        self.text = tk.Text(self.text_frame, width=50, height=25, state='disabled', wrap='word', background='#18181B',
                    foreground='white', font=self.custom_font)
        self.text.grid(row=0, column=0, sticky="ew")

        self.scrollbar = ttk.Scrollbar(self.text_frame, command=self.text.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ew")
        self.text.config(yscrollcommand=self.scrollbar.set)
        
        self.left_frame = ttk.Frame(root)
        self.left_frame.grid(row=1, column=1, padx=10, pady=10)        

        self.speedchat_frame = ttk.LabelFrame(self.left_frame, text="SpeedChat")
        self.speedchat_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        ttk.Label(self.speedchat_frame, text="Volumen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.speedchat_volume = ttk.Scale(self.speedchat_frame, from_=0, to=100, orient="horizontal",command= editVolumenS)
        self.speedchat_volume.set(cargarVolumenS())
        self.speedchat_volume.grid(row=0, column=1, padx=10, pady=10)
        self.inicio_speedchat_button = ttk.Button(self.speedchat_frame, text="Iniciar", command= self.speekChatCheck)
        self.inicio_speedchat_button.grid(row=0, column=2, padx=10, pady=10)

        self.entry = tk.Entry(self.left_frame)
        self.entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.button = tk.Button(self.left_frame, text="Enviar", command=self.send_message)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.bot = ChatBot(self)
        threading.Thread(target=self.bot.run).start()


    def iniciospeedchat(self):
        threading.Thread(target=self.speedchat.run).start()
        
    def stop_bot(self):
        # Detén el bot de chat antes de cerrar la aplicación
        self.bot.loop.stop()
        self.root.destroy()

    def send_message(self):
        message = self.entry.get()
        self.text.config(state='normal')
        tag_name = f"user_PacoBot"
        self.text.tag_configure(tag_name, foreground="#BF565F")
        self.text.insert(tk.END, f'PacoBot": ', tag_name)
        self.text.insert(tk.END, f'{message}\n')
        self.entry.delete(0, tk.END)
        self.text.config(state='disabled')
        self.text.see(tk.END)
        # Enviar el mensaje al chat de Twitch
        asyncio.run_coroutine_threadsafe(self.bot.send_message(CHANNEL, message), self.bot.loop)

    def update_chat(self, username, message, color):
        self.text.config(state='normal')
        tag_name = f"user_{username}"
        self.text.tag_configure(tag_name, foreground=color)
        self.text.insert(tk.END, f'{username}: ', tag_name)
        self.text.insert(tk.END, f'{message}\n')
        self.text.config(state='disabled')
        self.text.see(tk.END)
    def speekChatCheck(self):
     
        config.read('src/parametros/archivo_parametros.ini')
        onoff_speed= config.get('parametro','onoff_speed' )
        if onoff_speed == 'false':
            print("SpeedChat iniciado")
            notification.notify(
                title="¡Ya esta iniciado El SpedChat!",
                message="¡Ya se conecto correctamente con " + CHANNEL,
                app_name="PacoBot"
            )
            config.set('parametro', 'onoff_speed', 'true')
            with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                 config.write(archivo_parametros)
            self.inicio_speedchat_button.config(text="Parar")
        else:
            print("SpeedChat deteniendo")
            config.set('parametro', 'onoff_speed', 'false')
            with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                 config.write(archivo_parametros)
            self.inicio_speedchat_button.config(text="Iniciar")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
