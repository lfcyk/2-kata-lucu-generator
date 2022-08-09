import requests
from bs4 import BeautifulSoup
url = "https://www.kbbi.co.id/daftar-kata?page="
s = ""
n=107 #107
for i in range(1,n):
    link = url + str(i)
    # print(link)
    page = requests.get(link)
    soup = BeautifulSoup(page.text,'lxml')
    table = soup.find('div', class_='row')
    infos = table.find_all('a')
    # print(infos[0].text)
    for info in infos:
        s =s + "\"" + info.text + "\"" + ', '

# print(s)
f = open('lib.txt','w')
f.write(s)
f.close()