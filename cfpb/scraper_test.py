import unittest
from datetime import date
from scraper import Scraper

class TestScraper(unittest.TestCase):

    def test_get_enforcement_action_search_page(self):
        expected_response_code = 200
        expected_url = 'https://www.consumerfinance.gov/enforcement/actions/'

        scraper = Scraper(None, None, None, None)

        response = scraper.get_enforcement_action_search_page()

        self.assertEqual(response.status_code, expected_response_code)
        self.assertEqual(response.url, expected_url)

    def test_get_enforcement_action_filtered_page(self):
        expected_response_code = 200
        expected_url = 'https://www.consumerfinance.gov/enforcement/actions/?page=1&categories=administrative-proceeding&statuses=expired-terminated-dismissed&statuses=post-order-post-judgment&from_date=2013-01-14&to_date=2016-01-14'

        categories = ['administrative-proceeding']
        statuses = ['expired-terminated-dismissed', 'post-order-post-judgment']
        from_date = date(2013,1,14)
        to_date = date(2016,1,14)

        scraper = Scraper(categories, statuses, from_date, to_date)

        response = scraper.get_enforcement_action_filtered_page(1)

        self.assertEqual(response.status_code, expected_response_code)
        self.assertEqual(response.url, expected_url)

    def test_get_enforcement_action_filtered_page_some_filters_missing(self):
        expected_response_code = 200
        expected_url = 'https://www.consumerfinance.gov/enforcement/actions/?page=1&categories=administrative-proceeding&statuses=expired-terminated-dismissed'

        categories = ['administrative-proceeding']
        statuses = ['expired-terminated-dismissed']
        from_date = None
        to_date = None

        scraper = Scraper(categories, statuses, from_date, to_date)

        response = scraper.get_enforcement_action_filtered_page(1)

        self.assertEqual(response.status_code, expected_response_code)
        self.assertEqual(response.url, expected_url)

if __name__ == '__main__':
    unittest.main()