# Python webscraper


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import mysql.connector
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import mysql.connector

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
mycursor = mydb.cursor()

for link in soup.findAll('a'):
    sql = "INSERT INTO links (main_link, link_scraped) VALUES (%s, %s)"
    val = (main_link, link[0])
    mycursor.execute(sql, val)
    mydb.commit()

#
# sql = "INSERT INTO links (main_link, link_scraped) VALUES (%s, %s)"
# val = (main_link, new_lst)
# mycursor.execute(sql, val)

