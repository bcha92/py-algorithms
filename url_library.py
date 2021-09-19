# Working with URLs with 'urllib' module

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    # __init__ method takes a website to scrape from a parameter
    def __init__(self, site):
        self.site = site
    # Used to call whenever you want to scrape data from the site
    def scrape(self):
        # urlopen() function makes a request to a website and
        # returns a response object that has its HTML stored
        # along with additional data.
        r = urllib.request.urlopen(self.site)
        # response.read() returns HTML from the Response object
        html = r.read()
        # BeautifulSoup parses the HTML
        sp = BeautifulSoup(html, 'html.parser')
        # find_all method returns iterable containing tag objects
        # it found.
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

# Example Input Values
news = "https://news.google.com/"
Scraper(news).scrape()
