import lightbulb

# Authenticate your bot with your token, ignore the prefix 
bot = lightbulb.BotApp(prefix="!", token="YOUR_TOKEN")

@bot.command() # Register the command to the bot
@lightbulb.command("ping", "Checks that the bot is active") # We give the command a name and description
@lightbulb.implements(lightbulb.SlashCommand) # Define it is a slash command 
async def ping(ctx: lightbulb.Context) -> None: # Define the function and name it ping
    await ctx.respond("Pong!") # Send a message to the discord channel

# Run the bot until the bot is shut off
bot.run()
#Reference: https://github.com/tandemdude/hikari-lightbulb/blob/development/examples/basic_slash_command_bot_example.py