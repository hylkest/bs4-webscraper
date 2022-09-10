# Python webscraper

import requests
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import mysql.connector
import re

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="webscraper"
)

req = Request("https://google.com")
html_page = urlopen(req)
main_link = "https://google.com"

soup = BeautifulSoup(html_page, "html.parser")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
    new_lst = ('"'.join(links))
    mycursor = mydb.cursor()

    sql = "INSERT INTO links (main_link, link_scraped) VALUES (%s, %s)"
    val = (main_link, new_lst)
    mycursor.execute(sql, val)

new_lst=('"'.join(links))
print(new_lst)

mycursor = mydb.cursor()

# sql = "INSERT INTO links (main_link, link_scraped) VALUES (%s, %s)"
# val = (main_link, new_lst)
# mycursor.execute(sql, val)

mydb.commit()
