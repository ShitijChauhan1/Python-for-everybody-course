text = "X-DSPAM-Confidence:    0.8475"
nit = text.find("0")
bit = text.find("5", nit)
line = text[nit:bit+1]
floww = float(line)
print(line)
