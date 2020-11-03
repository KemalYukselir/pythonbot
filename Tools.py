
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import re

mainbot = commands.Bot(command_prefix = "-")




mainbot.remove_command("help")

channel_id = 717262662215532620

test_channel = 688447908613324867 ### Test 



help_message = """
```

Say 'stop' to stop the bot if anything goes wrong

1) -b 

* converts binary to text and automatically puts it into a discord invite form for users to join
* Automatically adds the code after https://discord.gg/ to make it useful for autojoiners.
* Removes the ' https://discord.gg/ ' if its accidentally put in the code after -b so there is no duplicate.

2) .b

* Fixes the text that is backwards 
* Automatically removes whitespace
* Automatically adds the code after https://discord.gg/ to make it useful for autojoiners.
* Removes the ' https://discord.gg/ ' if its accidentally put in the code after .b so there is no duplicate
* Also handles ' https://discord.gg/ ' if its backwards e.g ' olleh/gg.drocsid//:sptth ' 

3) Auto Detection 

* The bot waits for anything that begins with 'https://discord.gg/' even if theres whitespace.
* Automatically removes whitespace on the 'https://discord.gg/' part
* Doesn't remove symbols on the 'https://discord.gg/' part
* Automatically removes whitespace on the discord invite code after the 'https://discord.gg/' part
* Automatically removes symbols on the discord invite code after the 'https://discord.gg/' part

4) -Monitor

* Bot waits for a discord code
* Removes whitespace and symbols from the code 
* Automatically adds it to the end of 'https://discord.gg/' to make it joinable 
* Handles 'https://discord.gg/' if its accidently put into the code after -monitor to avoid duplication.
```
"""


@mainbot.event
@commands.guild_only()
async def on_message(message):

    if message.content.lower().startswith('stop'):
        print("bot stoped")
        return

    ### Ignore. This bit is for the automatic detection

    auto_message = str(message.content).replace(" ","")
    

    if message.content.startswith('.b'):
        the_message = str(message.content).replace(" ","").replace(".b ","").replace(".b","").replace("https://discord.gg/","").replace("/gg.drocsid//:sptth","").replace("/gg.drocsid","")
        if the_message == "":
            pass

        else:
            channel = message.channel
            backwards = str(the_message[::-1])

            await channel.send("https://discord.gg/" + backwards)




    if auto_message.lower().startswith('https://discord.gg/') or auto_message.lower().startswith('discord.gg/'):
        
        #auto_message_no_symbol = re.sub("[^A-Za-z0-9]+","",auto_message)

        if message.author == mainbot.user: 
            return
        
        else:
            channel = message.channel

            sent_message = str(message.content)
            sent_message = sent_message.replace(" ","").replace("https://discord.gg/","").replace('discord.gg/',"")

            sent_message_no_symbol = re.sub("[^A-Za-z0-9]+","",sent_message)
            
            

            await channel.send("https://discord.gg/" + sent_message_no_symbol)

            return


    elif message.content.startswith('-help'):
        channel = message.channel

        await channel.send(help_message)

    await mainbot.process_commands(message)
        



@mainbot.command()
@commands.guild_only()
async def i(ctx,*,message):
    message = str(message).replace(" ","").replace("https://discord.gg/","")
    message = re.sub("[^A-Za-z0-9]+","",message)
     
    await ctx.send("https://discord.gg/" + message)    

@mainbot.command()
@commands.guild_only()
async def link(ctx):
    return

    await ctx.send("Please provide the password link (type 'cancel' to stop everything)")

    # This will make sure that the response will only be registered if the following
    # conditions are met:

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

    msg = await mainbot.wait_for("message", check=check)


    await ctx.send("Awaiting password...")

    msg2 = await mainbot.wait_for("message", check=check)
    msg2 = str(msg2.content)

    if msg2 == "cancel":
        return


    msg2_no_whitespace = msg2.replace(" ","")

    msg2_no_symbols = re.sub("[^A-Za-z0-9]+","",msg2)

    await ctx.send("Orignal " + msg.content + msg2 + "\n" + "removed whitespace " + msg.content + msg2_no_whitespace + "\n" + "removed whitepsace + symbols " + msg.content + msg2_no_symbols)

    #await ctx.send("hello" + "\n" + "hi")



@mainbot.command()
@commands.guild_only()
async def monitor(ctx):

    def check(msg):

        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

    checker = await mainbot.wait_for("message", check=check)
    x = True

    if bool(x) == True:

        while True:

            await ctx.send("Awaiting discord code")

            # This will make sure that the response will only be registered if the following
            # conditions are met:


            msg = await mainbot.wait_for("message", check=check)

            msg_code = str(msg.content).replace(" ","").replace("https://discord.gg/","").replace("discord.gg/","")
            msg_code_no_symbol = re.sub("[^A-Za-z0-9]+","",msg_code)


            await ctx.send("https://discord.gg/" + msg_code_no_symbol)

    #await ctx.send("hello" + "\n" + "hi")


########## Binary converter 
@mainbot.command()
@commands.guild_only()
async def b(ctx,*,message):


    binary_values = message.split()

    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
        ascii_string = str(ascii_string).replace(" ","")
        ascii_string = ascii_string.replace("https://discord.gg/"," ")
        
    await ctx.send("https://discord.gg/" + ascii_string)

        
token_RR = "NzA4MDAxODIwMTQ3OTc0MTk0.XrRAEw.KGPrssGTL3m48RgvHMRCNkJVi9U"
token_test = "NzE0MDgzODU1MjU0MDI4MzA4.XvfNRg.aWHB5hzC2vd0gvsgJEhvHhzDWfY"


mainbot.run(token_RR)
