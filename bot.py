import discord
from discord.ext import commands
import random
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
client= commands.Bot(command_prefix="^")


game = ['rock','paper','scissors']
reactionwon = ['gottee!','ez bwoi','bruh, I won ;-;']
reactionlost = ['wtf how!','how did you..','sheer luck mate!']

@client.event
async def on_ready():
    print("Bot Ready for use")

# driver = webdriver.Chrome()
# driver.get('https://www.cleverbot.com')
# driver.find_element_by_id('noteb').click()

# def get_response(message):
#     driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(message + Keys.RETURN)
#     while True:
#         try:
#             driver.find_element_by_xpath('//*[@id="snipTextIcon"]')
#             break
#         except:
#             continue
#     response = driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
#     return response

#     async def on_message(self, message):
#         if message.author != self.user:
#             reponse = get_response(message.content)
#             await message.channel.send({reponse})


@client.command(aliases=['hi','Hi','Hello'])
async def hello(ctx):
    await ctx.send("Hi")

@client.command(aliases=['c','C','delete','Clear','Delete'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 2):
    await ctx.channel.purge(limit = amount)
    
@client.command(aliases=['k','K','Kick','throw'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason="Because you suck!"):
    await ctx.send(f"{member}has been kicked for :"+"\n"+"||"+reason+"||")
    await member.kick(reason = reason)

@client.command(aliases=['b','B','Ban'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason="Because you suck!"):
    await ctx.send(f"{member}banned for :"+"\n"+"||"+reason+"||")
    await member.ban(reason = reason)

@client.command(aliases = ['ub','UB','Unban'])
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name,member_disc=member.split("#")

    for banned_entry in banned_users:
        user = banned_entry.user
        if(user.name,user.discriminator) == (member_name,member_disc):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} has been unbanned")
            return
    await ctx.send(member+"not found")

@client.command(aliases = ['m','M','Muted'])
@commands.has_permissions(kick_members = True)
async def mute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(837364188959473714)
    await member.add_roles(muted_role)
    await ctx.send(member.mention+"has been muted")
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg=message.content
    if msg.startswith('^rock'):
        choice = random.choice(game)
        await message.channel.send(choice)
        if(choice=="paper"):
            await message.channel.send(random.choice(reactionwon))
        elif(choice=="scissors"):
            await message.channel.send(random.choice(reactionlost))
        else:
            await message.channel.send("It\'s a draw bruh!")

    if msg.startswith('^paper'):
        choice = random.choice(game)
        await message.channel.send(choice)
        if(choice=="scissors"):
            await message.channel.send(random.choice(reactionwon))
        elif(choice=="rock"):
            await message.channel.send(random.choice(reactionlost))
        else:
            await message.channel.send("It\'s a draw bruh!")

    if msg.startswith('^scissors'):
        choice = random.choice(game)
        await message.channel.send(choice)
        if(choice=="rock"):
            await message.channel.send(random.choice(reactionwon))
        elif(choice=="paper"):
            await message.channel.send(random.choice(reactionlost))
        else:
            await message.channel.send("It\'s a draw bruh!")
    await client.process_commands(message)



client.run("ODM3MDIzMTUxMDM2Njk0NjIw.YImgjg.51dlHAhsoDm1Gt1plbHXaec0qiw")