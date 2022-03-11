import requests
from bs4 import BeautifulSoup as bs
import json



# pers_ur_list=[]
# for i in range(0,700,20):
#     url=f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}'
#     q=requests.get(url)
#     result=q.content
#     soup=bs(result,'lxml')
#     persons=soup.find_all(class_='bt-open-in-overlay')

#     for person in persons:
#         person_page_url=person.get('href')
#         pers_ur_list.append(person_page_url)
# with open('person_list.txt','a',encoding='utf-8') as file:
#     for l in pers_ur_list:
#         file.write(f'{l}\n')

with open('person_list.txt',encoding='utf-8') as file:
    lines=[line.strip() for line in file.readlines()]

    data_dct=[]
    for line in lines:
        print(lines)
        q=requests.get(line)
        result = q.content
        
        soup=bs(result,'lxml')
        person=soup.find(class_='bt-biografie-name').find('h3').text
        person_name_comp=person.strip().split(',')
        # print(person_name_comp)
        person_name=person_name_comp[0]
        person_company=person_name_comp[1]
        social_networks=soup.find_all(class_='bt-link-extern')
        social_networks_url=[]
        for item in social_networks:
            social_networks_url.append(item.get('href'))

        data={
            'person_name':person_name,
            'person_company':person_company,
            'social_networks_url':social_networks_url

        }
        data_dct.append(data)

        with open('data.json','w',encoding='utf-8') as file:
            json.dump(data_dct,file,indent=4,ensure_ascii=False)

