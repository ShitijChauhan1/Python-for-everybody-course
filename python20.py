import re
count = 0 
tot = 0
hand = open('py20.txt')
numlist = list()
for line in hand:
    stuff = re.findall('[0-9]+', line)
    for values in stuff:
        intval = int(values)
        count = count + 1
        tot = tot + intval

   
print (tot)