import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib import robotparser

if __name__ == '__main__':
    url_scrap = 'https://pitchfork.com/best/'
    url_robots = 'https://pitchfork.com/robots.txt'

    # Check de l'arxiu robots.txt
    rp = robotparser.RobotFileParser()
    rp.set_url(url_robots)
    rp.read()
    print(rp.crawl_delay("*"))
    print(rp.can_fetch("*", url_scrap))

    # Create a Request object by gathering information from the URL below
    page = requests.get(url_scrap)

    # Check that the request worked (status code should be 200)
    print(page.status_code)

    soup = BeautifulSoup(page.content, 'lxml')
    # print(soup.prettify())

    # All the albums or tracks have the following class tags
    class_tags = ['bnm-hero__review-block', 'bnm-small album-small', 'bnm-small track-small', 'bnm-small album-small']

    reviews = soup.find_all('div', {'class': class_tags})

    print(len(reviews))

    print(BeautifulSoup(str(reviews[0]), 'lxml'))
