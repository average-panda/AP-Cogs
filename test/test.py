import discord
from discord.ext import commands
import asyncio

class test:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        
    Tembed = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~", colour=discord.Colour(0x687508), url="https://discordapp.com", description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```")
    
    Tembed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
    Tembed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
    Tembed.set_author(name="author name", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    Tembed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    Tembed.add_field(name="1", value="some of these properties have certain limits...")
    Tembed.add_field(name="2", value="try exceeding some of them!")
    Tembed.add_field(name="3", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
    Tembed.add_field(name="<:thonkang:219069250692841473>", value="???")

    @commands.command()
    async def punch(self, user : discord.Member):
        """I will puch anyone! >.<"""

        #Your code will go here
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")
        
    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")
        
    @commands.command()
    async def embed(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say(embed=Tembed)
        
    @commands.command()
    async def embed2(self):
        """This does stuff!"""
        
        #Your code will go here
        await self.bot.say(content="this `supports` __a__ **subset** *of* ~~markdown~~ 😃 ```js\nfunction foo(bar) {\n  console.log(bar);\n}\n\nfoo(1);```", embed=Tembed)

def setup(bot):
    bot.add_cog(test(bot))
