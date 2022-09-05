### Workshop 3 & 4 Pre-requisite Requirements:

These are some pre-requisite requirements before we dive into Workshops 3 & 4. There will be flags as you continue along in this tutorial. For any questions or clarifications, use the Cyber Aegis discord workshop help channel to share your question.

---
### Homework Checklist

- [ ] Create a .gitignore file 
- [ ] Install Python-dotenv Package  
- [ ] Install Hikari-Lightbulb Package
- [ ] Review sample code from Hikari-Lightbulb Package


---
### Create a .gitignore file

- Wherever you are planning to store workshop files, create a file called .gitignore.
- Open this file and type in .env.
- You have now created a file which tells git to ignore the .env file, preventing you from accidentally adding sensitive information into a Github repo.

```
.env
```

---

### Install Python-dotenv Package

Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles.

```
pip install python-dotenv
```
https://github.com/theskumar/python-dotenv

---

### Introduction to Hikari-Lightbulb Package

#### Hikari Lightbulb Package

Hiakri-Lightbulb is designed to be an easy to use command handler library that integrates with the Discord API wrapper library for Python, Hikari.

This library aims to make it simple for you to make your own Discord bots and provide all the utilities and functions you need to help make this job easier.

```
pip install hikari-lightbulb
```

https://pypi.org/project/hikari-lightbulb/

---
### Review Sample Code from Hikari-Lightbulb Package


Read this sample piece of code from the Hikari-Lightbulb Github Repo. Try to familiarize yourself with the package. Don't worry if you don't understand all of the code now, we will walk through it together on workshop day.


```

import lightbulb

# Authenticate your bot with the token
bot = lightbulb.BotApp(prefix="!", token="YOUR_TOKEN")


# Register the command to the bot
@bot.command()
# Use the command decorator to convert the function into a command
@lightbulb.command("ping", "Checks that the bot is alive")
# Define the command type(s) that this command implements, this is a slash command
@lightbulb.implements(lightbulb.SlashCommand)
# Define a function called ping
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("Pong!")


# Another example of a slash command function called echo
@bot.command()
@lightbulb.option("text", "Text to repeat")
@lightbulb.command("echo", "Repeats the user's input")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)


# Run the bot
# Note that this is blocking meaning no code after this line will run
# until the bot is shut off
bot.run()
```

Reference: https://github.com/tandemdude/hikari-lightbulb/blob/development/examples/basic_slash_command_bot_example.py