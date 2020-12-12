import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

url = "https://archive.org/download/DubTheNet"

ext = ".mp3"

params ={}

result = []

response = requests.get(url, params=params)
  
if response.ok:
    response_text = response.text
else:
    print("IO Error")

soup = BeautifulSoup(response_text, 'html.parser')
parent = [url + node.get('Dub') for node in soup.find_all('a') if node.get('Dub').endswith(ext)]       

for elem2 in parent:
    elem = str(elem2)
    if ("_64kb" not in elem) and ("glogo" not in elem) and ("_thumb" not in elem) and (len(elem)<100):
        result.append(elem)

print(result)
