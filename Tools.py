
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import re
import base64

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
* It doesn't matter if there is no spaces between each binary code. The bot already handles it

2) .b

* Fixes the text that is backwards 
* Automatically removes whitespace
* Automatically adds the code after https://discord.gg/ to make it useful for autojoiners.
* Removes the ' https://discord.gg/ ' if its accidentally put in the code after .b so there is no duplicate
* Also handles ' https://discord.gg/ ' if its backwards e.g ' olleh/gg.drocsid//:sptth '

3) -64

* converts base 64 to text  

4) -i 
* Automatically removes whitespace on the discord invite code 
* Automatically removes symbols on the discord invite code
* Removes the ' https://discord.gg/ ' if its accidentally put in the code after -i so there is no duplicate
* Makes it into a discord invite form

```
"""


@mainbot.event
@commands.guild_only()
async def on_message(message):

    if message.content.lower().startswith('stop'):
        print("bot stoped")
        return

    ### Ignore. This bit is for the automatic detection

    
    if message.content.startswith('.b'):
        the_message = str(message.content).replace(" ","").replace(".b ","").replace(".b","").replace("https://discord.gg/","").replace("/gg.drocsid//:sptth","").replace("/gg.drocsid","")
        if the_message == "":
            pass

        else:
            channel = message.channel
            backwards = str(the_message[::-1])

            await channel.send("https://discord.gg/" + backwards)
    

    if message.content.startswith('-64'):
        the_message = str(message.content).replace(" ","").replace("-64 ","").replace("-64","").replace("https://discord.gg/","").replace("discord.gg/","").replace("/gg.drocsid//:sptth","").replace("/gg.drocsid","")
        
        if the_message == "":
            pass

        else:
            channel = message.channel
            converted = base64.b64decode(the_message)

            await channel.send(converted.decode('ascii'))



    elif message.content.startswith('-help'):
        channel = message.channel

        await channel.send(help_message)

    await mainbot.process_commands(message)
        



@mainbot.command()
@commands.guild_only()
async def i(ctx,*,message):
    message = str(message).replace(" ","").replace("https://discord.gg/","").replace("discord.gg/","")
    message = re.sub("[^A-Za-z0-9]+","",message)
     
    await ctx.send("https://discord.gg/" + message)    



# Still needs work
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





########## Binary converter 
@mainbot.command()
@commands.guild_only()
async def b(ctx,*,message):

    try:

        binary_values = message.split()
        print(binary_values)

        ascii_string = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character
            ascii_string = str(ascii_string).replace(" ","")
            ascii_string = ascii_string.replace("https://discord.gg/"," ")
            
        await ctx.send("https://discord.gg/" + ascii_string)
    
    except OverflowError:
        x = 0 
        y = 8 

        line = ""
        while y <= int(len(message)):
            oneBinaryCode = message
            oneBinaryCode = message[x:y]
            x += 8
            y += 8 


            line += " " + oneBinaryCode


        line = line.replace(" ","",1)



        binary_values = line.split()
        print(binary_values)


        ascii_string = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character
            ascii_string = str(ascii_string).replace(" ","")
            ascii_string = ascii_string.replace("https://discord.gg/"," ")
            
        await ctx.send("https://discord.gg/" + ascii_string)
        


token_test = "NzE0MDgzODU1MjU0MDI4MzA4.Xspgag.Uof1FspmtRqpQpHAnYboMZLyDXw"
token_RR = "NzA4MDAxODIwMTQ3OTc0MTk0.XrRAEw.KGPrssGTL3m48RgvHMRCNkJVi9U"

mainbot.run(token_RR)
