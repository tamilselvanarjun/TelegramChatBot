import unittest
from unittest.mock import patch
import tech_news  # Assuming the script name is tech_news.py

class TestTechNews(unittest.TestCase):
    
    @patch('tech_news.requests.get')
    def test_fetch_tech_news(self, mock_get):
        # Mocking the response from the News API
        mock_response = {
            "articles": [
                {"title": "Test Article 1", "description": "Description 1", "url": "http://example.com/1"},
                {"title": "Test Article 2", "description": "Description 2", "url": "http://example.com/2"}
            ]
        }
        mock_get.return_value.json.return_value = mock_response
        
        news = tech_news.fetch_tech_news()
        
        self.assertEqual(len(news), 1)  # Ensure only one article is fetched
        self.assertEqual(news[0]['title'], "Test Article 1")  # Check if title matches
        
    def test_format_news(self):
        news = [{"title": "Test Article", "description": "Description", "url": "http://example.com"}]
        formatted_news = tech_news.format_news(news)
        
        expected_output = "Title: Test Article\nDescription: Description\nURL: http://example.com\n\n"
        self.assertEqual(formatted_news, expected_output)
    
    @patch('tech_news.requests.get')
    def test_fetch_and_post_tech_news(self, mock_get):
        # Mocking the response from the News API
        mock_response = {
            "articles": [
                {"title": "Test Article", "description": "Description", "url": "http://example.com"}
            ]
        }
        mock_get.return_value.json.return_value = mock_response
        
        with patch('tech_news.requests.get') as mock_post:
            # Mocking the response from Telegram API
            mock_post.return_value.status_code = 200
            
            tech_news.fetch_and_post_tech_news()
            
            # Check if the post request to Telegram was made
            mock_post.assert_called_once()
    
    def test_generate_random_technology_keyword(self):
        keyword = tech_news.generate_random_technology_keyword()
        self.assertIn(keyword, tech_news.technology_keywords)  # Check if generated keyword is in the list

if __name__ == '__main__':
    unittest.main()
