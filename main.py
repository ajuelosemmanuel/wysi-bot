import discord, random
from discord.ext import commands
from config import token

client = commands.Bot(command_prefix = '.')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Wondering what comes after 726...'))
    print("[Bot Status] Bot is now ON.")

@client.command()
async def roll(ctx, n):
    ret = random.randint(0,n)
    await ctx.reply(str(ret), mention_author=False)

@client.event
async def on_message(message):
    msg = message.content.lower()
    if "727" in msg:
        await message.channel.send(content="WYSI")
        rng = random.randint(0, 1000)
        if rng == 727:
            message.channel.send(content=None, tts=False, embed=None, file=discord.File('./media/bz.jpg'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
        elif 695 <= rng <= 705:
            message.channel.send(content=None, tts=False, embed=None, file=discord.File('./media/cookingz.png'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
        elif 0 <= rng <= 100:
            message.channel.send(content=None, tts=False, embed=None, file=discord.File('./media/wysicaps.jpg'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
        else:
            message.channel.send(content=None, tts=False, embed=None, file=discord.File('./media/wysiaireu.gif'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)

client.run(token)