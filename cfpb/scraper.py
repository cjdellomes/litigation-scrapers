import requests
from datetime import date
from typing import List
import urlbuilder

class Scraper:
    cfpb_base_url = 'https://www.consumerfinance.gov'
    enforcement_actions_url = cfpb_base_url + '/enforcement/actions'
    press_releases_url = cfpb_base_url + '/about-us/newsroom'

    def __init__(self, categories: List[str], statuses: List[str], from_date: date, to_date: date):
        self.categories = categories
        self.statuses = statuses
        self.from_date = from_date
        self.to_date = to_date

    def get_enforcement_action_filter_page(self):
        url_builder = urlbuilder.UrlBuilder(base_url=self.enforcement_actions_url)

        return requests.get(url_builder.build())

    def get_enforcement_action_filtered_page(self, page_number: int):
        url_builder = urlbuilder.EnforcementActionFilterUrlBuilder(
            base_url=self.enforcement_actions_url,
            page_number=page_number,
            categories=self.categories,
            statuses=self.statuses,
            from_date=self.from_date,
            to_date=self.to_date)

        return requests.get(url_builder.build())