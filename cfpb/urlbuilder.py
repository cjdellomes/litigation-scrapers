from datetime import date
from typing import List

class UrlBuilder:

    def __init__(self, base_url='', subdirectory=''):
        self.base_url = base_url
        self.sub_directory = subdirectory

    def build(self):
        return self.base_url + self.sub_directory

class EnforcementActionFilterUrlBuilder(UrlBuilder):

    def __init__(self, base_url='', page_number=0, categories=[], statuses=[], from_date=None, to_date=None):
        super().__init__(base_url=base_url)
        self.page_number(page_number)
        self.categories(categories)
        self.statuses(statuses)
        self.from_date(from_date)
        self.to_date(to_date)

    def build(self):
        return (self.base_url
                + '/?'
                + self.page_number
                + self.categories
                + self.statuses
                + self.from_date
                + self.to_date)

    def page_number(self, page_number: int):
        self.page_number = ''
        if page_number <= 0:
            return
        self.page_number = '&page=' + str(page_number)
        
    def categories(self, categories: List[str]):
        self.categories = ''
        if categories is None:
            return
        for category in categories:
            self.categories += '&categories=' + category

    def statuses(self, statuses: List[str]):
        self.statuses = ''
        if statuses is None:
            return
        for status in statuses:
            self.statuses += '&statuses=' + status

    def from_date(self, from_date: date):
        self.from_date = ''
        if from_date is None:
            return
        self.from_date = '&from_date=' + from_date.isoformat()

    def to_date(self, to_date: date):
        self.to_date = ''
        if to_date is None:
            return
        self.to_date = '&to_date=' + to_date.isoformat()