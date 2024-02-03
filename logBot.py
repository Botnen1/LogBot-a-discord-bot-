import discord
from discord.ext import commands
from webserver import keep_alive
import responses1

bot = commands.Bot(command_prefix=".")

hemmeligkode = "      ----    INSERT BOT TOKEN HERE    -----     "

@bot.event
async def on_ready():
  print("Bot is ONLINE!...")


@bot.event
async def on_ready():
    activity = discord.Game(name="  ---  INSERT COOL STATUS HERE  ----    ", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")


@bot.command()
async def send_message(message, user_message, is_private):
        try:
            respons = responses1.get_response(user_message)
            await message.author.send(respons) if is_private else await message.channel.send(respons)
            
        except Exception as e:
            print(e) 

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message starts with the bot's command prefix
    if message.content.startswith(bot.command_prefix):
        # Check if the message is a command and not just a random message starting with the command prefix
        ctx = await bot.get_context(message)
        if ctx.valid:  # If it's a valid command, let the command handler take care of it
            await bot.process_commands(message)
            return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    
        
    print(f'{username} said: "{user_message}" ({channel})')
        
    liste = message.id
        
        
        
    with open("log.txt", "a") as f:
        f.write("user : ")
        f.write(username)
        f.write("\n")
        f.write("said : ")
        f.write(user_message)
        f.write("\n")
        f.write("in channel : ")
        f.write(channel)
        f.write("\n")
        f.write("message ID : ")
        f.write(str(liste))
        f.write("\n")
        f.write("\n")
            
            
            
    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)


      

keep_alive()

bot.run(hemmeligkode)


