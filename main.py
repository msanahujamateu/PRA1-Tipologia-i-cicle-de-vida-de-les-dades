import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib import robotparser

if __name__ == '__main__':
    url_scrap = 'https://pitchfork.com/best/'
    url_robots = 'https://pitchfork.com/robots.txt'
    url_site = 'https://pitchfork.com'

    # Check de l'arxiu robots.txt
    rp = robotparser.RobotFileParser()
    rp.set_url(url_robots)
    rp.read()
    # print(rp.crawl_delay("*"))
    # print(rp.can_l_delay("*"))
    # print(rp.can_fetch("*", url_scrap))

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

    # print(BeautifulSoup(str(reviews[0]), 'lxml'))

    artista, titol, genere, url, tipus, imatge = [], [], [], [], [], []

    for artist in soup.find_all('ul', class_="artist-list"):
        artista.append(artist.text)

    for titl in soup.find_all('h3', class_="bnm-hero__title"):
        titol.append(titl.text)

    for titl in soup.find_all('h2', class_="title"):
        titol.append(titl.text)

    for genl in soup.find_all('ul', class_="genre-list genre-list--inline bnm-hero__genre-list"):
        genere.append(genl.text)

    for genl in soup.find_all('ul', class_="genre-list genre-list--inline"):
        genere.append(genl.text)

    for div in soup.find_all('a', class_="bnm-hero__link-block"):
        url.append(url_site + div.attrs['href'])

    for div in soup.find_all('a', class_="link-block"):
        url.append(url_site + div.attrs['href'])

    for urll in url:
        if urll.find("/albums/") > 0:
            tipus.append("album")
        elif urll.find("/tracks/") > 0:
            tipus.append("track")
        else:
            tipus.append("")

    for divv in soup.find_all('div', class_="artwork"):
        imatge.append(divv.find('img').attrs['src'])

    genere.insert(16, '')  # Missing genre in web

    data_dict = {'artist': artista, 'title': titol, 'genre': genere, 'url': url, 'type' : tipus, 'image' : imatge}

    print(len(artista))

    print(len(titol))  # Three of them have class bnm-hero__title, label h3

    print(len(genere))

    print(len(url))

    print(len(tipus))

    print(len(imatge))

    df = pd.DataFrame(data_dict)

    df.to_csv(r'dataset.csv', index=False)
