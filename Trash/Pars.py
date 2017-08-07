#!/usr/bin/env python3

import urllib
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.urlopen(url)
    return response.read()

def parse(html):
    
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", "items_list")
    rows = table.find_all("tr")
    print(soup)
    print(table)

    print (rows)
    

if __name__ == '__main__':
    parse(get_html("http://weblancer.net/projects/"))
