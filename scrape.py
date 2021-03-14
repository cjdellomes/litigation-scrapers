import re
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.sec.gov/litigation/litreleases/litrelarchive/litarchive2006.shtml")

soup = BeautifulSoup(r.text, 'html.parser')

for a in soup.find_all('a', href=True):
    if (re.search("\/litigation\/litreleases\/\d*\/.*.htm", a['href'])):
        print("Found the URL: ", a['href'])