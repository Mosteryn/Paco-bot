import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import psutil
import configparser
from src.funciones import *
from twitchio.ext import commands
import random
import pygame
from src.funciones import *
import sqlite3
import os
import pyttsx3
from dotenv import load_dotenv
from plyer import notification
load_dotenv()
with open('src/parametros/Bola8.txt', 'r') as file:
            boll8 = [line.strip() for line 
                    in file]
engine = pyttsx3.init()
engine.setProperty("rate", 150)
config.read('src/parametros/archivo_parametros.ini')
CHANNEL= config.get('parametro', 'channel')

pygame.init()
pygame.mixer.init()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Espectadores = []

config = configparser.ConfigParser()


class CommandApp:
    def __init__(self, root):
        self.root = root
        #self.root.title("Gestor de Comandos")
        
        self.config = configparser.ConfigParser()
        self.config.read('src/parametros/archivo_parametros.ini')
        
        self.create_database()
        
        # Frame principal
        main_frame = ttk.Frame(root)
        main_frame.pack(expand=True, fill='both')
        main_frame.grid_rowconfigure(0, weight=0)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=0)  
        main_frame.grid_columnconfigure(1, weight=1)  
        

        # Sección de comandos General
        self.comandos_frame = ttk.LabelFrame(main_frame, text="Comandos")
        self.comandos_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        ttk.Label(self.comandos_frame, text="Volumen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.commands_volume = ttk.Scale(self.comandos_frame, from_=0, to=100, orient="horizontal", command= editVolumenC)
        self.commands_volume.set(CargarVolumenC())
        self.commands_volume.grid(row=0, column=1, padx=10, pady=10)
        self.inicio_command_button = ttk.Button(self.comandos_frame, text="Iniciar", command=self.ComandosCheck)
        self.inicio_command_button.grid(row=0, column=2, padx=10, pady=10)

        # Sección para agregar/editar comandos
        self.add_command_frame = ttk.LabelFrame(main_frame, text="Agregar/Editar Comando")
        self.add_command_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        ttk.Label(self.add_command_frame, text="Nombre del Comando:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.add_command_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.add_command_frame, text="Palabra Clave:").grid(row=1, column=0, padx=5, pady=5)
        self.palabraClave_entry = ttk.Entry(self.add_command_frame)
        self.palabraClave_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.var1 = tk.BooleanVar()
        self.caracter_checkbutton = tk.Checkbutton(self.add_command_frame, text="Caracter Inicial",variable=self.var1, command=self.check_caracter)
        self.caracter_checkbutton.grid(row=0, column=2,pady=10)
        self.caracter_entry = ttk.Entry(self.add_command_frame, state='disabled')
        self.caracter_entry.grid(row=0,column=3,pady=10)

        self.sonido_label = ttk.Label(self.add_command_frame, text=("Sonido:"))
        self.sonido_label.grid(row=1,column=2,pady=10)
        self.sonido_boton = ttk.Button(self.add_command_frame, text= "Seleccione", command=self.seleccionSonido)
        self.sonido_boton.grid(row=1,column=3,pady=10)

        self.add_command_button = ttk.Button(self.add_command_frame, text="Agregar Comando", command=self.create_command)
        self.add_command_button.grid(row=2, column=0, pady=10)
        
        self.edit_command_button = ttk.Button(self.add_command_frame, text="Editar Comando", command=self.edit_command)
        self.edit_command_button.grid(row=2, column=1, pady=10)

        self.respueta_frame= ttk.Labelframe(self.add_command_frame, text="Respuesta:")
        self.respueta_frame.grid(row=3, column=0, padx=5, pady=5,columnspan=3)

        self.response_entry = tk.Text(self.respueta_frame, width=40, height=10)
        self.response_entry.pack()


        # Lista de comandos
        self.commands_frame = ttk.LabelFrame(main_frame, text="Lista de Comandos")
        self.commands_frame.grid(row=0, column=0, rowspan=2, padx=0, pady=10, sticky='nsew')
        
        self.commands_frame.grid_rowconfigure(0, weight=1)
        self.commands_frame.grid_rowconfigure(1, weight=0)
        self.commands_frame.grid_columnconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.commands_frame, columns=('Nombre'), show='headings')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        
        self.delete_command_button = ttk.Button(self.commands_frame, text="Eliminar Comando", command=self.delete_command)
        self.delete_command_button.grid(row=1, column=0, pady=10)

        self.view_commands()
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.bind("<Button-3>", self.on_right_click)
        #self.bot = comandosBot(self)
        #threading.Thread(target=self.bot.run).start()
        #self.commands = {}
        self.menu = tk.Menu(root, tearoff=0)
        self.menu.add_command(label="Editar Comando", command=self.edit_command)
    def check_caracter(self):
        if self.var1.get():
             
            self.caracter_entry.config( state='enable')
        else:
            self.caracter_entry.config(state='disable')
    def seleccionSonido(self):
        #esta funcion permite la seleccion del archovo y cambia el label de sonido 
        filepath = filedialog.askopenfilename()
        filename = os.path.basename(filepath)

        self.sonido_label.config(text="Sonido:"+ filename)


    def prueba(sekf):
         print("funca")
    def on_double_click(self, event):
        self.edit_command()
    def on_right_click(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.menu.post(event.x_root, event.y_root)
    def create_database(self):
        self.conn = sqlite3.connect('commands.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS commands
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    response TEXT NOT NULL,
                    keyword TEXT NOT NULL)
                    ''')
        self.conn.commit()

    def create_command(self):
        name = self.name_entry.get()
        keyword = self.palabraClave_entry.get()
        response = self.response_entry.get("1.0", tk.END)
    
        if name and response and keyword:
            try:
                self.cursor.execute("INSERT INTO commands (name, response, keyword) VALUES (?, ?, ?)",
                                (name, response, keyword))
                self.conn.commit()
                messagebox.showinfo("Éxito", "Comando creado correctamente")
                self.clear_entries()
                self.view_commands()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "El nombre del comando ya existe")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def UPDATE_command(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            command_id = item['values'][0]
            name = self.name_entry.get()
            response = self.response_entry.get()
            keyword = self.palabraClave_entry.get()
        
            if name and response and keyword:
                try:
                    self.cursor.execute("UPDATE commands SET name=?, response=?, keyword=? WHERE id=?",
                                        (name, response, keyword, command_id))
                    self.conn.commit()
                    messagebox.showinfo("Éxito", "Comando actualizado correctamente")
                    self.clear_entries()
                    self.view_commands()
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "El nombre del comando ya existe")
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            messagebox.showerror("Error", "Selecciona un comando para editar")

    def delete_command(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            name = item['values'][0]
        
            if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar este comando?"):
                self.cursor.execute("DELETE FROM commands WHERE name=?", (name,))
                self.conn.commit()
                messagebox.showinfo("Éxito", "Comando eliminado correctamente")
                self.view_commands()
        else:
            messagebox.showerror("Error", "Selecciona un comando para eliminar")
    def view_commands(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
    
        self.cursor.execute("SELECT name FROM commands")
        self.tree.insert('', 'end', values=("Nuevo Comando"))

        for row in self.cursor.fetchall():
            self.tree.insert('', 'end', values=row)

    def iniciar_proceso3(self):
        # Ejecuta el Bot de comandos
        global p3
        proceso3 = "bot_Comandos.py"
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
            self.inicio_command_button.config(text="Iniciar")
        else:
            p2 = subprocess.Popen(proceso3, shell=True)
            self.inicio_command_button.config(text="Parar")
    def add_command(self):
        name = self.name_entry.get()
        command_id = self.command_id_entry.get()
        response = self.response_entry.get()
        messagebox.showinfo("Aviso", agregar_linea(command_id,response))
    
    def edit_command(self):
        selected_item = self.tree.selection()
        
        
        if selected_item:
            posicion = self.tree.index(selected_item[0])
            if posicion == 0: 
                self.clear_entries()
                return
            item = self.tree.item(selected_item[0])
            name = item['values'][0]
            self.cursor.execute("SELECT * FROM commands WHERE name=?", (name,))
            rows = self.cursor.fetchall()
        # Llenar los campos de entrada con los valores actuales
            for row in rows:
                id = row[0]
                self.clear_entries()
                self.name_entry.insert(0,row[1])
                self.palabraClave_entry.insert(0,row[3])
                self.response_entry.insert(tk.END, row[2])
            for row in rows: 
                """ name)
                self.response_entry.delete(0, row[1])
                 row[2])
                 row[3])
            #self.palabraClave_entry.insert(0, current_keyword)"""

        # Función interna para realizar la actualización
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.response_entry.delete(1.0, tk.END)
        self.palabraClave_entry.delete(0, tk.END)
    def ComandosCheck(self):
     
        config.read('src/parametros/archivo_parametros.ini')
        onoff_comandos = config.get('parametro','onoff_comandos' )
        if onoff_comandos == 'false':
            print("Comandos iniciado")
            notification.notify(
                title="¡Ya esta iniciado los Comandos!",
                message="¡Ya se conecto correctamente con " + CHANNEL,
                app_name="PacoBot",
                app_icon='src/parametros/PacoBot.ico'
            )
            config.set('parametro', 'onoff_comandos', 'true')
            with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                 config.write(archivo_parametros)
            self.inicio_command_button.config(text="Parar")
        else:
            print("Comandos deteniendo")
            config.set('parametro', 'onoff_comandos', 'false')
            with open('src/parametros/archivo_parametros.ini', 'w') as archivo_parametros:
                 config.write(archivo_parametros)
            self.inicio_command_button.config(text="Iniciar")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class comandosBot(commands.Bot):
    

    def __init__(self,app):
        super().__init__(token=os.environ['TWITCH_TOKEN'],
                         prefix=os.environ['BOT_PREFIX'],
                         initial_channels=[CHANNEL])
        self.app = app
        self.conn = sqlite3.connect('commands.db')
        self.cursor = self.conn.cursor()
        

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def event_ready(self):
        
        print("Comandos iniciado")

    async def event_message(self, message):
        nick = message.author.name
        print(nick , ": " , message.content)
        
        if not nick in Espectadores:

            Espectadores.append(nick)
        config.read('src/parametros/archivo_parametros.ini')
        onoff_comandos= config.get('parametro','onoff_comandos' )
        if not onoff_comandos =="true" : 
             return
        if  "!" in message.content.lower():
            command = message.content.split()[0].lower()
            self.cursor.execute("SELECT response FROM commands WHERE keyword=?", (command,))
            result = self.cursor.fetchone()

            if result:
                # Si se encuentra el comando, envía la respuesta
                await message.channel.send(result[0])

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if "custom-reward-id=" in message.raw_data: 
            if "custom-reward-id=5e76d158-a1c2-4bcb-a197-b6f2c0595d6d" in message.raw_data:
                
                await message.channel.send("en seguida Vamos con" + message.content)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        if message.echo:
            return
        
        if  "hola" in message.content.lower()  or  "buenas" in message.content.lower()  or  "hello" in message.content.lower():
            await self.reproducir_sonido('src/sonidos/buenas.wav')
        if  "gg" in message.content.lower():
                await self.reproducir_sonido('src/sonidos/gg.wav')
        if "sensual" in message.content.lower() or "sexi" in message.content.lower() :
            await self.reproducir_sonido('src/sonidos/sensual.mp3')
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
            await self.reproducir_sonido('src/sonidos/susto'+ str(r) +'.wav')
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
                await self.reproducir_sonido('src/sonidos/coscorron.wav')
            else:

                    await ctx.send(f"{ctx.author.name} Mando a mimir a {Nombre} de un coscorron")
                    await self.reproducir_sonido('src/sonidos/coscorron.wav')
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
            await self.reproducir_sonido('src/sonidos/corree.wav')
    @commands.command()
    async def tocktock(self, ctx: commands.Context):
            await self.reproducir_sonido('src/sonidos/tocktock.wav')
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
                  await self.reproducir_sonido('src/sonidos/Memide.wav')
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
                    await self.reproducir_sonido('src/sonidos/sensual.mp3')
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
                    await self.reproducir_sonido('src/sonidos/Memide.wav')
    @commands.command()
    async def facha(self, ctx: commands.Context):
            n = len(ctx.message.content)
            mensage = ctx.message.content
            R = random.randint(0,100)
            await ctx.send(f"{ctx.author.name}tiene una facha de: 62%")
            if R >90:
                await self.reproducir_sonido('src/sonidos/sensual.mp3')
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
        config.read('src/parametros/archivo_parametros.ini')
        volumen = float(CargarVolumenC())
        archivo_audio = archivo  
        sound = pygame.mixer.Sound(archivo_audio)
        sound.set_volume(volumen/100)
        sound.play()
    def start(self):
        self.run()
# No ejecutar la interfaz gráfica si se importa este archivo
