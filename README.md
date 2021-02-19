## TheImperialGod 
TheImperialGod is an awesome discord.py bot which has plenty of features!
**If you like TheImperialGod as a discord bot, starring the repo is the best that you can do and is very much appreciated. 
This is because starring the repo, brings it higher in search results and makes the repo more popular.**

It has many features, so you dont have to have many bots in your server just to get the commands that you want. It is always being improved, so if you see a bug or have a suggestion, dont hesitate to use the report bug or suggest commands to contact the devloper. It is always online, so no need to worry about it going offline randomly
# Features
TheImperialGod is an awesome bot with plenty of utilities and good for all the roles in a discord server
The Roles in a discord server are:
* Member
* Moderator
* Admin

For each of these, TheImperialGod has its very own commands, and is easily self-hostable. 
With a nice themed topic and useful features, that is TheImperialGod in a nutshell. 

# License warning
DO NOT COPY CODE FROM THIS REPOSITORY WITHOUT PROPERLY CREDITING ME! I don't want to DMCA anyone, but I will do what is necessary to defend the license. 
<br> If you are not familiar with how to give credit then please DM me on discord (NightZan999#0194) or you can obviously create an issue!

Read LICENSE, for more information about the license.

## Introduction
Before touching the code and stuff please read till the end of the MD file. There is a ton of important information in this README file. Also once you read this, read the code of conduct. <br>

You can choose whether or not you want to read CONTRIBUTING.md, as do it only if you want to contribute, as some of the code is hard for inexperienced programmers. And leave it if your new here, as first check out the bot!

Once you have and if you like the public bot or the code then consider starring this repository. This not only helps out the contributors but the people who actually coded this bot. 
Thanks and Regards,
NightZan999

## Moderation
Has advanced moderation features for all people! With using the concept of embeds and more! <br> Cool right, it also has automoderation features and that's customizable, which makes it perfect for you! <br>

The bot is even smart enough NOT to filter automod in NSFW channels even if its enabled!

## Economy
Okay economy systems are hard, they take about 1000 lines just to write a shop and have a wallet and arcade system. See this is hard!

But don't worry, for we have used SQLite3. Oh you must be wondering, isn't sqlite not usable for discord.py, yes it is. So I use aiosqlite as a databse!
**Sadly we still use JSON for minor stuff like automod or server settings. But we will be switching very soon!**

## Utilities
Yes, TheImperialGod has like plenty of utility features including a changing status that changes his status every 10 seconds, which to me is really cool.

Now, it has coinflip and plenty of stuff, so yeah have fun with your friends.
So till now good going and before you touch the code.

## Giveaways
So we have some Giveaway features which simply reroll and start a giveaway, kinda basic but that's all we have for the bot. The rest of the commands are just customizable.

###### (We also have *error handling* for all commands!)

## Issues
Issues with the public bot will probably be outages and we cannot help those, rather than making them, please refrain from doing that.

You have the code in front of you, please download it and host it. 

# Self Hosting
Yes this is the most important place here. <br>**Note:** Self hosting is suggested as the public bot goes offline sometimes and that may disrupt your giveaways.

Just in bot.py check the bot token and replace it with yours. As TheImperialGod doesn't have changing prefixes, so change the prefix as well if you would like!

But please, **GIVE THE CREDITS.** If you keep the credits and don't brag that you made the bot. Its fine that you can use the bot!

## Steps for Self Hosting
Please note, this is expected to be done with basic Python knowledge. If you do not know how Python works, please do not attempt to self-host.
1. Download the bot files either by downloading as a zip in github or doing `git clone https://github.com/NightZan999/TheImperialGod.git`, make sure you have git installed or  github CLI (Client Line Interface).
3. Then go to cmd of that directory and type `pip install -r requirements.txt`. Once its done, go to config.json and fill it in with all the correct details.

For the reddit section create an app [here](https://reddit.com/prefs/apps) make your own **script** and you should have all the data. 
Yeah and then its simple throw your data into config.json and done it should work. 

4. Then you can go to cmd and type `python bot.py`, which should start the bot.
5. Enjoy the bot! <br>
**Note:** TheImperialGod uses an old version of discord.py as listed in requirements.txt, which means if you just `pip install` all the modules listed it WON'T work!

## **Self Hosting Guildlines and Agreement.**
You **must** give credits to Nightzan999.
You **cannot** say you made the bot yourself. You must give credits in your source code.
You **cannot** brag or say that you made it when you did not.
You **cannot** make your self-hosted bot a public bot.
If you're self-hosting the bot as it is, you **must** give all credits.
If you're using the source code to add just a few commands (1-5), credits is not necessary, **but it will be appreciated**. If you're adding more than 5 commands from the source code, you must give credits.
**Please respect the [LICENSE](https://github.com/NightZan999/TheImperialGod/blob/main/LICENSE).**

Due to this having a LICENSE, you breaking any of the following rules could **cause legal issues.**


### Public Bot
I guess, well you read that and your a new programmer. <br>**Note:** This code may be hard for inexperienced programmers, so if you don't understand stuff, just add the public bot!

You can find the invite link in the main bot file, just copy paste that into your browser, so yes continue and your bot is here!

Or of course if you don't know how to read variables simply click [this](https://discordapp.com/oauth2/authorize?&client_id=768695035092271124&scope=bot&permissions=21474836398)!

He will be up most of the time, but when he is down please cope with it!
But anyways, if you are interested in the public bot. Then you are in the currency system, and if you want coins join my server where there are giveaways happening.

Join [here](https://discord.gg/ZyD8xJRHMS)

# Contributions
As I realize that the bot is not perfect, and has some improvements which can be made. I agree I am not the best in discord.py.
Read CONTRIBUTING.md to know a bit more about contributing to this repository. 

Hope you contribute :D
**Note: There are many ways to contribute in this repository. I would prefer if you read CONTRIBUTING.md**

## Suggestions and More:
If you tested the bot and loved it, but thought you would want to give in some suggestions, please first don't make an issue. 

Firstly you should simply, check BETA_FEATURES.md for some new things the bot might get, if your suggestion is an improvement first search for a similar suggestion in the issues, if there are none then make a new one. 

Otherwise you also can suggest stuff in my discord server, so you could join it and make things easy!

# File Tree

```text
nightzan999/theimperialgod/
├── theimperialgod/
│   ├── bot.py
│   ├── Procfile
│   ├── requirements.txt
│   ├── project.yml
│   ├── config.json
|   ├── utils/
|   |   ├── embeds.py
|   |   ├── emojis.py
|   |   ├── jsonfile.py 
|   ├── events/
|   |   ├── GuildEvents.py
|   ├── cogs/
|   |   ├── moderation/
|   |   ├   ├── admin.py
|   |   ├   ├── mod.py
|   |   ├   ├── giveaways.py
|   |   ├   ├── owner.py
|   |   ├── info/
|   |   ├   ├── info.py
|   |   ├   ├── math.py
|   |   ├   ├── help.py
|   |   ├   ├── topgg.py
|   |   ├── economy/
|   |   ├   ├── bankcommands.py
|   |   ├   ├── moneymaking.py
|   |   ├   ├── shop.py
|   |   ├── tickets/
|   |   ├   ├── tickets.py
|   |   ├── fun/
|   |   ├   ├── animals.py
|   |   ├   ├── misc.py
|   |   ├   ├── utils.py
|   ├── assets/
|   |   ├── bot_pic.jpg
|   |   ├── candy.jpg
|   |   ├── wanted.jpg 
|   ├── data/
|   |   ├── admin.db
|   |   ├── automod.json
|   |   ├── economy.db
|   |   ├── emojis.json
|   |   ├── guilds.json
|   |   ├── mainbank.json
|   |   ├── muterole.json
|   |   ├── tickets.json
|   |   ├── warns.json
```

## Hosting
You would obviously need to find a good hosting manager, which is probably why you need this file: HOSTING.md. 
In this file we mention about **almost all hosts.**

# Credits:
**1. NightZan999:**
The main developer of TheImperialGod, not only coded all the cogs and the code himself, but also hosted the bot and did more. <br>
**2. Dragonizedpizza:**
The second most important developer, not only helped TheImperialGod's earlier version in advanced moderation and gave me very useful suggestions <br>
He also helped me with Github stuff. <br> 
**3. Makiyu-py:**
he helped me out in grammar errors 😎 and in some commands! <br>
**4. JakeLion:**
Jake has helped in tickets and fixing code to the modern style (im old school RIP). 
