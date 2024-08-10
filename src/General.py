import tkinter as tk
from tkinter import ttk
import threading
import configparser
import subprocess
import time
import psutil
from plyer import notification
from src.funciones import *
from src.Chat import ChatBot
config = configparser.ConfigParser()
config.read('src/parametros/archivo_parametros.ini')


class GeneralApp:
    def __init__(self, root):
        
        self.root = root
        #self.root.title("General")
        
        # Crear la interfaz de la General
        self.info_frame = ttk.LabelFrame(root, text="Información")
        self.info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        ttk.Label(self.info_frame, text="Nick del canal:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.nick_entry = ttk.Entry(self.info_frame)
        self.nick_entry.grid(row=0, column=1, padx=10, pady=10)
        self.nick_entry.insert(0,config.get('parametro', 'channel'))
        ttk.Button(self.info_frame, text="Guardar",command= self.obtener_datos).grid(row=0, column=2, padx=10, pady=10)
        
        # Crear la seccion de speedchat
        self.speedchat_frame = ttk.LabelFrame(root, text="SpeedChat")
        self.speedchat_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        ttk.Label(self.speedchat_frame, text="Volumen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.speedchat_volume = ttk.Scale(self.speedchat_frame, from_=0, to=100, orient="horizontal",command= volumenS)
        self.speedchat_volume.set(config.get('parametro','volumens'))
        self.speedchat_volume.grid(row=0, column=1, padx=10, pady=10)
        self.inicio_speedchat_button = ttk.Button(self.speedchat_frame, text="Iniciar", command= self.speekChatCheck)
        self.inicio_speedchat_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.comandos_frame = ttk.LabelFrame(root, text="Comandos")
        self.comandos_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        ttk.Label(self.comandos_frame, text="Volumen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.commands_volume = ttk.Scale(self.comandos_frame, from_=0, to=100, orient="horizontal", command= volumenC)
        self.commands_volume.set(config.get('parametro','volumenc'))
        self.commands_volume.grid(row=0, column=1, padx=10, pady=10)
        self.inicio_command_button=ttk.Button(self.comandos_frame, text="Iniciar", command=self.ComandsCheck)
        self.inicio_command_button.grid(row=0, column=2, padx=10, pady=10)
        
        ttk.Button(self.root, text="Salir", command=self.salir).grid(row=3, column=0, padx=10, pady=10)

    def speekChatCheck(self):
     
        """config.read('src/parametros/archivo_parametros.ini')
        if config.get('parametro','onoff_speed' ) == 'false':
            print("Comandos iniciado")
            config.set('parametro', 'onoff_speed', 'true')
            with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                 config.write(archivo_parametros)
            self.inicio_command_button.config(text="Parar")
            notification.notify(
                title="¡Ya esta iniciado los Comandos!",
                message="¡Ya se conecto correctamente con " + config.get('parametro', 'channel'),
                app_name="PacoBot"
            )
        else:
            print("Comandos deteniendo")
            config.set('parametro', 'onoff_speed', 'false')
            with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                 config.write(archivo_parametros)
            self.inicio_command_button.config(text="Iniciar")"""
    def ComandsCheck(self):
     
        config.read('src/parametros/archivo_parametros.ini')
        """if config.get('parametro','onoff_comandos' ) == 'false':
            print("SpeedChat iniciado")
            config.set('parametro', 'onoff_comandos', 'true')
            with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                 config.write(archivo_parametros)
            self.inicio_speedchat_button.config(text="Parar")
            notification.notify(
                title="¡Ya esta iniciado El SpedChat!",
                message="¡Ya se conecto correctamente con " + config.get('parametro', 'channel'),
                app_name="PacoBot"
            )
        else:
            print("SpeedChat deteniendo")
            config.set('parametro', 'onoff_speed', 'false')
            with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                 config.write(archivo_parametros)
            self.inicio_speedchat_button.config(text="Iniciar")"""

    def salir(self):
        # Detiene ambos procesos antes de salir del programa
        global p1 
        global p2
        global proceso1 
        global proceso2
        procesos = psutil.process_iter()
        for proceso in procesos:
            try:
                lista = proceso.cmdline()
                if proceso.name() == 'python.exe' and 'botMusica.py' in proceso.cmdline()[1] :
                    # El proceso es un subproceso de tu proyecto, lo cerramos
                    proceso.kill()
                    proceso.terminate()
                if  proceso.name() == 'python.exe' and 'SpeedChat.py' in proceso.cmdline()[1]:
                    proceso.kill()
                    proceso.terminate()
                if  proceso.name() == 'python.exe' and 'bot_Comandos.py' in proceso.cmdline()[1]:
                    proceso.kill()
                    proceso.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                pass
        
        
        tk.quit()
    def obtener_datos(self):
        config.read('src/parametros/archivo_parametros.ini')
        Canal = self.nick_entry.get()
        config.set('parametro', 'channel', Canal)
        with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
        CHANNEL= config.get('parametro', 'channel')
        print(CHANNEL)

        
if __name__ == "__main__":
    root = tk.Tk()
    app = GeneralApp(root)
    root.mainloop()