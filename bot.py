import discord
from discord.ext import commands
import random
# from transformers import AutoModelWithLMHead, AutoTokenizer
# import torch
client= commands.Bot(command_prefix="^")


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
# model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-small")

game = ['rock','paper','scissors']
reactionwon = ['gottee!','ez bwoi','bruh, I won ;-;']
reactionlost = ['wtf how!','how did you..','sheer luck mate!']


@client.event
async def on_ready():
    print("Bot Ready for use")


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
    await ctx.send(f"{member} has been kicked for :"+"\n"+"||"+reason+"||")
    await member.kick(reason = reason)

@client.command(aliases=['b','B','Ban'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason="Because you suck!"):
    await ctx.send(f"{member} banned for :"+"\n"+"||"+reason+"||")
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
    muted_role = ctx.guild.get_role(842301615519825922)
    await member.add_roles(muted_role)
    await ctx.send(member.mention+" has been muted")


# @client.event
# async def on_message(self, message):
#     if message.author == client.user:
#         return
#     msg=message.content
#     channel = client.get_channel(842310690635120640)
#     bot_input_ids = tokenizer.encode(msg + tokenizer.eos_token, return_tensors='pt')
#     chat_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
#     messagebot = tokenizer.decode(chat_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
#     tosend = "no comment" if messagebot == "" else messagebot
#     await message.channel.send(tosend)    
    

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



client.run("ODM3MDIzMTUxMDM2Njk0NjIw.YImgjg.nO08voZ229wsQ-bK4IYxsDxzP0A")