import tkinter as tk
from tkinter import ttk
from src.Comandos import CommandApp
from src.General import GeneralApp
from src.Chat import ChatApp
import threading
import configparser
import multiprocessing
from src.funciones import *

config = configparser.ConfigParser()
# config.read('src/parametros/archivo_parametros.ini')

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz Principal")
        
        # Crear el Notebook
        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill='both')
        # Crear los frames
        self.command_app_frame = ttk.Frame(notebook)
        self.general_app_frame = ttk.Frame(notebook)
        self.chat_app_frame = ttk.Frame(notebook)
        
        # Añadir los frames al Notebook
        notebook.add(self.general_app_frame, text='General')
        notebook.add(self.command_app_frame, text='Comandos')
        notebook.add(self.chat_app_frame, text='SpeedChat')

        # Instanciar GeneralApp dentro del frame correspondiente
        self.general_app = GeneralApp(self.general_app_frame)
        self.command_app = CommandApp(self.command_app_frame)
        self.chat_app = ChatApp(self.chat_app_frame)

        notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)
        root.protocol("WM_DELETE_WINDOW", self.salir)

    def on_tab_change(self, event):
        config.read('src/parametros/archivo_parametros.ini')
        onoff_speed = config.get('parametro', 'onoff_speed')
        onoff_comandos = config.get('parametro', 'onoff_comandos')
        #onoff_comandos = config.get('parametro', 'onoff_comandos')
        if onoff_speed == 'true':
            self.chat_app.inicio_speedchat_button.config(text="Parar")
            self.general_app.inicio_speedchat_button.config(text="Parar")
        else:
            self.chat_app.inicio_speedchat_button.config(text="Iniciar")
            self.general_app.inicio_speedchat_button.config(text="Iniciar")
        if onoff_comandos == 'true': 
            self.command_app.inicio_command_button.config(text="Parar")
            self.general_app.inicio_command_button.config(text="Parar")
        else: 
            self.command_app.inicio_command_button.config(text="Inicio")
            self.general_app.inicio_command_button.config(text="Inicio")
        
        vc1 = self.general_app.commands_volume.get()
        vc2 = self.command_app.commands_volume.get()
        vc1 = int(vc1)
        vc2 = int(vc2)

        if vc1 != vc2:
            config.read('src/parametros/archivo_parametros.ini')
            self.general_app.commands_volume.set(CargarVolumenC())
            self.command_app.commands_volume.set(CargarVolumenC())
        
        vs1 = self.general_app.speedchat_volume.get()
        vs2 = self.chat_app.speedchat_volume.get()
        vs1 = int(vs1)
        vs2 = int(vs2)
        if vs1 != vs2:
            config.read('src/parametros/archivo_parametros.ini')
            self.general_app.speedchat_volume.set(config.get('parametro', 'volumens'))
            self.chat_app.speedchat_volume.set(config.get('parametro', 'volumens'))

    def salir(self):
        # Aquí puedes detener los bots si es necesario
        self.root.destroy()

def run_chat_bot():
    from src.Chat import ChatBot
    bot = ChatBot(None)
    bot.run()

def run_command_bot():
    from src.Comandos import comandosBot
    bot = comandosBot(None)
    bot.run()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)

    # Iniciar los bots en procesos separados
    #chat_bot_process = multiprocessing.Process(target=run_chat_bot)
    command_bot_process = multiprocessing.Process(target=run_command_bot)

    #chat_bot_process.start()
    command_bot_process.start()

    root.minsize(width=470, height=465)
    root.mainloop()

    # Asegurarse de que los procesos se detengan al cerrar la aplicación
    #chat_bot_process.join()
    command_bot_process.join()


    
