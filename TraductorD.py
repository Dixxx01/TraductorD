import discord
from discord.ext import commands
from googletrans import Translator
import os  # Asegúrate de importar os para usar las variables de entorno

# Inicializar el traductor
translator = Translator()

# Configurar el bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento: cuando el bot esté listo
@bot.event
async def on_ready():
    print(f'Bot está listo como {bot.user}')

# Evento: cuando se recibe un mensaje
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content:  # Verifica que el mensaje no esté vacío
        translated = translator.translate(message.content, dest='es')
        await message.channel.send(translated.text)

# Token del bot
bot.run(os.getenv('DISCORD_TOKEN'))  # Asegúrate de que 'DISCORD_TOKEN' esté configurado en Railway
