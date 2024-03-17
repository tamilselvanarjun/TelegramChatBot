# Telegram Tech News Bot

## Overview
This Telegram bot fetches and posts technology-related news articles to a specified Telegram channel. It utilizes the News API to fetch news and the Telegram Bot API to post news articles to the channel.

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
Replace placeholders in the script:

Replace your_telegram_bot_token with your actual Telegram bot token.

Replace your_telegram_channel_id with your actual Telegram channel ID.

Replace your_news_api_key with your actual News API key.

## Usage
Run the script:
```
python telegram_tech_news_bot.py
```
The bot will fetch a technology keyword, fetch news related to that keyword, format the news, and post it to the specified Telegram channel.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.