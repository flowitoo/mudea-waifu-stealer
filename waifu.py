import discord
import json
import re
from discord.ext import tasks
import asyncio

bot = discord.Client()

token = "token" # <--- Enter your token here

@bot.event
async def on_ready():
    global mudaeID
    global mudaemaidID
    global yourID
    global server1
    global server2
    global server3
    global minKakera
    
    minKakera = int(400) # <--- Minimum kakera for waifu to have in order to claim it.
    mudaeID = 432610292342587392
    mudaemaidID = 509695019767037953
    yourID = 745736015146123348
    server1 = bot.get_channel(123456789123456789) # <--- channel id for commands/mudae channel in a server
    server2 = bot.get_channel(123456789123456789) # <--- channel id for commands/mudae channel in a server
    server3 = bot.get_channel(123456789123456789) # <--- channel id for commands/mudae channel in a server

    print("I'm online!")
    await start_tasks() # <--- You can comment this line if you do not want to claim daily kakera or roll waifus (only waifu stealing)
    
async def start_tasks():
    daily_kakera.start()
    await asyncio.sleep(5)
    roll_waifus.start()

@bot.event
async def on_reaction_add(reaction, user):
    embeds = reaction.message.embeds
    if reaction.message.author.id == mudaeID or reaction.message.author.id == mudaemaidID:
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
        await server1.send('$w')
        await asyncio.sleep(2)
        
        await server2.send('$w')
        await asyncio.sleep(2)
        
        await server3.send('$w')
        await asyncio.sleep(5)
        # You can add more servers there. Check lines 25 - 28
    print('  out of rolls.')

@tasks.loop(hours=21)
async def daily_kakera():
    print(' claiming daily kakera.')
    try:
        await server1.send('$dk')
        await server2.send('$dk')
        await server3.send('$dk')
        # You can add more servers there. Check lines 25 - 28
    except:
        print('   [!] Looks like I do not have permissions to send a message (daily_kakera function)')
    print(' daily kakera claimed!')

bot.run(token, bot=False) 
