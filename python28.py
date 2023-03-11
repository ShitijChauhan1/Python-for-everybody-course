import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
import ssl

sum = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1684249.xml"
print('Retreaving: ', url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved: ', len(data), 'characters')
data.decode()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
icount = len(lst)
for counts in lst:
    sum += float(counts.find('count').text)
print(sum)
print(icount)



