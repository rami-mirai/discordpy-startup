from discord.ext import commands
import os


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_message(message):
   if message.author.bot:
       return
   if message.content == ('$mjoha'):
       await message.channel.send("<@588392127919161357>"+'おはよう:heart:')
   if message.content == ('$mjlove'):
       await message.channel.send("<@588392127919161357>"+'大好き:heart:')
   if message.content == ('$mjbut'):
       await message.channel.send("<@588392127919161357>"+'嫌い！:rage: ')
   if message.content == ('$mjwakeup'):
       await message.channel.send("<@588392127919161357>"+'起きて:heart:')
   if message.content == ('$mjyabai'):
       await message.channel.send("<@588392127919161357>"+'含み損すごい:heart:')
   if message.content == ('$mjome'):
       await message.channel.send("<@588392127919161357>"+'大好き:heart:')
   if message.content == ('$uwaki'):
       await message.channel.send("<@588392127919161357>"+'あっちに逝こうか:heart:')
   if message.content == ('$mjsongiri'):
       await message.channel.send("<@588392127919161357>"+'残念損切り:heart:')
   if message.content == ('おめでとう'):
       await message.channel.send('私も嬉しい:heart:')
   if message.content == ('MJさんは？'):
       await message.channel.send('ドイツ:heart:')
   if message.content == ('利確どこ？'):
       await message.channel.send('私も知りたい:heart:')
   if message.content == ("<@588392127919161357>"):
           await message.channel.send("<@588392127919161357>" +'呼んでるわよ？:heart:')
   if message.content == (":99_gbpjpy:"):
       await message.channel.send("<@588392127919161357>" +':99_gbpjpy: のおーだ知りたいなぁ:heart:')
   if message.content == (":99_usdjpy:"):
       await message.channel.send("<@588392127919161357>" +':99_usdjpy: のおーだ知りたいなぁ:heart:')
   if message.content == ('れんかぶす'):
       await message.channel.send("<@588392127919161357>"+'はかっこいいよ:heart:')
   if message.content == ('てんが利確どこ？'):
       await message.channel.send("<@522237932606717968>"+'早よ言え:heart:')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
