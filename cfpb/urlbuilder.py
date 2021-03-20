from datetime import date
from typing import List

class UrlBuilder:

    def __init__(self, base_url='', subdirectory=''):
        self.url = base_url + subdirectory

    def build(self):
        return self.url

class EnforcementActionFilterUrlBuilder(UrlBuilder):

    def __init__(self, base_url='', page_number=0, categories=[], statuses=[], from_date=None, to_date=None):
        super().__init__(base_url=base_url)
        self.url += '/?'
        self.page_number(page_number)
        self.categories(categories)
        self.statuses(statuses)
        self.from_date(from_date)
        self.to_date(to_date)

    def page_number(self, page_number: int):
        if page_number <= 0:
            return
        self.url += '&page=' + str(page_number)
        
    def categories(self, categories: List[str]):
        if categories is None:
            return
        for category in categories:
            self.url += '&categories=' + category

    def statuses(self, statuses: List[str]):
        if statuses is None:
            return
        for status in statuses:
            self.url += '&statuses=' + status

    def from_date(self, from_date: date):
        if from_date is None:
            return
        self.url += '&from_date=' + from_date.isoformat()

    def to_date(self, to_date: date):
        if to_date is None:
            return
        self.url += '&to_date=' + to_date.isoformat()