from pymongo import MongoClient
import pprint
from bs4 import BeautifulSoup
import requests
import time
import random

client = MongoClient('localhost', 27017)
db = client['eia_data']

#Put everything together for oil production, gas production, and gas flare
main_oil_url = 'https://www.eia.gov/dnav/pet/pet_crd_crpdn_adc_mbbl_a.htm'
main_ngf_url = 'https://www.eia.gov/dnav/ng/ng_prod_sum_a_EPG0_VGV_mmcf_a.htm'
main_ngp_url = 'https://www.eia.gov/dnav/ng/ng_prod_sum_a_EPG0_FGW_mmcf_a.htm'
pages = [main_oil_url, main_ngp_url, main_ngf_url]
sub_pages = ['https://www.eia.gov/dnav/pet', 'https://www.eia.gov/dnav/ng', 'https://www.eia.gov/dnav/ng']

#initialize collection based on data sets
oil_produced = db['oil_produced']
natural_gas_produced = db['natural_gas_produced']
natural_gas_flared = db['natural_gas_flared']

collections = [oil_produced, natural_gas_produced, natural_gas_flared]

for idx, url in enumerate(pages):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    d={}
    for row in soup.find_all('tr', class_ = 'DataRow'):
        #State
        if row.find(class_='DataStub1') == None:
            continue
        state = row.find(class_='DataStub1').text
        state = state.replace('.', '')
        state = state.lower()
        #Sublink for historical data
        link = row.find('a')['href'][1:]
        sub_link = sub_pages[idx] + link
        sub_page = requests.get(sub_link)
        sub_soup = BeautifulSoup(sub_page.text, 'html.parser')
        data = sub_soup.find_all(class_='B3')
        n = len(data)
        all_data = [sub_soup.find_all(class_ = 'B3')[i].text.strip() for i in range(len(data))]
        d[state] = all_data
        #print(d)
        slp = random.randint(1,3)
        time.sleep(slp)
    #add state:data dict to mongo db
    collections[idx].insert_one(d)
    #print(d)
    #print('______________________________________________')
    
        
    time.sleep(20)

