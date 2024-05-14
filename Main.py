from tkinter import *
import configparser
import subprocess
import signal
import os
import time
import psutil

config = configparser.ConfigParser()
config.read('parametros/archivo_parametros.ini')

proceso1 = "botMusica.py"
proceso2 = "SpeedChat.py"
proceso3 = "bot_Comandos.py"
p1 = None
p2 = None
p3 = None
config.set('parametro', 'autoplay', 'False')
config.set('parametro','pausa','False')
config.set('parametro', 'stop', 'False')

with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
    config.write(archivo_parametros)
#-------------------------------------------------------------------------------------------------------------------------------------------------
def volumen(valor):
        # Actualiza el valor de la variable 'autoplay' en el archivo de configuración
        config.set('parametro', 'volumen', valor)
        with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
def Skip():
        config.set('parametro', 'stop', 'True')
        with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
        config.set('parametro', 'stop', 'False')
        # Esperar 1 segundo
        time.sleep(1)
        with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
def Pausa():
        config.set('parametro','pausa','True')
        with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
        config.set('parametro','pausa','False')
        time.sleep(1)
        with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
        cambiarBoton(btnPausa)
def Autoplay():
        config.read('parametros/archivo_parametros.ini')
        if config.get('parametro', 'autoplay') == 'True':
            config.set('parametro', 'autoplay', 'False')
            with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                config.write(archivo_parametros)
        elif config.get('parametro', 'autoplay') == 'False':
            config.set('parametro', 'autoplay', 'True')
            with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                config.write(archivo_parametros)
        cambiarBoton(btnAutoPlay)

        # Escribir el archivo de parámetros modificado
        
def iniciar_proceso1():
        # Ejecuta el primer proceso
        global p1 
        global proceso1
        activo = False
        procesos = psutil.process_iter()
        for proceso in procesos:
            try:
                if proceso.name() == 'python.exe' and proceso1 in proceso.cmdline()[1] :
                   activo = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                pass
        if activo:
            StopMusica()
        else:
            p1 = subprocess.Popen(proceso1, shell=True)
        time.sleep(3)
        cambiar(botMusica_frame,btnInicioMusica)
def iniciar_proceso2():
        # Ejecuta el segundo proceso
        global p2
        global proceso2
        activo = False
        procesos = psutil.process_iter()
        #procesos()
        for proceso in procesos:
            try:
                if  proceso.name() == 'python.exe' and proceso2 in proceso.cmdline()[1]:
                    activo = True
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                pass
        if activo:
            StopSeetChat()
        else:
            p2 = subprocess.Popen(proceso2, shell=True)
        time.sleep(3)
        cambiar(speedChat_frame,btnInicioSpeedChat)

def iniciar_proceso3():
        # Ejecuta el segundo proceso
        global p3
        global proceso3
        activo = False
        procesos = psutil.process_iter()
        #procesos()
        for proceso in procesos:
            try:
                if  proceso.name() == 'python.exe' and proceso3 in proceso.cmdline()[1]:
                    activo = True
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                pass
        if activo:
            StopComandos()
        else:
            p3 = subprocess.Popen(proceso3, shell=True)
        time.sleep(3)
        cambiar(Comandos_frame,btnInicioComandos)

def procesos():
        procesos = psutil.process_iter()
        for proceso in procesos:
            try:
                if proceso.name() == 'python.exe':
                    # El proceso es un subproceso de Python, mostramos su información
                    print('Nombre del proceso:', proceso.name())
                    print('ID del proceso:', proceso.pid)
                    print('Comando de línea de comandos:', proceso.cmdline())
                    print('Estado del proceso:', proceso.status())
                    print('Tiempo de creación del proceso:', proceso.create_time())
                    print('Memoria utilizada por el proceso:', proceso.memory_info().rss)
                    print('--------------------------------------------------------')
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                pass
def cambiarBoton(boton):
        #print(boton.cget('foreground'))
        if boton["fg"] == "SystemButtonText":
            boton.config(fg="Green")
        else:
            boton.config(fg="SystemButtonText")
def cambiar(label,boton):
        # Cambia el color del botón cuando se hace clic en él
        #print(button.cget('bg'))
        if label["fg"] == "Red":
            label.config(fg="green")
            boton.config(text="Parar")
        else:
            label.config(fg="Red")
            boton.config(text="Iniciar")
