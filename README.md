# Project Description

This project utilizes the Discord.py API and the YouTube API. Mainly one that makes searching and sharing videos in the discord app instead of searching. There is a little tradeoff as it will retrieve only the top result from the query. And there is no other GUI aside from the Discord window. Also utilizes a Postgres database that caches the search history so the application stays under the query limit imposed by the YouTube API.

# Requirements

- [Python3](https://www.python.org/downloads)
- [Postgres](https://www.postgresql.org/)
- YouTube API Key (Obtain it here with this [guide](https://developers.google.com/youtube/v3/docs))
- [Discord](https://discord.com)
- Discord Application Token (Setup a bot with this [guide](https://discord.com/developers/docs/getting-started))

# Setting up

- Follow the instructions on how to connect a bot to your server from Application Token guide above.
- Create an .env in the root folder following the .env.example file.
- Run `python3 Bot.py`(Mac) or `py Bot.py`(Windows) in Terminal/CMD to run.
