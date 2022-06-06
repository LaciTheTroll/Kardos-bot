from turtle import color
import datetime
from discord.ext import commands
from datetime import datetime
import discord
from discord import File
import datetime
from random import choice, randint
import asyncio
import libneko
from easy_pil import Editor, load_image_async, Font
import discord
import configs
from discord.ext import commands
from discord.utils import get
from moviepy.editor import *
client=commands.Bot(command_prefix=">")

intents = discord.Intents.default()
intents.members = True
x = datetime.datetime.now()
client = commands.Bot(command_prefix=">", intents=intents)
client.remove_command('help')

@commands.guild_only()
@client.group(invoke_without_command=True)
async def help(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name="⚔️ KARDOSALAKULAT ⚔️",icon_url=kardos.icon_url)
    embed.add_field(name="Fun",value="`>help fun`",inline=True)
    embed.add_field(name="Moderáció",value="`>help moderacio`",inline=True)
    embed.set_thumbnail(url=kardos.icon_url)
    await ctx.send(embed=embed)

@commands.guild_only()
@help.command(name="fun")
async def _fun(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name="⚔️ KARDOSALAKULAT ⚔️ Fun 😄",icon_url=kardos.icon_url)
    embed.add_field(name="homo",value="`>homo @Név/ID`",inline=True)
    embed.add_field(name="hitler",value="`>hitler @Név`",inline=True)
    embed.add_field(name="slap",value="`>slap @Név @Név`",inline=True)
    embed.add_field(name="bonk",value="`>bonk @Név @Név`",inline=True)
    embed.add_field(name="hotfood",value="`>hotfood @Név`",inline=True)
    embed.add_field(name="fiveman",value="`>fiveman @Név`",inline=True)
    embed.set_thumbnail(url=kardos.icon_url)
    await ctx.send(embed=embed)

@commands.guild_only()
@commands.has_permissions(kick_members=True)
@help.command(name="moderacio")
async def _moderacio(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name="⚔️ KARDOSALAKULAT ⚔️ Admin panel",icon_url=kardos.icon_url)
    embed.add_field(name="Mute", value=f"`>mute idő indok`", inline=True)
    embed.add_field(name="unmute", value=f"`>unmute Név/ID`", inline=True)
    embed.add_field(name="whois", value=f"`>userinfo Név/ID`", inline=True)
    embed.add_field(name="hackwhois", value=f"`>hackwhois ID`", inline=True)
    embed.add_field(name="clear", value=f"`>clear 1-500`", inline=True)
    embed.add_field(name="ban", value=f"`>ban Név/ID indok`", inline=True)
    embed.add_field(name="kick", value=f"`>kick Név/ID indok`", inline=True)
    embed.add_field(name="unban", value=f"`>unban Név/ID`", inline=True)
    embed.set_footer(text="További információkért >info (parancs)")
    embed.set_thumbnail(url=kardos.icon_url)
    await ctx.send(embed=embed)

