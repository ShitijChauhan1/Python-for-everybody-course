largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        inputt = int(num)
    except : 
        print('Invalid input')
    if smallest == None :
        smallest = inputt 
    elif smallest > inputt :
        smallest = inputt
    if largest == None :
        largest = inputt
    elif largest < inputt :
        largest = inputt
print ('Maximum is', largest)
print ('Minimum is', smallest)

    
        
  

