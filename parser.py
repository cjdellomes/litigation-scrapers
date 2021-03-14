import re
from bs4 import BeautifulSoup

class Parser:
    
    @staticmethod
    def get_litigation_links(html:str):
        soup = BeautifulSoup(html, 'html.parser')

        litigation_links = []

        for a in soup.find_all('a', href=True):
            if (re.search('\/litigation\/litreleases\/.*[.htm|.txt]', a['href'])):
                litigation_links.append(a['href'])
        
        return litigation_links