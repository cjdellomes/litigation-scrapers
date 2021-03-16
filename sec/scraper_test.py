import unittest
from scraper import Scraper

class TestScraper(unittest.TestCase):

    def test_get_year_page_current_year(self):
        year = 2021
        expected_response_code = 200
        expected_url = 'https://www.sec.gov/litigation/litreleases.htm'

        response = Scraper.get_year_page(year)

        self.assertEqual(response.status_code, expected_response_code)
        self.assertEqual(response.url, expected_url)

    def test_get_year_page_previous_year(self):
        year = 2006
        expected_response_code = 200
        expected_url = 'https://www.sec.gov/litigation/litreleases/litrelarchive/litarchive2006.shtml'

        response = Scraper.get_year_page(year)

        self.assertEqual(response.status_code, expected_response_code)
        self.assertEqual(response.url, expected_url)

    def test_get_litigation_page_txt_file(self):
        expected_response_code = 200
        link = '/litigation/litreleases/lr14769.txt'
        expected_url = 'https://www.sec.gov/litigation/litreleases/lr14769.txt'

        response = Scraper.get_litigation_page(link)

        self.assertEqual(response.status_code, expected_response_code)
        self.assertEqual(response.url, expected_url)

    def test_get_litigation_page_htm_file(self):
        expected_response_code = 200
        link = '/litigation/litreleases/2006/lr19955.htm'
        expected_url = 'https://www.sec.gov/litigation/litreleases/2006/lr19955.htm'

        response = Scraper.get_litigation_page(link)

        self.assertEqual(response.status_code, expected_response_code)
        self.assertEqual(response.url, expected_url)

if __name__ == '__main__':
    unittest.main()