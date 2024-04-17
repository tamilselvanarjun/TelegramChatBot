import unittest
from unittest.mock import patch
from main import generate_random_technology_keyword, fetch_tech_news, format_news, fetch_and_post_tech_news

class TestTechNews(unittest.TestCase):
    def test_generate_random_technology_keyword(self):
        """
        Test case to check if the generated technology keyword is valid.
        """
        keyword = generate_random_technology_keyword()
        self.assertIn(keyword, [
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
            "DevOps",
            "Matplotlib",
            "Google Cloud",
            "Azure"
        ])

    @patch('main.requests.get')
    def test_fetch_tech_news(self, mock_get):
        """
        Test case to check if the tech news fetching function works correctly.
        """
        mock_data = {
            'articles': [
                {'title': 'Sample Title', 'description': 'Sample Description', 'url': 'https://example.com'}
            ]
        }
        mock_get.return_value.json.return_value = mock_data
        news = fetch_tech_news()
        self.assertEqual(len(news), 1)
        self.assertEqual(news[0]['title'], 'Sample Title')

    def test_format_news(self):
        """
        Test case to check if the news formatting function works correctly.
        """
        articles = [
            {'title': 'Sample Title', 'description': 'Sample Description', 'url': 'https://example.com'}
        ]
        formatted_news = format_news(articles)
        self.assertIn('Title: Sample Title', formatted_news)
        self.assertIn('Description: Sample Description', formatted_news)
        self.assertIn('URL: https://example.com', formatted_news)

    @patch('main.requests.get')
    def test_fetch_and_post_tech_news(self, mock_get):
        """
        Test case to check if the fetch and post news function works correctly.
        """
        mock_data = {
            'articles': [
                {'title': 'Sample Title', 'description': 'Sample Description', 'url': 'https://example.com'}
            ]
        }
        mock_get.return_value.json.return_value = mock_data
        with patch('main.requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            fetch_and_post_tech_news()
            mock_request.assert_called_once()
            self.assertTrue(mock_request.called)

if __name__ == '__main__':
    unittest.main()
