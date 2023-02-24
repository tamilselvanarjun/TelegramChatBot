import random
import requests
from urllib.parse import quote
import logging

# Configure logging
logging.basicConfig(filename='tech_news.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHANNEL_ID = 'your_telegram_channel_id'
NEWS_API_KEY = 'your_news_api_key'

# List of technology-related keywords
technology_keywords = [
    "artificial intelligence",
    "machine learning",
    "cybersecurity",
    "blockchain",
    "internet of things",
    "5g technology",
    "cloud computing",
    "big data",
    "virtual reality",
    "augmented reality",
    "quantum computing",
    "generative AI",
    "data science",
    "python programming",
    "java",
    "DevOps",
    "Matplotlib",
    "Google Cloud",  # Added comma here
    "Azure"
]


def generate_random_technology_keyword():
    # Randomly select a keyword from the list
    return random.choice(technology_keywords)


def fetch_tech_news():
    # Fetch top headlines from News API with 'tech' category
    keyword = generate_random_technology_keyword()
    # Encode the keyword
    encoded_keyword = quote(keyword)
    url = f'https://newsapi.org/v2/everything?q={encoded_keyword}&language=en&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = [random.choice(data['articles'])]
    return articles


def format_news(news):
    # Format the fetched news into a readable format (e.g., markdown)
    formatted_news = ""
    for article in news:
        formatted_news += f"Title: {article['title']}\n"
        formatted_news += f"Description: {article['description']}\n"
        formatted_news += f"URL: {article['url']}\n\n"
    return formatted_news


def fetch_and_post_tech_news():
    # Fetch tech news from News API
    news = fetch_tech_news()

    # Format the news
    formatted_news = format_news(news)

    # Print the formatted news
    print(formatted_news)

    # Log successful news fetching
    logging.info("Tech news fetched successfully.")

    # Prepare the channel URL for Telegram
    channel_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id=-your_telegram_channel_id&text={formatted_news}"

    # Send the formatted news to Telegram
    response = requests.get(channel_url)

    # Check if the request to Telegram was successful
    if response.status_code == 200:
        # Print the Telegram response
        print(response.json())

        # Log successful news posting to Telegram
        logging.info("Tech news posted to Telegram successfully.")
    else:
        # Print an error message for unsuccessful request to Telegram
        print("Error:", response.status_code)

        # Log the error for failed news posting to Telegram
        logging.error(f"Failed to post tech news to Telegram. Status code: {response.status_code}")



if __name__ == '__main__':
    fetch_and_post_tech_news()
