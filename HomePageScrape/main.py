from selenium import webdriver
import bs4
import requests
import json

url = 'https://www.wayfair.com/a/lifestyle/get_next_page?page=3&_txid=otAgY1gzKbOJuwP1HqOHAg%3D%3D'


class ScrapeMobile(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)
        self.header = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
                       'Host': 'www.wayfair.com'}

    def scrape_links(self):
        #session = requests.Session()
        #session.headers = self.header
        #response = session.get(url)
        #response = response.text
        response = requests.post(url, self.header)
        #response = response.text
        #print(response.headers['content-type'])
        response = response.content
        #response = response.json()
        #print(type(response))

        soup = bs4.BeautifulSoup(response, 'html.parser')
        #print(soup)
        #quit()
        #soup = soup.prettify()

        clicklocations = []
        for each in soup.find_all(['a']):

            click = each.get('data-click-location')
            if click is not None:
                clicklocations.append(click)
        self.driver.quit()
        print(clicklocations)

if __name__ == '__main__':
    scraper = ScrapeMobile()
    scraper.scrape_links()
