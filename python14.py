fname = input("Enter file name: ")
fh = open(fname)
data = []
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words :
        if word not in data:
            data.append(word)

print(sorted(data))