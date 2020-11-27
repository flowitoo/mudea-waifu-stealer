import discord
import json
import re
from discord.ext import tasks
import asyncio

bot = discord.Client()

token = "token" # <--- Enter your token here

@bot.event
async def on_ready():
    global mudeaID
    global mudeamaidID
    global yourID
    global adria
    global brotherz
    global axis
    global minKakera
    
    minKakera = int(400) # <--- Minimum kakera for waifu to have in order to claim it.
    mudeaID = 432610292342587392
    mudeamaidID = 509695019767037953
    yourID = 745736015146123348
    adria = bot.get_channel(778010068046184459)
    brotherz = bot.get_channel(780115909788434443)
    axis = bot.get_channel(656289494743646237)

    print("I'm online!")
    await start_tasks() # <--- You can comment this line if you do not want to claim daily kakera or roll waifus (only waifu stealing)
    
async def start_tasks():
    daily_kakera.start()
    await asyncio.sleep(5)
    roll_waifus.start()

@bot.event
async def on_reaction_add(reaction, user):
    embeds = reaction.message.embeds
    if reaction.message.author.id == mudeaID or reaction.message.author.id == mudeamaidID:
            for embed in embeds:
                a = embed.to_dict()
                b = json.dumps(a)
            c = json.loads(b)
            d1 = c['author']
            e1 = d1['name']
            f1 = str(e1)
            d = c['description']
            e = str(d)
            f = re.search(r"\*\*(\d+)\*\*", e)
            g = f.group(0)
            gstr = str(g)
            gfind = re.search(r"\d+", g)
            gmatch = gfind.group(0)
            h = int(gmatch)
            try:
                d2 = c['footer']
                e2 = d2['text']
                f2 = str(e2)
                if "/" in f2:
                    return
                elif "Belongs" in f2:
                    try:
                        await reaction.message.add_reaction(reaction)
                    except:
                        print('   [!] Looks like I do not have permissions to react.')
                    if user.id == yourID:
                        print(f'     [+] i tried to claim kakera. {f1} ({h}) {f2}')
                    else:
                        return
            except:
                pass
            
            emojis = [':two_hearts:', ':heartbeat:', ':sparkling_heart:', ':cupid:', ':heart:', ':heartpulse:']
            
            if h >= minKakera:
                for emoji in emojis:
                    if str(reaction.emoji) == str(emoji):
                        try:
                            await reaction.message.add_reaction(reaction)
                        except:
                            print('   [!] Looks like I do not have permissions to react.')
                        if user.id == yourID:
                            print(f'     [+] i tried to steal {f1} ({h})')
                        else:
                            pass

@tasks.loop(minutes=60)
async def roll_waifus():
    print(' rolling waifus...')
    rolls = 10
    i = 0
    while True:
        if i == rolls:
            break
        i += 1
        await adria.send('$w')
        await asyncio.sleep(2)
        
        await brotherz.send('$w')
        await asyncio.sleep(2)
        
        await axis.send('$w')
        await asyncio.sleep(5)
        # You can add more servers there. Check lines 25 - 28
    print('  out of rolls.')

@tasks.loop(hours=21)
async def daily_kakera():
    print(' claiming daily kakera.')
    try:
        await adria.send('$dk')
        await brotherz.send('$dk')
        await axis.send('$dk')
        # You can add more servers there. Check lines 25 - 28
    except:
        print('   [!] Looks like I do not have permissions to send a message (daily_kakera function)')
    print(' daily kakera claimed!')

bot.run(token, bot=False) 
