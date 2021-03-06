import discord
from discord.ext import commands

from core.extension import Extension


class Command(Extension):
    @commands.command()
    async def status(self, ctx):
        server = ctx.message.guild
        owner = ctx.message.guild.owner.name
        member_count = ctx.message.guild.member_count
        online_member, dnd_member, idle_member = 0, 0, 0
        for member in ctx.guild.members:
            online_member = online_member + 1 if str(member.status) != 'offline' else online_member
            dnd_member = dnd_member + 1 if str(member.status) == 'dnd' else dnd_member
            idle_member = idle_member + 1 if str(member.status) == 'idle' else idle_member

        embed = discord.Embed(title='樂高', description='不要踩會痛', color=0xff2600)
        embed.add_field(name='伺服器', value=server, inline=True)
        embed.add_field(name='創始者', value=owner, inline=True)
        embed.add_field(name='人數', value=member_count, inline=False)
        embed.add_field(name='線上', value=online_member, inline=True)
        embed.add_field(name='閒置', value=idle_member, inline=True)
        embed.add_field(name='勿擾', value=dnd_member, inline=True)
        embed.add_field(name='Ping', value=f'{round(self.bot.latency * 1000)} ms', inline=True)
        embed.add_field(name='狀態', value='上線中', inline=True)
        embed.set_footer(text='ver. 0.1.0 beta')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Command(bot))
