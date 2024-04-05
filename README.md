# Telegram Tech News Bot

## Overview
This Telegram bot fetches and posts technology-related news articles to a specified Telegram channel. It utilizes the News API to fetch news and the Telegram Bot API to post news articles to the channel.

[![Telegram Bot - Watch Video](https://previews.jumpshare.com/thumb/815bc01b796dd6f1733c957c5af19493245781fcd3b4253afe7452d17839a064e8fcf04488c008cf7e56129b09b48fbe91c9ec60d9030029d63e1faced566cb9e39ae69f08db93e7ee2164ad7418f08dfd0c2526c345e82c0e1b01ff617013ce)](https://jmp.sh/s/f2OqGgInjNFl8shX7z2Q)

Click the above play button  to watch the demo.

## Features
1.Fetches random technology-related news using the News API.

2.Formats news articles into a readable format with titles, descriptions, and URLs.

3.Posts formatted news to a specified Telegram channel using the Telegram Bot API.

4.Randomly selects a technology keyword for each news fetch to provide variety.

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)

## Setup
Clone the repository:
   ```
   git clone https://github.com/tamilselvanarjun/TelegramChatBot.git
   ```

## Install the required library:
```
pip install requests
```
## Configuration

Replace placeholders in the script:

open the .env file in the project root directory and add your environment variables:

TELEGRAM_BOT_TOKEN: Your Telegram bot token obtained from the BotFather.

TELEGRAM_CHANNEL_ID: The ID of your Telegram channel where you want to post the news.

NEWS_API_KEY: Your News API key obtained from https://newsapi.org/.

TELEGRAM_BOT_TOKEN=your_telegram_bot_token

TELEGRAM_CHANNEL_ID=your_telegram_channel_id

NEWS_API_KEY=your_news_api_key


## Usage
Run the script:
```
python telegram_bot.py
```
The bot will fetch a technology keyword, fetch news related to that keyword, format the news, and post it to the specified Telegram channel.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.