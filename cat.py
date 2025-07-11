import nextcord
from nextcord.ext import commands
import requests, random
import catConfig

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

api_key = catConfig.get_api_key()

@bot.command()
async def cat(ctx, count: int = 1, breed_id: str = None):
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        "x-api-key": api_key
    }

    if count > 5:
        await ctx.send("You can request up to 5 cat images at a time. Please reduce the limit to at most 5.")
        return
    
    if count < 1:
        await ctx.send("You must request at least 1 cat image. Showing 1 image.")
        count = 1

    if breed_id:
        url += f"?breed_ids={breed_id}&limit={count}"
    else:
        url += f"?limit={count}"

    response = requests.get(url, headers=headers)
    
    print(response.status_code)
    print(response.content)

    if response.status_code == 200:
        cat_data = response.json()
        if cat_data:
            cat_image_urls = [cat["url"] for cat in cat_data]
            await ctx.send("\n".join(cat_image_urls))  # Send all URLs in one message
        else:
            await ctx.send("No cat images found.")
    else:
        await ctx.send("Failed to fetch cat images.")

# Command that detects the cat emoji, and returns a random cat image if cat emoji is present
@bot.event
async def on_message(message):
    if "🐱" in message.content:
        cat_image_url = get_random_cat_image()
        if cat_image_url:
            await message.channel.send(cat_image_url)
        else:
            await message.channel.send("Failed to get a cat image. Meow!")

    if message.content == "!catBreeds":
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        
        if response.status_code == 200:
            breeds_data = response.json()
            breed_info = [(breed["id"], breed["name"]) for breed in breeds_data]
            breed_info_string = "\n".join([f"{breed[0]} - {breed[1]}" for breed in breed_info])
            await message.channel.send(f"Available breed IDs and names:\n{breed_info_string}\n\nNote: Please use the breed ID when querying a specific breed.")
        else:
            await message.channel.send("Failed to fetch breed data.")

    await bot.process_commands(message)

def get_random_cat_image():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        cat_data = response.json()
        if cat_data:
            cat_image_url = cat_data[0]["url"]
            return cat_image_url
    return None

# Event handling
@bot.command()
async def my_command(ctx):
    # Command code here
    await ctx.send("Command executed!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is connected and ready.")

@bot.event
async def on_connect():
    print(f"{bot.user.name} is connected to the server.")

@bot.event
async def on_disconnect():
    print("Bot has disconnected from the server.")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"Error occurred: {args[0]}")

@bot.event
async def on_command_error(ctx, error):
    print(f"Command error: {error}")

token = catConfig.get_token()

bot.run(token)