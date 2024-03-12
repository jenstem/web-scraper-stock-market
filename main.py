import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://ticker.finology.in/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# Test if website is accessible or not by uncommenting first
# print(r)

# Titles of the table
table = soup.find("table",class_ = "table table-sm table-hover screenertable")
headers = table.find_all("th")

titles = []

for i in headers:
    title = i.text
    titles.append(title)

df = pd.DataFrame(columns = titles)

# Data of the table
rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv("stock_market_data.csv")