import discord
from discord.ext import commands

class test:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        
    testEmbed = discord.Embed(title='test', type='rich', description='test', url='https://github.com/Rapptz/discord.py/issues/424', colour = discord.Colour.blue())
    testEmbed.set_thumbnail(url='https://github.com/Rapptz/discord.py/issues/424')
    testEmbed.set_author(name='test')
    testEmbed.set_footer(text='test')

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
        await self.bot.say(embed=testEmbed)

def setup(bot):
    bot.add_cog(test(bot))
