from os import path
from pathlib import PurePath
import sys

from bs4 import BeautifulSoup
import requests

with open(path, 'r') as fh:
        content = fh.read()

container = soup.find(id='container')

content = container.get_text()

d = {}

d[path] = content.strip() if content is not None else ''

unserialized = d

l = []

with open('urls.txt', 'r') as fh:
    urls = fh.readlines()
urls = [url.strip() for url in urls]

paths = download_urls(urls, '.')

paths = []

for url in urls:
    file_name = PurePath(url).name
    file_path = path.join(dir, file_name)
    text = ''

    try:
        response = requests.get(url)
        if response.ok:
            text = response.text
        else:
            print('Bad response for', url, response.status_code)
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
with open(file_path, 'w') as fh:
    fh.write(text)

paths.append(file_path)

paths = paths(urls, '.')



for path in paths:
    print('Written to', path)
    l.append(run_single(path))

print(l)