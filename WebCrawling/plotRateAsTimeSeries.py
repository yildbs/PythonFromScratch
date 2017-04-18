import crawlOneWebtoon
import datetime as dt
import matplotlib.pyplot as plt

url = 'http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue'
url_denma = 'http://comic.naver.com/webtoon/list.nhn?titleId=119874&weekday=fri'

data = crawlOneWebtoon.crawlOneWebtoon(url_denma)

for datum in data:
    print(datum)

x_data, y_data = [], []

for datum in data:
    times = dt.datetime.strptime(datum[1],'%Y.%m.%d')
    x_data.append(times)
    y_data.append(datum[2])

plt.plot(x_data, y_data, linestyle='-', marker='o', label='value')

plt.xlabel('time')
plt.ylabel('rate')
plt.show()

