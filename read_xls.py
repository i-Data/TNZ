import csv
import re

locations1 = []
locations2 = []

with open('/Users/chengzhang/OneDrive/YouJustGo/Itenaries/area-unit-2013-classification-v1-0.txt', 'r') as f:
    text = csv.reader(f, delimiter = '\t')

    for code, name in text:
        locations1.append(re.sub(r' ', '-', name.lower()))

with open('/Users/chengzhang/OneDrive/YouJustGo/Itenaries/area-unit-2013-classification-v1-0.txt', 'r') as f:
    text = csv.reader(f, delimiter='\t')

    for code, name in text:
        for i in re.findall(r"[\w']+", name.lower()):
            locations2.append(i)




locations_admin = ['Abel-Tasman-National-Park', 'Akaroa', 'Apiti', 'Arthurs-Pass', 'Ashurst', 'Auckland', 'Blenheim', 'Cape-Kidnappers', 'Cape-Reinga', 'Cardrona Alpine Resort',
'Christchurch',
'Coromandel',
'Dargaville',
'Dunedin',
'Fox Glacier',
'Franz Josef Glacier',
'Gisborne',
'Gore',
'Greymouth',
'Haast',
'Hahei',
'Half Moon Bay',
'Hamilton',
'Hanmer Springs',
'Hastings',
'Hobbiton',
'Hokianga',
'Hokitika',
'Invercargill',
'Jacksons',
'Kaikoura',
'Kaitaia',
'Kaiteriteri',
'Kauri Cliffs',
'Kerikeri',
'Lake Tekapo',
'Mangaweka',
'Mangonui',
'Martinborough',
'Masterton',
'Matamata',
'Matauri Bay',
'Milford Sound',
'Motueka',
'Mount Cook',
'Murchison',
'Napier',
'National Park',
'Nelson',
'New Plymouth',
'Oamaru',
'Ohakune',
'Opotiki',
'Paihia',
'Palmerston North',
'Picton',
'Piha',
'Pukaki',
'Punakaiki',
'Puponga',
'Queenstown',
'Rakopi',
'Rotorua',
'Russel',
'Somes Island',
'St Arnaud',
'Stewart Island',
'Tata Beach',
'Taupo',
'Tauranga',
'Te Anau',
'Te Araroa',
'Tekapo',
'Thames',
'The Mahia',
'The Remarkables',
'Turangi',
'Turoa',
'Twizel',
'Waiheke Island',
'Waikaremoana',
'Waipoua Forest',
'Waipoua Kauri Forest',
'Waitomo',
'Wanaka',
'Wellington',
'Westport',
'Whakapapa',
'Whakatane',
'Whangamata',
'Whanganui',
'Whangarei',
'Whangaruru',
'Whataroa',
'White Island',
'Whitianga']

locations3 = []
locations4 = []

for i in locations_admin:
    locations3.append(re.sub(r' ', '-', i.lower()))

for i in locations_admin:
    for j in re.findall(r"[\w']+", i.lower()):
        locations4.append(j)


locations_a = locations1 + locations2
locations_b = locations3 + locations4

locations = set(locations_b) - set(locations_a)

f_locations = list(locations)



