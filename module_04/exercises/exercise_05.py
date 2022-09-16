from dotenv import load_dotenv
import os
import lightbulb
import random

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = lightbulb.BotApp(prefix="!", token=DISCORD_TOKEN)

@bot.command()
@lightbulb.command("hello", "Greets users") 
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx: lightbulb.Context) -> None: 
    await ctx.respond("H3110 H@ck3r!🔥💻🔥") 

@bot.command()
@lightbulb.command("joke", "Tells you a joke") 
@lightbulb.implements(lightbulb.SlashCommand)
async def joke(ctx: lightbulb.Context) -> None: 
    jokes = [
        "Why did the programmer leave the camping trip early?\n🥁 Because there were too many bugs! 🐛 🐛 🐛",
        "What did the hacker's out of office message say?\n🥁 Gone phishing. 🎣 🎣 🎣",
        "What do you call a turtle that surfs the Dark Web?\n🥁 A TORtoise. 🧅 🐢 🧅 🐢 🧅 🐢 ",
        "What's a hacker's favourite season?\n🥁 Phishing season. 🎣 🎣 🎣 ",
        "What’s the best way to catch a runaway robot?\n🥁 Use a botnet. 🤖 🥅 ",
        "An SQL statement walks into a bar and sees two tables. It approaches and asks…\n🥁 May I join you? 🍸 🍸 🍸"
    ]
    random_num = random.randrange(0, 6)
    await ctx.respond(jokes[random_num]) 

async def main(bot):
    hello()
    joke()

bot.run()