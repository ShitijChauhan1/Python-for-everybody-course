import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
x = BeautifulSoup(html, 'html.parser')

list = []
sum = 0
tags = x('span')
for tag in tags:
    line = tag.contents[0]
    numbers = int(line)
    sum = sum + numbers
print(sum)
