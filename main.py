import discord, random
from discord.ext import commands
from config import token
from discord import File

client = commands.Bot(command_prefix = '.')

@client.command()
async def roll(ctx, integer):
    await ctx.reply(str(random.randint(0, int(integer))), mention_author=False)

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
            strEmb += embed.description
            for f in embed.fields:
                await message.channel.send(content=strEmb)
                strEmb += f.name
                strEmb += f.value

    msg = message.content.lower()
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
