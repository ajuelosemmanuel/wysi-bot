import discord, random, re
from discord.ext import commands
from config import token
from discord import File

client = commands.Bot(command_prefix = '.')

@client.command()
async def credits(ctx):
    em = discord.Embed(title = "Credits")
    em.set_thumbnail(url="https://raw.githubusercontent.com/ajuelosemmanuel/wysi-bot/main/media/wysiaireu.gif")
    em.add_field(name = "Github Repo", value = "https://github.com/ajuelosemmanuel/wysi-bot")
    await ctx.send(embed = em)

@client.command()
async def roll(ctx, integer=1000):
    await ctx.reply(str(random.randint(1, int(integer))), mention_author=False)

@client.command()
async def servers(ctx):
    await ctx.send(f"Connected on {str(len(client.guilds))} servers")
    
    
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Wondering what comes after 726...'))
    print("[Bot Status] Bot is now ON.")

@client.event
async def on_message(message):
    wysiList = ["727", "7.27", "72.7", "7:27", "7/27", "7+27", "7*27", "7,27", "72,7", "7-27", "72+7", "72-7", "72*7"]
    strEmb = ""
    if message.embeds:
        for embed in message.embeds:
            if type(embed.description) == str:
                strEmb += embed.description
            for f in embed.fields:
                strEmb += f.name
                strEmb += f.value

    strEmb = re.sub(r'<:\w*:\d*>','', strEmb)

    msg = message.content.lower()
    msg = re.sub(r'<a?:\w*:\d*>','', msg)
    msg = re.sub(r"<@.\w*>",'', msg)

    if any(ext in msg for ext in wysiList) or any(ext in strEmb for ext in wysiList):
        rng = random.randint(0, 1000)
        if rng == 727:
            await message.channel.send(content="WYSI", tts=False, embed=None, file=File('./media/bz.jpg'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
        elif 695 <= rng <= 705:
            await message.channel.send(content="WYSI", tts=False, embed=None, file=File('./media/cookingz.png'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
        elif 0 <= rng <= 100:
            await message.channel.send(content="WYSI", tts=False, embed=None, file=File('./media/wysicaps.jpg'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
        elif 101 <= rng <= 111:
            await message.channel.send(content="WYSI", tts=False, embed=None, file=File('./media/donaldwysi.png'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
        elif 990 <= rng <= 1000:
            await message.channel.send(content="WYSI", tts=False, embed=None, file=File('./media/dicarpacciowysi.jpg'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
        else:
            await message.channel.send(content="WYSI", tts=False, embed=None, file=File('./media/wysiaireu.gif'), files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
    

    
    await client.process_commands(message)

client.run(token)
