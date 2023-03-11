import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Aleksander.html"
position = int(input("Enter position:"))-1
count = int(input("Enter count:"))

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


Sequence = []
tags = soup('a')

for i in range(count):
    link = tags[position].get('href', None)
    print('Retrieving: ', link)
    Sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html ,'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(Sequence[-1])