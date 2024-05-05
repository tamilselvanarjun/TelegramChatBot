import unittest
from unittest.mock import patch, MagicMock
import io
from my_script import generate_random_technology_keyword, fetch_tech_news, format_news, fetch_and_post_tech_news

class TestTechNews(unittest.TestCase):
    # Testing the generate_random_technology_keyword function
    @patch('random.choice')
    def test_generate_random_technology_keyword(self, mock_choice):
        mock_choice.return_value = "artificial intelligence"
        keyword = generate_random_technology_keyword()
        self.assertEqual(keyword, "artificial intelligence", "Should return 'artificial intelligence'")

    # Testing the fetch_tech_news function with mocked API response
    @patch('requests.get')
    def test_fetch_tech_news(self, mock_get):
        mock_response = {'articles': [{'title': 'Test Title', 'description': 'Test Description', 'url': 'https://example.com'}]}
        mock_get.return_value.json.return_value = mock_response
        news = fetch_tech_news()
        expected_news = [{'title': 'Test Title', 'description': 'Test Description', 'url': 'https://example.com'}]
        self.assertEqual(news, expected_news, "Should fetch and return tech news correctly")

    # Testing the format_news function
    def test_format_news(self):
        news = [{'title': 'Test Title', 'description': 'Test Description', 'url': 'https://example.com'}]
        formatted_news = format_news(news)
        expected_output = "Title: Test Title\nDescription: Test Description\nURL: https://example.com\n\n"
        self.assertEqual(formatted_news, expected_output, "Should format news correctly")

    # Testing the fetch_and_post_tech_news function with mocked API response and stdout
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fetch_and_post_tech_news_success(self, mock_stdout):
        response_mock = MagicMock()
        response_mock.status_code = 200
        with patch('requests.get', return_value=response_mock):
            fetch_and_post_tech_news()
            self.assertEqual(mock_stdout.getvalue(), "Tech news posted to Telegram successfully.\n", "Should log successful news posting")

    # Testing the fetch_and_post_tech_news function with mocked API response and stderr
    @patch('sys.stderr', new_callable=io.StringIO)
    def test_fetch_and_post_tech_news_failure(self, mock_stderr):
        response_mock = MagicMock()
        response_mock.status_code = 404
        with patch('requests.get', return_value=response_mock):
            fetch_and_post_tech_news()
            self.assertIn("Failed to post tech news to Telegram. Status code: 404", mock_stderr.getvalue(), "Should log error for failed news posting")

if __name__ == '__main__':
    unittest.main()
