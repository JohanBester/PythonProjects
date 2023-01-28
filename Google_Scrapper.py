# Google Pic Search Scrapper

from typing import cast
import requests
from bs4 import BeautifulSoup as bs

site_search = 'https://www.google.com/search?q='
search_term = input('Input Search Term: ')
url_term = search_term.replace(" ", "+")
search_url = site_search+url_term
url = site_search+url_term+'&tbm=isch'
print(url)
r = requests.get(url)
soup = bs(r.content, 'html5lib')     ##'html.parser'
total_links = 0
link_list = []
raw_list = []

for link in soup.find_all('a'):
    ahref = link.get('href')
    raw_list.append(ahref)

    # link_href = 'https://www.google.com'+ahref
    # link_list.append(link_href)

    total_links += 1
    print('\n' + str(total_links) + "    " + ahref)

print("\n\nTotal number of links: " + str(total_links) + "\n")
# print(link_list)
print(raw_list)
