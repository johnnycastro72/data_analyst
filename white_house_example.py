import requests
import lxml
import cchardet
from bs4 import BeautifulSoup
import time

start_time = time.time()
result = requests.get("https://www.whitehouse.gov/briefings-statements/")

#print(result.status_code)
#print(result.headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    if h2_tag.find('a') != None:
        a_tag = h2_tag.find('a')
        urls.append(a_tag.attrs['href'])

print(urls)

stop_time = time.time()
print(f"Runtime of the script is {stop_time - start_time}")