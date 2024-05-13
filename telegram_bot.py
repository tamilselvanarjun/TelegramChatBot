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

# Constants
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# List of technology-related keywords
technology_keywords = [
    "artificial intelligence", "machine learning", "cybersecurity", "blockchain", "internet of things",
    "5g technology", "cloud computing", "big data", "virtual reality", "augmented reality", "quantum computing",
    "generative AI", "data science", "python programming", "DevOps", "Matplotlib", "Google Cloud", "Azure"
]

def generate_random_technology_keyword():
    """Generate a random technology keyword."""
    return random.choice(technology_keywords)

def fetch_tech_news():
    """Fetch top headlines from News API with a random technology keyword."""
    keyword = generate_random_technology_keyword()
    encoded_keyword = quote(keyword)
    url = f'https://newsapi.org/v2/everything?q={encoded_keyword}&language=en&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    if articles:
        return [random.choice(articles)]
    else:
        logging.warning(f"No articles found for keyword: {keyword}")
        return []

def format_news(news):
    """Format news articles."""
    formatted_news = ""
    for article in news:
        formatted_news += f"Title: {article['title']}\n"
        formatted_news += f"Description: {article['description']}\n"
        formatted_news += f"URL: {article['url']}\n\n"
    return formatted_news

def fetch_and_post_tech_news():
    """Fetch and post tech news to Telegram."""
    news = fetch_tech_news()
    if news:
        formatted_news = format_news(news)
        channel_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL_ID}&text={formatted_news}"
        response = requests.get(channel_url)
        if response.status_code == 200:
            logging.info("Tech news posted to Telegram successfully.")
        else:
            logging.error(f"Failed to post tech news to Telegram. Status code: {response.status_code}")
    else:
        logging.warning("No tech news fetched.")

if __name__ == '__main__':
    fetch_and_post_tech_news()

