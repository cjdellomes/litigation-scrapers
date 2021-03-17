import requests
from datetime import date
from typing import List

class Scraper:
    cfpb_base_url = 'https://www.consumerfinance.gov'
    enforcement_actions_url = cfpb_base_url + '/enforcement/actions'
    press_releases_url = cfpb_base_url + '/about-us/newsroom'

    def __init__(self, categories: List[str], statuses: List[str], from_date: date, to_date: date):
        self.categories = categories
        self.statuses = statuses
        self.from_date = from_date
        self.to_date = to_date

    def get_enforcement_action_search_page(self):
        return requests.get(Scraper.enforcement_actions_url)

    def get_enforcement_action_filtered_page(self, page_number: int):
        url = self.enforcement_actions_url + '/?'

        url = self._add_page_number_to_url(url, page_number)
        url = self._add_categories_to_url(url, self.categories)
        url = self._add_statuses_to_url(url, self.statuses)
        url = self._add_from_date_to_url(url, self.from_date)
        url = self._add_to_date_to_url(url, self.to_date)

        return requests.get(url)

    def _add_page_number_to_url(self, url: str, page_number: int):
        if page_number <= 0:
            return url
        return url + 'page=' + str(page_number)
    
    def _add_categories_to_url(self, url: str, categories: List[str]):
        if categories is None:
            return url
        for category in categories:
            url += '&categories=' + category
        return url

    def _add_statuses_to_url(self, url: str, statuses: List[str]):
        if statuses is None:
            return url
        for status in statuses:
            url += '&statuses=' + status
        return url

    def _add_from_date_to_url(self, url: str, from_date: date):
        if from_date is None:
            return url
        return url + '&from_date=' + from_date.isoformat()

    def _add_to_date_to_url(self, url: str, to_date: date):
        if to_date is None:
            return url
        return url + '&to_date=' + to_date.isoformat()