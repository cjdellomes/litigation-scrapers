import unittest
from scraper import Scraper

class TestScraper(unittest.TestCase):

    def test_get_enforcement_action_search_page(self):
        expected_response_code = 200
        expected_url = 'https://www.consumerfinance.gov/enforcement/actions/'

        scraper = Scraper(None, None, None, None)

        response = Scraper.get_enforcement_action_search_page()

        self.assertEqual(response.status_code, expected_response_code)
        self.assertEqual(response.url, expected_url)

if __name__ == '__main__':
    unittest.main()