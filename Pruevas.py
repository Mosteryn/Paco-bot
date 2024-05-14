from twitchio.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token= os.environ['TWITCH_TOKEN'], prefix=os.environ['BOT_PREFIX'],initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    @commands.command(name='puntos')
    async def my_command(self, ctx):
        await ctx.send(f'Hola, {ctx.author.name}!')

bot = Bot()
bot.run()
