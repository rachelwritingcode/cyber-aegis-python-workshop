from dotenv import load_dotenv
import os
import lightbulb

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = lightbulb.BotApp(prefix="!", token=DISCORD_TOKEN)

@bot.command()
@lightbulb.command("hello", "Greets users") 
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx: lightbulb.Context) -> None: 
    await ctx.respond("H3110 H@ck3r!🔥💻🔥") 

bot.run()