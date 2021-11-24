import lxml
import cchardet
import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()
result = requests.get("https://www.google.com")

#print(result.status_code)
#print(result.headers)

src = result.content

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
#print(links)
#print("\n")

for link in links:
    if "About" in link.text or "acerca" in link.text:
        print(link)
        print(link.attrs['href'])
stop_time = time.time()
print(f"Runtime of the script is {stop_time - start_time}")
