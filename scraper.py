import requests
from datetime import datetime

class Scraper:
    sec_base_url = 'https://www.sec.gov'
    sec_litigation_base_url = sec_base_url + '/litigation/litreleases'
    current_year_litigation_url = sec_litigation_base_url + '.htm'
    archive_base_url = sec_litigation_base_url + '/litrelarchive/litarchive'

    @staticmethod
    def get_year_page(year:int):
        if year == datetime.today().year:
            url = Scraper.current_year_litigation_url
        else:
            url = Scraper.archive_base_url + str(year) + '.shtml'
        response = requests.get(url)
        return response