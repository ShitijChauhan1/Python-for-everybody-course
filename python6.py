hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate per hour:")
r = float(rph)
answer = 0
if h >=40 :
   nt = h * r
   ot = (h - 40) * (r * 0.5)
   answer = nt + ot;

else :
   answer = h * r
print(answer)