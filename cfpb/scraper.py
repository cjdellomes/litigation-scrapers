import requests
from datetime import datetime
from typing import List

class Scraper:
    cfpb_base_url = 'https://www.consumerfinance.gov'
    enforcement_actions_url = cfpb_base_url + '/enforcement/actions'
    press_releases_url = cfpb_base_url + '/about-us/newsroom'

    def __init__(self, categories:List[str], statuses:List[str], from_date:datetime, to_date:datetime):
        self.categories = categories
        self.statuses = statuses
        self.from_date = from_date
        self.to_date = to_date

    def get_enforcement_action_search_page():
        response = requests.get(Scraper.enforcement_actions_url)
        return response