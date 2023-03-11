rawster = input('enter a number') 
try : 
    ival = int(rawster)
except:
    ival = -1

if ival > 0 :
    print ("Nice work")
else : 
    print ("not a number")
