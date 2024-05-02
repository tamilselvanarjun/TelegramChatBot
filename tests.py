import unittest
from unittest.mock import patch, MagicMock
import io
import sys
import requests
from my_script import generate_random_technology_keyword, fetch_tech_news, format_news, fetch_and_post_tech_news

class TestTechNews(unittest.TestCase):
    @patch('random.choice')
    def test_generate_random_technology_keyword(self, mock_choice):
        mock_choice.return_value = "artificial intelligence"
        keyword = generate_random_technology_keyword()
        self.assertEqual(keyword, "artificial intelligence")

    @patch('requests.get')
    def test_fetch_tech_news(self, mock_get):
        mock_response = {'articles': [{'title': 'Test Title', 'description': 'Test Description', 'url': 'https://example.com'}]}
        mock_get.return_value.json.return_value = mock_response
        news = fetch_tech_news()
        self.assertEqual(news, [{'title': 'Test Title', 'description': 'Test Description', 'url': 'https://example.com'}])

    def test_format_news(self):
        news = [{'title': 'Test Title', 'description': 'Test Description', 'url': 'https://example.com'}]
        formatted_news = format_news(news)
        expected_output = "Title: Test Title\nDescription: Test Description\nURL: https://example.com\n\n"
        self.assertEqual(formatted_news, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fetch_and_post_tech_news_success(self, mock_stdout):
        response_mock = MagicMock()
        response_mock.status_code = 200
        with patch('requests.get', return_value=response_mock):
            fetch_and_post_tech_news()
            self.assertEqual(mock_stdout.getvalue(), "Tech news posted to Telegram successfully.\n")

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_fetch_and_post_tech_news_failure(self, mock_stderr):
        response_mock = MagicMock()
        response_mock.status_code = 404
        with patch('requests.get', return_value=response_mock):
            fetch_and_post_tech_news()
            self.assertIn("Failed to post tech news to Telegram. Status code: 404", mock_stderr.getvalue())

if __name__ == '__main__':
    unittest.main()
