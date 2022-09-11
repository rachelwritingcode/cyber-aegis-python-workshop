from dotenv import load_dotenv
import os
import lightbulb

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = lightbulb.BotApp(prefix="!", token=DISCORD_TOKEN)

@bot.command()
@lightbulb.command("ping", "Checks that the bot is active") 
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None: 
    await ctx.respond("Pong!") 

bot.run()