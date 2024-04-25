import unittest
from unittest.mock import patch, Mock
from your_script_file import (
    generate_random_technology_keyword,
    fetch_tech_news,
    format_news,
    fetch_and_post_tech_news,
)

class TestTechNewsFunctions(unittest.TestCase):

    def test_generate_random_technology_keyword(self):
        keyword = generate_random_technology_keyword()
        self.assertIsInstance(keyword, str)
        self.assertIn(keyword, technology_keywords)

    @patch('requests.get')
    def test_fetch_tech_news(self, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'articles': [{'title': 'Test Title', 'description': 'Test Description', 'url': 'http://test.url'}]}
        mock_requests_get.return_value = mock_response

        news = fetch_tech_news()
        self.assertEqual(len(news), 1)
        self.assertIn('title', news[0])
        self.assertIn('description', news[0])
        self.assertIn('url', news[0])

    def test_format_news(self):
        test_news = [{'title': 'Test Title', 'description': 'Test Description', 'url': 'http://test.url'}]
        formatted_news = format_news(test_news)
        self.assertNotEqual(formatted_news, "")
        self.assertIn('Test Title', formatted_news)
        self.assertIn('Test Description', formatted_news)
        self.assertIn('http://test.url', formatted_news)

    @patch('requests.get')
    @patch('logging.info')
    def test_fetch_and_post_tech_news(self, mock_logging_info, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response

        fetch_and_post_tech_news()
        mock_logging_info.assert_called_with("Tech news fetched successfully.")

if __name__ == '__main__':
    unittest.main()
