import urllib
import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup



db = pymysql.connect(host='localhost', user='yildbs', passwd='1234',db ='test',charset='utf8',autocommit=True)

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print("Database version : ", data)

db.close()