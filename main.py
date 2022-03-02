import json
import requests
from bs4 import BeautifulSoup


# persons_urls = []

# for i in range(0, 736, 20):
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'

#     q = requests.get(url)
#     result = q.content

#     soup = BeautifulSoup(result, 'lxml')

#     persons = soup.find_all(class_='bt-open-in-overlay')

#     for person in persons:
#         person_url = person.get('href')
#         persons_urls.append(person_url)


# with open('persons.txt', 'a') as file:
#     for line in persons_urls:
#         file.write(f'{line}\n')

with open('persons.txt') as file:

    lines = [line.strip() for line in file.readlines()]

    count = 0
    data_dict = []
    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')

        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_='bt-link-extern')

        social_networks_url = []

        for item in social_networks:
            social_networks_url.append(item.get('href'))

        data = {
            'name': person_name,
            'company': person_company,
            'url_networks': social_networks_url
        }
        count +=1
        print(f'#{count} completed !')
        data_dict.append(data)

        with open('data.json', 'w') as file_json:
            json.dump(data_dict, file_json, indent = 4)
