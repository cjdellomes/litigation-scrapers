import re
from bs4 import BeautifulSoup

class Parser:

    @staticmethod
    def get_enforcement_action_detail_links(html:str):
        soup = BeautifulSoup(html, 'html.parser')

        litigation_links = []

        for a in soup.find_all('a', href=True):
            if (re.search('\/enforcement\/actions\/.*/', a['href'])):
                litigation_links.append(a['href'])
        
        return litigation_links