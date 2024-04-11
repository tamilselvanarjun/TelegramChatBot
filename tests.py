import unittest
from unittest.mock import patch
from your_script_name import fetch_tech_news, format_news, generate_random_technology_keyword

class TestTechNews(unittest.TestCase):
    @patch('your_script_name.requests.get')
    def test_fetch_tech_news(self, mock_get):
        mock_get.return_value.json.return_value = {'articles': [{'title': 'Test Title', 'description': 'Test Description', 'url': 'http://example.com'}]}
        articles = fetch_tech_news()
        self.assertEqual(len(articles), 1)
        self.assertIn('title', articles[0])
        self.assertIn('description', articles[0])
        self.assertIn('url', articles[0])
def test_format_news(self):
        news = [{'title': 'Test Title', 'description': 'Test Description', 'url': 'http://example.com'}]
        formatted_news = format_news(news)
        self.assertIn('Test Title', formatted_news)
        self.assertIn('Test Description', formatted_news)
        self.assertIn('http://example.com', formatted_news)

if __name__ == '__main__':
    unittest.main()


#Vice President of Operations at TEAM Public Choices
