import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


def crawlOnePage(url):
    content = urlopen(url)
    soup = BeautifulSoup(content, 'lxml')

    urlPrefix = url[:url.index('.') + url[url.index('.'):].index('/')]

    nextPageLink = soup.find('a', attrs={'class': 'next'})
    if( nextPageLink is not None ):
        nextPageLink = urlPrefix + nextPageLink['href']

    data = []

    titles = soup.findAll('td',attrs={'class':'title'})
    dates = soup.findAll('td', attrs={'class':'num'})
    rates = soup.findAll('div',attrs={'class':'rating_type'})
    num = len(titles)

    for i in range(num):
        title = titles[i].find('a').text
        link = urlPrefix + titles[i].find('a')['href']
        date = dates[i].text
        rate = rates[i].find('strong').text

        data.append([title, date, rate, link])

    return data, nextPageLink
    #return data, None



def crawlOneWebtoon(url):
    nextPageLink = url

    data = []
    while(True):
        _data, nextPageLink = crawlOnePage(nextPageLink)

        for datum in _data:
            data.append(datum)

        if(nextPageLink is None):
            break

    return data