import random
import requests
from urllib.parse import quote
import logging
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(filename='tech_news.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

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
    # Randomly select a keyword from the list of technology keywords
    random_keyword = random.choice(technology_keywords)
    return random_keyword


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
    # Initialize an empty string to store the formatted news
    formatted_news = ""

    # Iterate through each article in the news list
    for article in news:
        # Append the title, description, and URL of each article to the formatted news string
        formatted_news += f"Title: {article['title']}\n"
        formatted_news += f"Description: {article['description']}\n"
        formatted_news += f"URL: {article['url']}\n\n"

    # Return the formatted news string
    return formatted_news


def fetch_and_post_tech_news():
    # Fetch tech news from News API
    news = fetch_tech_news()

    # Format the news
    formatted_news = format_news(news)

    # Log successful news fetching
    logging.info("Tech news fetched successfully.")

    # Prepare the channel URL for Telegram
    channel_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL_ID}&text={formatted_news}"

    # Send the formatted news to Telegram
    response = requests.get(channel_url)

    # Check if the request to Telegram was successful
    if response.status_code == 200:
        # Log successful news posting to Telegram
        logging.info("Tech news posted to Telegram successfully.")
    else:
        # Log the error for failed news posting to Telegram
        logging.error(f"Failed to post tech news to Telegram. Status code: {response.status_code}")


if __name__ == '__main__':
    fetch_and_post_tech_news()
