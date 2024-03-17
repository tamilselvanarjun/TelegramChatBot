import random
import requests
from urllib.parse import quote

TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHANNEL_ID = 'your_telegram_channel_id'
NEWS_API_KEY = 'your_news_api_key'

# List of technology-related keywords
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
    "Google Cloud"
    "Azure"
]


def generate_random_technology_keyword():
    # Randomly select a keyword from the list
    return random.choice(technology_keywords)

def fetch_and_post_tech_news():
    # Fetch tech news from News API
    news = fetch_tech_news()

    # Format the news
    formatted_news = format_news(news)
    print(formatted_news)
    channel_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id=-your_telegram_channel_id&text={formatted_news}"
    response = requests.get(channel_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Do something with the response, like print it
        print(response.json())
    else:
        print("Error:", response.status_code)

def fetch_tech_news():
    # Fetch top headlines from News API with 'tech' category
    keyword = generate_random_technology_keyword()
    # Encode the keyword
    encoded_keyword = quote(keyword)
    url = f'https://newsapi.org/v2/everything?q={encoded_keyword}&language=en&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    lower_bound = 1
    upper_bound = len(data)
    # Generate a random number inclusively within the specified range
    random_number = random.randint(lower_bound, upper_bound)
    articles = [data['articles'][random_number]]
    return articles

def format_news(news):
    # Format the fetched news into a readable format (e.g., markdown)
    formatted_news = ""
    for article in news:
        formatted_news += f"Title: {article['title']}\n"
        formatted_news += f"Description: {article['description']}\n"
        formatted_news += f"URL: {article['url']}\n\n"
    return formatted_news

if __name__ == '__main__':
    fetch_and_post_tech_news()
