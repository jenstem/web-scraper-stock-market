import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://ticker.finology.in/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# Test if website is accessible or not by uncommenting first
# print(r)