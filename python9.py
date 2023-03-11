def computepay(h, r) :
    if h > 40 :
        nt = h * r
        ot = (h - 40) * (r * 0.5)
        answer = ot + nt
    else :
        answer = h * r
    return answer

hrs = input("Enter Hours: ")
h = float(hrs)
rph = input("Enter Rate: ")
r = float(rph)
p = computepay(h, r)
print("Pay", p)




