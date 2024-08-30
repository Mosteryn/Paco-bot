from tkinter import *
import configparser
import subprocess
import time
import psutil
import sqlite3
config = configparser.ConfigParser()
config.read('src/parametros/archivo_parametros.ini')

config.set('parametro','onoff_speed','false')
config.set('parametro','onoff_comandos','false')

with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
    config.write(archivo_parametros)



def volumenS(valor):
        config.read('src/parametros/archivo_parametros.ini')
        config.set('parametro', 'volumens', valor)
        with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
def volumenC(valor):
        config.read('src/parametros/archivo_parametros.ini')
        config.set('parametro', 'volumenc', valor)
        with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
def CargarVolumenC():
    try:
        sqliteConnection = sqlite3.connect('commands.db')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT volumenc FROM parametros"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            valor = int(row[0])
            return valor
        
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def cargarVolumenS():
    try:
        sqliteConnection = sqlite3.connect('commands.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT volumens FROM `parametros`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            valor = int(row[0])
            return  valor
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def editVolumenC(valor):
    try:
        sqliteConnection = sqlite3.connect('commands.db')
        cursor = sqliteConnection.cursor()

        cursor.execute('UPDATE parametros SET volumenc = ? ',(valor,))
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def editVolumenS(valor):
    try:
        sqliteConnection = sqlite3.connect('commands.db')
        cursor = sqliteConnection.cursor()


        cursor.execute('UPDATE parametros SET volumens = ? ',(valor,))
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def Skip():
        config.read('src/parametros/archivo_parametros.ini')
        config.set('parametro', 'stop', 'True')
        with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
        config.set('parametro', 'stop', 'False')
        # Esperar 1 segundo
        time.sleep(1)
        with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            config.write(archivo_parametros)
def agregar_linea(command,response):
    nueva_linea = "    @commands.command()\n    async def " + command + "(self, ctx: commands.Context):\n        await ctx.send('" + response + "')"
    if nueva_linea:
        try:
            with open('bot_Comandos.py', 'r') as archivo:
                lineas = archivo.readlines()
            
            # Insertar la nueva línea en la posición 1 (línea 2 en términos humanos)
            lineas.insert(87, nueva_linea + '\n')
            
            with open('src/bot_Comandos.py', 'w') as archivo:
                archivo.writelines(lineas)
            
            return "Se agrego corectamente el comando !"+ command +" con la respuesta: "+response+". ahora toca esperar a que el streaner reinicie los comandos"
            entrada.delete(0, tk.END)
        except FileNotFoundError:
            return "El archivo 'codigo.py' no existe."
    else:
        return "El campo de texto está vacío."
#def Pausa():
        #config.set('parametro','pausa','True')
       # with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            #config.write(archivo_parametros)
        #config.set('parametro','pausa','False')
        #time.sleep(1)
        #with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
            #config.write(archivo_parametros)
        #cambiarBoton(btnPausa)
#def Autoplay():
        #config.read('parametros/archivo_parametros.ini')
        #if config.get('parametro', 'autoplay') == 'True':
            #config.set('parametro', 'autoplay', 'False')
            #with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                #config.write(archivo_parametros)
        #elif config.get('parametro', 'autoplay') == 'False':
            #config.set('parametro', 'autoplay', 'True')
            #with open('parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                #config.write(archivo_parametros)
        #cambiarBoton(btnAutoPlay)

        # Escribir el archivo de parámetros modificado
        
#def iniciar_proceso1():
        # Ejecuta el Bot De musica
        #global p1 
        #global proceso1
        #activo = False
        #procesos = psutil.process_iter()
        #for proceso in procesos:
            #try:
                #if proceso.name() == 'python.exe' and proceso1 in proceso.cmdline()[1] :
                   #activo = True
            #except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # El proceso ya terminó o no se puede acceder, lo ignoramos
                #pass
        #if activo:
            #StopMusica()
        #else:
           # p1 = subprocess.Popen(proceso1, shell=True)
        #time.sleep(3)
        #cambiar(botMusica_frame,btnInicioMusica)

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

        if boton["fg"] == "SystemButtonText":
            boton.config(fg="Green")
        else:
            boton.config(fg="SystemButtonText")
def cambiar(label,boton):
        # Cambia el color del botón cuando se hace clic en él
        if boton["text"] == "Iniciar":
            boton.config(text="Parar")
        else:
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


