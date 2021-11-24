from bs4 import BeautifulSoup
import requests

print('Print a skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date or 'today' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href']

        if unfamiliar_skill not in skills:
            print(f"Company Name: {company_name}")
            print(f"Required Skills: {skills}")
            print(f"More info: {more_info}")
            print('')
