c = {'a':10, 'b':1, 'c':22}
tmp = []
for (k,v) in c.items():
    tmp.append((v,k))


tmp = sorted(tmp)
print(tmp)