def StopSeetChat():
        procesos = psutil.process_iter()
        #procesos()
        for proceso in procesos:
            try:
                if  proceso.name() == 'python.exe' and 'SpeedChat.py' in proceso.cmdline()[1]:
                    proceso.kill()
                    proceso.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                pass
def StopComandos():
        procesos = psutil.process_iter()
        #procesos()
        for proceso in procesos:
            try:
                if  proceso.name() == 'python.exe' and 'bot_Comandos.py' in proceso.cmdline()[1]:
                    proceso.kill()
                    proceso.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                pass
def StopMusica():
        #procesos()
        procesos = psutil.process_iter()
        for proceso in procesos:
            try:
                if proceso.name() == 'python.exe' and 'botMusica.py' in proceso.cmdline()[1] :
                    # El proceso es un subproceso de tu proyecto, lo cerramos
                    proceso.kill()
                    proceso.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                pass
def salir():
        # Detiene ambos procesos antes de salir del programa
        global p1 
        global p2
        global proceso1 
        global proceso2
        procesos = psutil.process_iter()
        #procesos()
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
        
        
        raiz.quit()

#-------Ventana principal/Raiz---------------------------------------------------------------------------------------------------
raiz = Tk()
raiz.title("BotPaco0")
raiz.resizable(False,False)
raiz.geometry("250x350")
raiz.iconbitmap("parametros/PacoBot.ico")
#------Frame1--------------------------------------------------------------------------------------------------------------------
#fBotMusica = Frame()
#fBotMusica.pack()

# Crea un marco para el botMusica
botMusica_frame = LabelFrame(raiz, text="botMusica",fg="Red", padx=20, pady=20)
botMusica_frame.place(x=5,y=0)

# Crea los botones para iniciar y detener el proceso botMusica
btnInicioMusica =  Button(botMusica_frame, text="Iniciar", command=iniciar_proceso1)
btnInicioMusica.config(cursor="hand2")
btnInicioMusica.grid()

btnAutoPlay =  Button(botMusica_frame, text="Autoplay",command=Autoplay)
btnAutoPlay.grid(row=0, column=1, padx=5, pady=5)
btnAutoPlay.config(cursor="hand2")

btnPausa =  Button(botMusica_frame, text= "Pausa", command= Pausa)
btnPausa.grid(row=0, column=2, padx=5, pady=5)
btnPausa.config(cursor="hand2")

btnSaltar=  Button(botMusica_frame, text="->", command=Skip)
btnSaltar.grid(row=0, column=3, padx=5, pady=5)
btnSaltar.config(cursor="hand2")
        
# Crea un marco para el SpeedChat
speedChat_frame = LabelFrame(raiz, text="SpeedChat",fg="Red", padx=20, pady=20)
speedChat_frame.place(x=25,y=100)

# Crea los botones para iniciar y detener el proceso SpeedChat
btnInicioSpeedChat= Button(speedChat_frame, text="Iniciar", command= iniciar_proceso2)
btnInicioSpeedChat.grid(row=0, column=0, padx=5, pady=5)
btnInicioSpeedChat.config(cursor="hand2")
# Crea un marco para el Comandos
Comandos_frame = LabelFrame(raiz, text="Comandos",fg="Red", padx=20, pady=20)
Comandos_frame.place(x=125,y=100)

# Crea los botones para iniciar y detener el proceso bot_Comandos
btnInicioComandos= Button(Comandos_frame, text="Iniciar", command=iniciar_proceso3)
btnInicioComandos.grid(row=0, column=0, padx=5, pady=5)
btnInicioComandos.config(cursor="hand2")
# Crea la barra gráfica
barra_grafica = Scale(raiz, from_=1, to=100, orient= HORIZONTAL, length=240,
                                      label="Volumen", command=volumen)
barra_grafica.set(config.get('parametro','volumen'))
barra_grafica.place(x=2,y=200)
barra_grafica.config(cursor="hand2")

# Crea un botón para salir del programa
btnSalir=  Button(raiz, text="Salir", command=salir)
btnSalir.place(x=108,y=275)
btnSalir.config(cursor="hand2")



raiz.mainloop()

