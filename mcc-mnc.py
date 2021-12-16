import urllib.request
from bs4 import BeautifulSoup
import csv
import ssl

# hdr = {'User-Agent': 'Mozilla/5.0'}
# context = ssl._create_unverified_context()
url = 'http://www.mcc-mnc.com/'
req = urllib.request.Request(url)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

target = soup.find('table', {'id': 'mncmccTable'})
tbody = target.find('tbody')
thead = target.find_all('th')
trData = tbody.find_all('tr')

theadlist = []
theadlen = len(thead)

for i in range(0, theadlen):
    th = target.find_all('th')[i].text
    theadlist.append(th)

rowList = []
colList = []

trDatalen = len(trData)
for i in range(0, trDatalen):
    tdData = trData[i].find_all('td')
    tdDatalen = len(tdData)

    for j in range(0, tdDatalen):
        element = tdData[j].text
        colList.append(element)

    rowList.append(colList)
    colList = []

with open('mcc-mnc_list.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(theadlist)
    writer.writerows(rowList)