@commands.guild_only()
@client.group(invoke_without_command=True)
async def info(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Melyik parancs információját szeretnéd megnézni❓",value="`>info parancs`",inline=True)
    embed.set_thumbnail(url=kardos.icon_url)
    await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.guild_only()
@info.command(name="mute")
async def __mute(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Mute parancs információi", value=f"`Némítás`**\n\nEl tudsz némítani felhasználókat a >mute paranccsal\nHasználata: *>mute `Név/ID` idő Indok*\nMegadható időtartam: `s` = `másodperc` / `m` = `perc` / `h` = `óra` / `d` = `nap`\n[Unix másodpercben](https://www.unixtimestamp.com/): 1h = 3600másodperc 1d = 86400másodperc**", inline=True)
    await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.guild_only()
@info.command(name="unmute")
async def __unmute(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Unmute parancs információi", value=f"`Némítás feloldása`**\n\nFel tudsz oldani némításokat a >unmute paranccsal\nHasználata: *>unmute `Név/ID`***", inline=True)
    await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.guild_only()
@info.command(name="whois")
async def __whois(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Whois parancs információi", value=f"`Felhaszálókról való információ lekérés`**\n\nKérj le információkat a szerveren lévő felhasználókról a >whois paranccsal\nHasználata: *>whois `Név/ID`***", inline=True)
    await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.guild_only()
@info.command(name="hackwhois")
async def __hackwhois(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Hackwhois parancs információi", value=f"`Felhaszálókról való információ lekérés`**\n\nKérj le információkat a nem szerveren lévő felhasználókról a >hackwhois paranccsal\nHasználata: *>whois `Név/ID`*\nHa a felhasználó ki lett tiltva, a bot hozzá tesz egy plusz sort!**", inline=True)
    await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.guild_only()
@info.command(name="clear")
async def __clear(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Clear parancs információi", value=f"`Üzenetek törlése`**\n\nTörölj egyszerre több parancsot a >clear paranccsal\nHasználata: *>clear `1-500 szám`*\nHa a szám meghaladja az 500-at, akkor a parancs nem fut le!**", inline=True)
    await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.guild_only()
@info.command(name="ban")
async def __ban(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Ban parancs információi", value=f"`Felhasználó kitiltása`**\n\nTilts ki a rosszindulatú felhasználókat a >ban paranccsal\nHasználata: `>ban Név/ID indok`**", inline=True)
    await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.guild_only()
@info.command(name="kick")
async def __kick(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Kick parancs információi", value=f"`Felhasználó kidobása`**\n\nDobj ki a rosszindulatú felhasználókat a >kick paranccsal\nHasználata: `>kick Név/ID indok`**", inline=True)
    await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.guild_only()
@info.command(name="unban")
async def __unban(ctx):
    kardos = ctx.guild
    embed=discord.Embed(color=0xff9900)
    embed.set_author(name=f"⚔️ KARDOSALAKULAT ⚔️ Command Információs pult ℹ️",icon_url=kardos.icon_url)
    embed.add_field(name="Unban parancs információi", value=f"`Felhasználó kitiltásának feloldása`**\n\nOld fel a felhasználók kitiltását a >unban paranccsal\nHasználata: `>unban Név/ID indok`**", inline=True)
    await ctx.send(embed=embed)


#███████╗██╗░░░██╗███╗░░██╗
#██╔════╝██║░░░██║████╗░██║
#█████╗░░██║░░░██║██╔██╗██║
#██╔══╝░░██║░░░██║██║╚████║
#██║░░░░░╚██████╔╝██║░╚███║
#╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝

@commands.guild_only()
@client.command(name="hitler")
async def hitler(ctx,member:discord.Member = None):
    background = Editor("hitler.png")
    profile_image = await load_image_async(str(member.avatar_url))
    profile = Editor(profile_image).resize((157, 176))
    background.paste(profile, (30, 26))
    file = File(fp=background.image_bytes, filename="hitler.png")
    await ctx.send(file=file)

@commands.guild_only()
@client.command(name="bonk")
async def _bonk(ctx, user: discord.Member, user2: discord.Member = None):
    if user == None:
        user == ctx.author
    if user2 == None:
        user2 = ctx.author
    background = Editor("bonker.png")
    profile_image = await load_image_async(str(user.avatar_url))
    profile = Editor(profile_image).resize((329, 256))
    background.paste(profile, (255, 117))
    profile_image = await load_image_async(str(user2.avatar_url))
    profile = Editor(profile_image).resize((287, 252))
    background.paste(profile, (806, 511))
    file = File(fp=background.image_bytes, filename="bonker.png")
    await ctx.send(file=file)

@commands.guild_only()
@client.command(name="fiveman")
async def _fiveman(ctx,member:discord.User = None):
    if not member:
        member = ctx.author
    background = Editor("five.png")
    profile_image = await load_image_async(str(member.avatar_url))
    profile = Editor(profile_image).resize((240, 234))
    background.paste(profile, (428, 260))
    file = File(fp=background.image_bytes, filename="five.png")
    await ctx.send(file=file)

@commands.guild_only()
@client.command(name="slap")
async def _slap(ctx, user: discord.Member, user2: discord.Member = None):
    if user == None:
        user == ctx.author
    if user2 == None:
        user2 = ctx.author
    background = Editor("batman.png")
    profile_image = await load_image_async(str(user2.avatar_url))
    profile = Editor(profile_image).resize((291, 251))
    background.paste(profile, (809, 321))
    profile_image = await load_image_async(str(user.avatar_url))
    profile = Editor(profile_image).resize((291, 251))
    background.paste(profile, (497, 115))
    file = File(fp=background.image_bytes, filename="batman.png")
    await ctx.send(file=file)

@commands.guild_only()
@client.command(name="hotfood")
async def _hotfood(ctx,member:discord.User = None):
    if not member:
        member = ctx.author
    background = Editor("hot.png")
    profile_image = await load_image_async(str(member.avatar_url))
    profile = Editor(profile_image).resize((483, 426))
    background.paste(profile, (53, 126))
    file = File(fp=background.image_bytes, filename="hot.png")
    await ctx.send(file=file)

@commands.guild_only()
@client.command(aliases=['gay-scanner', 'gayscanner','homo','gayrate','Gayrate','Gay-scanner'])
async def gay_scanner(ctx, *, user: str = None):
        if not user:
            user = ctx.author.name
            
        await ctx.trigger_typing()

        gayness = randint(0, 100)

        if gayness <= 33:
            gayStatus = choice(["No homo",
                                "Straight-ish",
                                "No homo bro",
                                "Girl-kisser",
                                "Hella straight",
                                "Small amount of Homo detected."])
            gayColor = 0xFFC0CB
        elif 33 < gayness < 66:
            gayStatus = choice(["Possible homo",
                                "My gay-sensor is picking something up",
                                "I can't tell if the socks are on or off",
                                "Gay-ish",
                                "Looking a bit homo",
                                "lol half  g a y",
                                "safely in between for now",
                                "50:50"])
            gayColor = 0xFF69B4
        else:
            gayStatus = choice([
                                "Homo Alert",
                                "My gay-sensor is off the charts",
                                "stinky gay",
                                "big gay",
                                "hella gay",
                                "Yeah, gay","Why are you gay?"])
            gayColor = 0xFF00FF

        meter = "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"

        if gayness <= 10:
            meter = "🏳‍🌈⬛⬛⬛⬛⬛⬛⬛⬛⬛"
        elif gayness <= 20:
            meter = "🏳‍🌈🏳‍🌈⬛⬛⬛⬛⬛⬛⬛⬛"
        elif gayness <= 30:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛⬛⬛⬛⬛"
        elif gayness <= 40:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛⬛⬛⬛"
        elif gayness <= 50:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛⬛⬛"
        elif gayness <= 60:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛⬛"
        elif gayness <= 70:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛⬛"
        elif gayness <= 80:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛⬛"
        elif gayness <= 90:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈⬛"
        else:
            meter = "🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈🏳‍🌈"

        emb = discord.Embed(
            description=f"Gayness for **{user}**", color=gayColor)
        emb.add_field(name="Gayness:", value=f"{gayness}% gay", inline=False)
        emb.add_field(name="Comment:",
                      value=f"{gayStatus}", inline=False)
        emb.add_field(name="Gay Meter:", value=meter, inline=False)
        emb.set_author(name="Gay Meter",
                       icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/ICA_flag.svg/2000px-ICA_flag.svg.png")
        await ctx.reply(embed=emb)

#███╗░░░███╗░█████╗░██████╗░███████╗██████╗░███████╗██████╗░░█████╗░░█████╗░██╗░█████╗░
#████╗░████║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
#██╔████╔██║██║░░██║██║░░██║█████╗░░██████╔╝█████╗░░██████╔╝███████║██║░░╚═╝██║██║░░██║
#██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░██╔══██╗██╔══╝░░██╔══██╗██╔══██║██║░░██╗██║██║░░██║
#██║░╚═╝░██║╚█████╔╝██████╔╝███████╗██║░░██║███████╗██║░░██║██║░░██║╚█████╔╝██║╚█████╔╝
#╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░

@commands.guild_only()
@client.command(name="mute")
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member,time,*,reason="Nincs indok megadva"):
    a=client.get_channel(Vizsgálati Napló ID)
    reason = "".join(reason)
    muted_role=discord.utils.get(ctx.guild.roles, id=Mute Rang ID)
    time_convert = {"s":1, "m":60, "h":3600,"d":86400}
    tempmute= int(time[0]) * time_convert[time[-1]]
    await member.add_roles(muted_role)
    embed = discord.Embed(description= f"✅ Anonymous Némítva", color=discord.Color.green(),timestamp=ctx.message.created_at)
    embed2=discord.Embed(color=0x9999ff,timestamp=ctx.message.created_at)
    embed2.set_author(name=f"{member} Némítva", icon_url=member.avatar_url)
    embed2.add_field(name=f"{member} Némítva!",value=f"\nIdő: {time}\nIndok: {reason}\nModerátor: {ctx.author.mention}")
    embed2.set_thumbnail(url=member.avatar_url)
    embed2.set_footer(text=member.id)
    await ctx.send(embed=embed)
    await a.send(embed=embed2)
    embed4=discord.Embed(color=0x9999ff,timestamp=ctx.message.created_at)
    embed4.set_author(name=f"{member}", icon_url=member.avatar_url)
    embed4.set_thumbnail(url=member.avatar_url)
    embed4.add_field(name=f"{member} Némítva lettél itt: {ctx.guild.name}",value=f"\nIdő: {time}\nIndok: {reason}")
    embed4.set_footer(text=member.id)
    await member.send(embed=embed4)
    await asyncio.sleep(tempmute)
    await member.remove_roles(muted_role)
    embed3=discord.Embed(color=0x00ff99,timestamp=ctx.message.created_at)
    embed3.set_author(name=f"{member}", icon_url=member.avatar_url)
    embed3.set_thumbnail(url=member.avatar_url)
    embed3.add_field(name=f"{member} némítása lejárt!",value=f"\nIndok: {reason}\nModerátor: {ctx.author.mention}")
    embed3.set_footer(text=member.id)
    await a.send(embed=embed3)
    embed5=discord.Embed(color=0x9999ff,timestamp=ctx.message.created_at)
    embed5.set_author(name=f"{member}", icon_url=member.avatar_url)
    embed5.set_thumbnail(url=member.avatar_url)
    embed5.add_field(name=f"{member} Nemításod lejárt itt: {ctx.guild.name}",value="\u200b")
    embed5.set_footer(text=member.id)
    await member.send(embed=embed4)
    print(f"{member} muteolva lett általa: {ctx.author} ennyi időre: {time} | {reason} - indokkal ekkor: {x.today():%x | %X}")

@commands.guild_only()
@client.command(name="unmute")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, *,member: discord.Member):
    a=client.get_channel(Vizsgálati Napló ID)
    muted_role=discord.utils.get(ctx.guild.roles, id="Rang ID")
    embed=discord.Embed(color=0x00ff99,timestamp=ctx.message.created_at)
    embed.add_field(name=f"{member} némítása feloldva!",value="\u200b")
    await ctx.send(embed=embed)
    embed1=discord.Embed(color=0x00ff99,timestamp=ctx.message.created_at)
    embed1.add_field(name=f"{member} némítása feloldva!",value=f"Moderátor: {ctx.author.mention}")
    embed1.set_thumbnail(url=member.avatar_url)
    embed1.set_footer(text=member.id)
    await ctx.send(embed=embed1)
    await member.remove_roles(muted_role)
    print(f"{member} unmuteolva lett általa: {ctx.author} ekkor: {x.today():%x / %X}")

@commands.guild_only()
@client.command(aliases=["whois"])
async def userinfo(ctx, *,member:discord.User):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role.mention for role in member.roles[1:]]  # don't get @everyone
    roles.append('@everyone')
    embed = discord.Embed(color=0x669999, timestamp=ctx.message.created_at,
                          title=f"Felhasználó információk - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Lekérte {ctx.message.author}",
				icon_url=f"{ctx.message.author.avatar_url}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Nickname:", value=member.display_name)

    embed.add_field(name="Létrehozva:", value=f"<t:{int(round(member.created_at.timestamp()))}:R>",inline=False)
    embed.add_field(name="Csatlakozott:", value=f"<t:{int(round(member.joined_at.timestamp()))}:R>",inline=True)

    embed.add_field(name=f"Rangok: [{len(roles)}]", value=" ".join(roles),inline=False)
    embed.add_field(name="Legnagyobb rang:", value=member.top_role.mention)
    await ctx.send(embed=embed)

@commands.guild_only()
@client.command(aliases=["hackwhois"])
async def hackuserinfo(ctx, *, member:discord.User):
        bans = await ctx.guild.bans() #Getting a list of all ban entries
        lst = [ban_e for ban_e in await ctx.guild.bans() if ban_e.user.id == member.id]
        embed = discord.Embed(color=0x669999, timestamp=ctx.message.created_at,title=f"Felhasználó információk - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Lekérte {ctx.message.author}",
                        icon_url=f"{ctx.message.author.avatar_url}")
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Nickname:", value=member.display_name)
        embed.add_field(name="Létrehozva:", value=f"<t:{int(round(member.created_at.timestamp()))}:R>",inline=False)
        if lst != []:
              ban_reason = lst[0].reason
              embed.add_field(name="Ban info:",value=ban_reason)
        await ctx.send(embed=embed)
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
@client.command(aliases = ["del", "pr", "prune","clean","clear"])
async def purge(ctx, amount: int = None, member: libneko.converters.InsensitiveMemberConverter = None):
        try:
            if amount <= 500:
                if member is None:
                    await ctx.channel.purge(limit = amount + 1)
                    print(f"{ctx.author} kitörölt ennyi üzenetet: {amount} ekkor: {x.today():%x / %X} itt: {ctx.channel.name}")
                else:
                    async for message in ctx.channel.history(limit = amount + 2):
                        if message.author is member:
                            await message.delete()
                            print(f"{ctx.author} kitörölt ennyi üzenetet: {amount} ekkor: {x.today():%x / %X} itt: {ctx.channel.name}")
                            
            else:
                embed=discord.Embed(description="❌ Elérted a maximumot. Egy időben csak 500 üzenetet törölhetsz")
                await ctx.reply(embed=embed)
        except:
            embed = discord.Embed(title=f"", color=0x34568B, description=f"")
            embed.add_field(name="Helytelen parancs, próbáld így:", value=">clear `(mennyiség)`", inline=True)
            embed.add_field(name="Mennyiség:", value="1-500 közti számok", inline=False)
            await ctx.reply(embed=embed)
            

@commands.guild_only()
@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, member: discord.User, *, reason="indok nincs megadva"):
            if member == None or member == ctx.message.author:
                await ctx.channel.send("Nem bannolhatod magad")
                return
            else:
                a=client.get_channel("Vizsgálati napló ID")
                reason = "".join(reason)
                embed = discord.Embed(title=f"Anonymous#0000 Ki lett tiltva",color=0xccffff, timestamp=ctx.message.created_at)
                embed.set_thumbnail(url="https://o.remove.bg/downloads/32d1934c-d5b1-499d-a943-424772808a77/image-removebg-preview.png")
                embed1 = discord.Embed(title=f"{member} Ki lett tiltva",description=f"\n Moderátor: {ctx.author.mention}\nIndok: {reason}",color=0x6699ff, timestamp=ctx.message.created_at)
                embed1.set_thumbnail(url=member.avatar_url)
                embed1.set_footer(icon_url=member.avatar_url, text=f"{member} | {member.id}")
                await a.send(embed=embed1)
                await ctx.send(embed=embed)
                await asyncio.sleep(0.1)
                await ctx.guild.ban(member, reason=reason)
                print(f"{member} bannolva lett {ctx.author} által {reason} indokkal ekkor: {x.today():%x / %X}")

@commands.guild_only()
@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member: discord.User, *, reason="indok nincs megadva"):
            if member == None or member == ctx.message.author:
                await ctx.channel.send("Nem kickelheted magad.")
                return
            else:
                a=client.get_channel("Vizsgálati napló ID")
                reason = "".join(reason)
                embed = discord.Embed(title=f"{member} Ki lett rúgva",description=f"\nModerátor:{ctx.author.mention}\nIndok: {reason}",color=0x34568B, timestamp=ctx.message.created_at)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(icon_url=member.avatar_url, text=f"{member.name} | {member.id}")
                embed1 = discord.Embed(title=f"{member} Ki lett rúgva",description=f"\n Moderátor: {ctx.author.mention}\nIndok: {reason}",color=0x6699ff, timestamp=ctx.message.created_at)
                embed1.set_thumbnail(url=member.avatar_url)
                embed1.set_footer(icon_url=member.avatar_url, text=f"{member} | {member.id}")
                await a.send(embed=embed1)
                await ctx.send(embed=embed)
                await asyncio.sleep(0.1)
                await ctx.guild.kick(member, reason=reason)
                print(f"{member} kickelve lett általa: {ctx.author} '{reason} ' indokkal ekkor: {x.today():%x / %X}")

@commands.guild_only()
@client.command(name='unban')
async def _unban(ctx, *,user:discord.User):
    a=client.get_channel("Vizsgálati napló ID")
    await ctx.guild.unban(user)
    embed = discord.Embed(title="Feloldva! 🤝", description=f'{user.mention} unbannolva!', color=0x00ccff,timestamp=ctx.message.created_at)
    embed.set_footer(text="Kitiltását feloldotta: {}".format(ctx.author.display_name))
    embed.set_footer(icon_url=user.avatar_url, text=f"ID: {user.id}")
    embed1 = discord.Embed(title=f"{user} Kitiltása fel lett oldva", color=0x66ff66, timestamp=ctx.message.created_at)
    embed1.add_field(name="\u200b", value=f"Moderátor:{ctx.author.mention}")
    embed1.set_footer(icon_url=user.avatar_url, text=f"{user} | {user.id}")
    embed1.set_thumbnail(url=user.avatar_url)
    await a.send(embed=embed1)
    await ctx.send(embed=embed)
    print(f"{user} Unbannolva általa: {ctx.author} ekkor: {x.today():%x / %X}")

#██╗░░░░░░█████╗░░██████╗░
#██║░░░░░██╔══██╗██╔════╝░
#██║░░░░░██║░░██║██║░░██╗░
#██║░░░░░██║░░██║██║░░╚██╗
#███████╗╚█████╔╝╚██████╔╝
#╚══════╝░╚════╝░░╚═════╝░

@client.event
async def on_message_delete(message):
        channel = client.get_channel(Vizsgálati Napló ID)
        embed = discord.Embed(description = f"Üzenet visszavonsára került itt: {message.channel.mention}\n\n**Üzenet:**\n{message.content}", color = 0xff3333, timestamp = datetime.datetime.utcnow())
        embed.set_author(name=f"{message.author}", icon_url=message.author.avatar_url)
        embed.set_footer(text=message.author.id)
        await channel.send(embed = embed)
        print(f"{message.author} törölte üzenetét itt: {message.channel} Üzenet: {message.content} ekkor: {x.today():%x / %X}")

@client.event
async def on_member_ban(guild, user):
        ban = "<:banned:967552305618616340>"
        a=client.get_channel(Vizsgálati Napló ID)
        embed = discord.Embed(description=f"{user} Bannolva lett! {ban}", color=0xff0000,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(icon_url=f"{user.avatar_url}", text=user.id)
        await a.send(embed=embed)
        print(f"{user} bannolva lett ekkor: {x.today():%x / %X}")

@client.event
async def on_member_unban(guild, user):
        ban = "<:pipa:979829575594962954>"
        a=client.get_channel(Vizsgálati Napló ID)
        embed = discord.Embed(description=f"{user} Unbannolva lett! {ban}", color=0x4dff4d,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(icon_url=f"{user.avatar_url}", text=user.id)
        await a.send(embed=embed)
        print(f"{user} unbannolva lett! ekkor:{x.today():%x / %X}")

@client.event
async def on_member_remove(user):
        leaved = "<:leaved:967552281115500554>"
        b=client.get_channel(Kilépő csatorna ID)
        a=client.get_channel(Vizsgálati Napló ID)
        embed = discord.Embed(description=f"{user.mention} Elhagyta a szervert\nCsatlakozott: <t:{int(round(user.joined_at.timestamp()))}:R>", color=0xff3333,timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=user.id)
        embed.set_author(name=f"{user} Kilépett", icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        await b.send(f"**{user}** -tól/től elvették a számítót szerencsére 😀👍")
        await a.send(embed=embed)
        print(f"{user} kilépett. ekkor: {x.today():%x / %X}")

#███████╗██╗░░░██╗███████╗███╗░░██╗████████╗███████╗██╗░░██╗
#██╔════╝██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔════╝██║░██╔╝
#█████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░█████╗░░█████═╝░
#██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░██╔═██╗░
#███████╗░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░███████╗██║░╚██╗
#╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

@client.event
async def on_raw_reaction_add(payload):
    message_id=payload.message_id
    if message_id == '''Ide az Üzenet IDje (töröld ki a 3x3-as commentet)''':
        guild_id=payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.id==('''Ide az Üzenet IDje (töröld ki a 3x3-as commentet)'''):
            role = guild.get_role('''Ide az Üzenet IDje (töröld ki a 3x3-as commentet)''')
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
@client.event
async def on_raw_reaction_remove(payload):
    message_id=payload.message_id
    if message_id == '''Ide az Üzenet IDje (töröld ki a 3x3-as commentet)''':
        guild_id=payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.id==('''Ide az Üzenet IDje (töröld ki a 3x3-as commentet)'''):
            role = guild.get_role('''Ide az Üzenet IDje (töröld ki a 3x3-as commentet)''')
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

#░█████╗░██╗░░░██╗████████╗░█████╗░  ███╗░░░███╗░█████╗░██████╗░███████╗██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
#██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
#███████║██║░░░██║░░░██║░░░██║░░██║  ██╔████╔██║██║░░██║██║░░██║█████╗░░██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
#██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
#██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

censured=["kys","KYS","KillYourSelf","killyourself","kjs","k-y-s","kYS","KyS","kyS","https://discord.gg/"]

@client.event
async def on_message(message):
    for word in censured:
        if word in message.content:
            await message.delete()
            print(f"A bot törölte {message.author} üzenetét, mivel tiltott szót tartalmazott, vagy meghívót")


#░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗██████╗░
#░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝██╔══██╗
#░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░██████╔╝
#░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗
#░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗██║░░██║
#░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝

invites = {}
last = ""
guild_id=(Szerver ID)
logs_channel=(Vizsgálati Napló ID)
async def fetch():
    global last
    global invites
    await client.wait_until_ready()
    gld = client.get_guild(int(guild_id))
    logs = client.get_channel(int(logs_channel))
    while True:
        invs = await gld.invites()
        tmp = []
        for i in invs:
            for s in invites:
                if s[0] == i.code:
                    if int(i.uses) > s[1]:
                        usr = gld.get_member(int(last))
                        eme = discord.Embed(color=0x03d692)
                        eme.set_author(name=f"{usr} csatlakozott a szerverhez", icon_url=usr.avatar_url)
                        eme.set_footer(text=f"{usr.id}")
                        eme.timestamp = usr.joined_at
                        eme.add_field(name="Létrehozva:", value=f'<t:{int(round(usr.created_at.timestamp()))}:R>\n**Csatlakozott:**\n<t:{int(round(usr.joined_at.timestamp()))}:R>',inline=False)
                        eme.add_field(name="Használt meghívó",value=f"Inviter: {i.inviter.mention} | {i.inviter} ID:`{i.inviter.id}` \nKód: `{i.code}` |  Használva: {i.uses}x", inline=False)
                        await logs.send(embed=eme)
            tmp.append(tuple((i.code, i.uses)))
        invites = tmp
        await asyncio.sleep(4)

@client.event
async def on_member_join(member):
    global last
    last = str(member.id)
    embed=discord.Embed(title="Üdvözöllek a Kardosalakulaton!", description="Mielőtt hozzáférést kapnál a szerverhez, először meg kell tenned a következő lépéseket:\n- Fogadd el és olvasd is el a szabályokat!\n- Ha ez megvan, be kell majd mutatkoznod a #✍bemutatkozás✍ csatornán!\n\nHa a hitelesítés sikerült, mielőtt bármihez is hozzá kezdenél, alaposan olvasd át a szabályzatot és tartsd is be azt!\n\n⚔️ Jó szórakozást! ⚔️", color=0xecac22)
    embed.set_thumbnail(url=member.guild.icon_url)
    await member.send(embed=embed)
    channel = client.get_channel(Üdvözlő csatorna ID)
    pos = sum(m.joined_at < member.joined_at for m in member.guild.members if m.joined_at is not None)
    if pos == 1:
        te = "."
    elif pos == 2:
        te = "."
    elif pos == 3:
        te = "."
    else: te = "."
    background = Editor("cappy.png")
    profile_image = await load_image_async(str(member.avatar_url))
    profile = Editor(profile_image).resize((450, 450)).circle_image()
    poppins = Font.poppins(size=100, variant="bold")
    poppins_small = Font.poppins(size=60, variant="bold")
    background.paste(profile, (760, 275))
    background.ellipse((760, 275), 450, 450, outline="white", stroke_width=7)
    background.text((960, 720), f"Üdvözöllek a Kardosalakulaton", color="white", font=poppins, align="center")
    background.text((960, 850), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
    background.text((960, 920), f"te vagy a(z) {pos}{te} tag", color="#0BE7F5", font=poppins_small, align="center")
    file = File(fp=background.image_bytes, filename="cappy.png")
    await channel.send(f"Üdvözlünk {member.mention}, mostantól hivatalosan is hetero vagy! :D")
    await channel.send(file=file)
    print(f"{member} csatlakozott ekkor: {x.today():%x / %X}")

#███████╗██████╗░██████╗░░█████╗░██████╗░  ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
#██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
#█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝  ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
#██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗  ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
#███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║  ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
#╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝
@commands.guild_only()
@mute.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"", color=0x34568B, description=f"Parancs hiba")
        embed.add_field(name="Helytelen Mute használat, próbáld meg így:", value=f">mute `(felhasználó)` `(idő)` `(indok)`",
                        inline=False)
        embed.add_field(name="\u200b",
                        value=f"Paraméterek:\n`Felhasználó:` *Felhasználó említés (@user) / ID* \n`Idő:` *Idő tartam angol betű végződéssel (s/m/h/d)*\n`Indok:` *Szöveg*\n\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=f"Parancs hiba", description="Nem rendelkezel a megfelelő jogokkal..",
                              color=0x34568B, )
        embed.add_field(name="\u200b",
                        value=f"Követelt engedély:\nFelhasználó kidobása\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
@commands.guild_only()
@ban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"", color=0x34568B, description=f"Parancs hiba")
        embed.add_field(name="Helytelen Ban használat, próbáld meg így:", value=f">ban `(felhasználó)` `(indok)`",
                        inline=False)
        embed.add_field(name="\u200b",
                        value=f"Paraméterek:\n`Felhasználó:` *Felhasználó említés (@user) / ID*\n`Indok:` *Szöveg*\n\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=f"Parancs hiba", description="Nem rendelkezel a megfelelő jogokkal..",
                              color=0x34568B, )
        embed.add_field(name="\u200b",
                        value=f"Követelt engedély:\nFelhasználó kitiltása\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
@commands.guild_only()
@kick.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"", color=0x34568B, description=f"Parancs hiba")
        embed.add_field(name="Helytelen Kick használat, próbáld meg így:", value=f">kick `(felhasználó)` `(indok)`",
                        inline=False)
        embed.add_field(name="\u200b",
                        value=f"Paraméterek:\n`Felhasználó:` *Felhasználó említés (@user) / ID* \n`Indok:` *Szöveg*\n\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=f"Parancs hiba", description="Nem rendelkezel a megfelelő jogokkal..",
                              color=0x34568B, )
        embed.add_field(name="\u200b",
                        value=f"Követelt engedély:\nFelhasználó kidobása\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
@commands.guild_only()
@_unban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"", color=0x34568B, description=f"Parancs hiba")
        embed.add_field(name="Helytelen Mute használat, próbáld meg így:", value=f">unban `(felhasználó)`",
                        inline=False)
        embed.add_field(name="\u200b",
                        value=f"Paraméterek:\n`Felhasználó:` *Felhasználó ID*\n\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=f"Parancs hiba", description="Nem rendelkezel a megfelelő jogokkal..",
                              color=0x34568B, )
        embed.add_field(name="\u200b",
                        value=f"Követelt engedély:\nFelhasználó kitiltása\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
@commands.guild_only()
@unmute.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"", color=0x34568B, description=f"Parancs hiba")
        embed.add_field(name="Helytelen unmute használat, próbáld meg így:", value=f">unmute `(felhasználó)`",
                        inline=False)
        embed.add_field(name="\u200b",
                        value=f"Paraméterek:\n`Felhasználó:` *Felhasználó említés (@user) / ID* \n\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=f"Parancs hiba", description="Nem rendelkezel a megfelelő jogokkal..",
                              color=0x34568B, )
        embed.add_field(name="\u200b",
                        value=f"Követelt engedély:\nFelhasználó kidobása\nHa a probléma nem oldódott meg, keresd a fejlesztőt.",
                        inline=False)
        await ctx.send(embed=embed)

@commands.guild_only()
@_moderacio.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Úgy látszik, hogy te nem férsz hozzá a ⚔️ KARDOSALAKULAT ⚔️ Admin paneljéhez.")

client.loop.create_task(fetch())
client.run("Token")
