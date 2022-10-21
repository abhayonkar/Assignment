from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://getlatka.com/saas-companies"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")

a = soup.find_all("table", class_="data-table_table__SwBLY")

print("Number of tables on site: ",len(a))

a1 = [None]*100

a1 = soup.findAll("table", class_="data-table_table__SwBLY")[0]

table_rows = a1.find_all("tr")

head = table_rows[1]
headings = []
for item in head.find_all("th"):
    item = (item.text).rstrip("\n")
    headings.append(item)

companies = []
for tr in table_rows:
    com = tr.find_all("td")
    row_demo = [tr.text for tr in com]
    companies.append(row_demo) 

com2 = pd.DataFrame(data=companies,columns=headings)  