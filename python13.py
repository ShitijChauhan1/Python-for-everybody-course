fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    if not line.startswith('From ') :
        continue
    else:
        line = line.rstrip()
        words = line.split()
        count = count + 1
        print(words[1])
    
        


print("There were", count, "lines in the file with From as the first word")