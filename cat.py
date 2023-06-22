import nextcord
from nextcord.ext import commands
import requests, random
import catConfig

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

api_key = catConfig.get_api_key()

# Command to fetch and display a random cat image URL
@bot.command()
async def cat(ctx):
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        "x-api-key": api_key
    }
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        cat_data = response.json()
        if cat_data:
            cat_image_url = random.choice(cat_data)['url']
            await ctx.send(cat_image_url)
        else:
            await ctx.send('No cat image found.')
    else:
        await ctx.send('Failed to fetch cat image.')

# Event handling
@bot.command()
async def my_command(ctx):
    # Command code here
    await ctx.send("Command executed!")

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected and ready.')

@bot.event
async def on_connect():
    print(f'{bot.user.name} is connected to the server.')

@bot.event
async def on_disconnect():
    print('Bot has disconnected from the server.')

@bot.event
async def on_error(event, *args, **kwargs):
    print(f'Error occurred: {args[0]}')

@bot.event
async def on_command_error(ctx, error):
    print(f'Command error: {error}')

token = catConfig.get_token()

bot.run(token)