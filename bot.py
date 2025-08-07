import discord
from discord.ext import commands
from clasificador import identificador 
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments: 
        # Create temp_images directory if it doesn't exist
        os.makedirs("./images", exist_ok=True)
        
        for attachment in ctx.message.attachments:
            # Check if attachment is an image
            if not attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                await ctx.send(f"Error: {attachment.filename} is not an image (.png, .jpg, .jpeg)")
                continue
                
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./images/{file_name}")
            await ctx.send(identificador(f"./images/{file_name}"))
    else:
        await ctx.send("no hay archivos adjuntos en el mensaje; mientras tanto, no olvides dejar un espacio limpio y organizado. Ademas, no olvides llevar bata, gafas y guantes para protegerte contra quimicos peligrosos")

bot.run("your token")
