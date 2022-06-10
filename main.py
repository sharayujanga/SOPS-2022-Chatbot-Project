from discord.ext import commands
import os
import random
bot = commands.Bot(command_prefix='!')

bot.list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '^', '*', '@']

bot.passwordList = []
@bot.command( )
async def hello(ctx):
  await ctx.send("hello " + ctx.author.display_name)
@bot.command()
async def char(ctx, *, number):
  num = int(number)
  while num > 0:
    bot.passwordList.append(random.choice(bot.list))
    print(bot.passwordList)
    num = num - 1
    
  for x in bot.passwordList:
    a = (" ".join(str(x) for x in bot.passwordList))
  await ctx.send(a)

password = os.environ['password']
bot.run(password)