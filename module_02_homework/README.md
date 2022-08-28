### Workshop 3 & 4 Pre-requisite Requirements:

These are some pre-requisite requirements before we dive into Workshops 3 & 4. There will be flags as you continue along in this tutorial. For any questions or clarifications, use the Cyber Aegis discord workshop help channel to share your questions. Thank you!

---
### Homework Checklist

- [ ] Create a Discord Server
- [ ] Create a Discord Bot and Set Permissions
- [ ] Generate Discord Bot API Key
- [ ] Store your API Key and APPLICATION ID in a .env file

---
### How to Create a Discord Server 

- Open the discord application on your machine
- Navigate to the left side and hover over the + icon, it will say "Add a Server".
- Click "Add a Server".
![](create_server/add_server.png)

- A window will pop up to show these options, choose the Create My Own without a template.
![](create_server/create_a_server.png)


- Select the server option "For me and my friends".\
![](create_server/for_friends_server.png)


- Create a name for the Discord server, name it whatever you want.
![](create_server/name_server.png)


- Your new Discord server show be created. 🎉 🎉 🎉
![](create_server/completed_creation.png)



- Enter the flag 
`flag{created_a_server}`
---

### How to Create a Discord Bot

- Login to the Discord Developer Portal Website here:
https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications
![](create_bot/dev_portal_login.png)


- Upon logging in, look at the top right of the page, click the "New Application" button. 
![](create_bot/new_app.png)


- Give the application a name, and name it anything you want.
![](create_bot/create_app.png)

- A successfully created application will display a menu of settings like this.
![](create_bot/created_app.png)


- Navigate to the left side menu of the same page. Look for the section called Bot, click it. Now look at the right side of the page, there is a Add Bot button click this.

![](create_bot/create_bot.png)


- Confirm that you want to add the bot.
![](create_bot/confirm_bot.png)

- A new page will display information about your new bot. Give it a name you want, after renaming it, click the green save button on the botton right of the screen.
![](create_bot/bot_created_menu.png)

- Click reset token for your bot and confirm when the popup displays.
![](create_bot/reset_bot_token.png)

- Copy the token text, we are going store this token safely in a new file called .env.

- Create a new file called .env, create a variable called DISCORD_TOKEN and paste the token into the file. 
`DISCORD_TOKEN=your_token_text`

- Go back to the discord developer portal Bot menu and go to Privileged Gateway section of the bot settings page. 
- Set all the toggle buttons to the same settings as the one in this image. Click the green Save Changes button when you are done.
![](create_bot/privileged_gateway.png)

- Scroll down to the Bot Permissions menu and select Admin permissions. Click the green Save Changes to update the settings.
![](create_bot/admin_bot.png)


- Enter the flag `flag{bot_complete}`


---

### How to add your bot to discord server

- Login to the Discord Developer Portal Website here:
https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications
![](create_bot/dev_portal_login.png)


- Under the applications settings, select the Bot application you created earlier.
![](add_bot/select_application.png)


- You will be redirected to a General Information page for your bot. 
![](add_bot/get_client_id.png)


- Retrieve the APPLICATION ID and store that in the .env file you created in the earlier tutorial. In the .env file, create a variable called CLIENT_ID and assign it to your APPLICATION ID.
`CLIENT_ID=your_application_id`


- Navigate to the left side of the General Information and select the OAuth2. Click on the URL Generator setting.
![](add_bot/oauth_menu.png)


- You will now see OAuth2 URL Generator page. Under the Scope settings, select bot.
![](add_bot/select_bot.png)


- Scroll down and set the BOT PERMISSIONS to ADMINISTRATOR and save settings if available.
![](add_bot/bot_permissions.png)


- Scroll down and copy the bot url link and paste it into the browser.
![](add_bot/bot_url.png)


- You will be redirected to a new page to select which server you want to add the bot to, select the discord server you created earlier.
![](add_bot/add_bot_to_server.png)


- Confirm that you authorize this bot to have ADMIN permissions. You will be asked to verify you are a human using a hcaptcha photo, complete the verification challenge to continue.
![](add_bot/authorize_admin.png)
![](add_bot/verify.png)


- You should have completed adding your bot to the discord server.
![](add_bot/completed.png)


- Navigate to the discord server you created and you should see activity from your bot in the general channel.
![](add_bot/welcome_to_server.png)

- Enter the flag `flag{bot_is_live}`