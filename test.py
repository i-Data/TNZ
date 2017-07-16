import requests
from bs4 import BeautifulSoup
import read_xls



locations = ['levin', 'otaki']




def tnz_spider(places):
    for place in places:
        url = "http://www.newzealand.com/cn/" + place
        source_code = requests.get(url)

        plain_text = source_code.text

        soup = BeautifulSoup(plain_text, "lxml")
        pi = open('place_info_v2.txt', "a+")
        for link in soup.findAll('p',{'class':'intro text-left'}):
            text = link.string
            pi.write(text + '\t' + url + '\n')
            # print(text)

        pi.close()

            # print(url)

tnz_spider(read_xls.f_locations)

