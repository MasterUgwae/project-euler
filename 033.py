den=[]
nume=[]
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
for i in range(10,100):
    for j in range(10,100):
        if (str(i)[0] in str(j) or str(i)[1] in str(j)) and ("0" not in str(j)) and "0" not in str(i) and i>j:
            if str(i)[0] in str(j):
                cancelledi=int(str(i)[1])
            else:
                cancelledi=int(str(i)[0])

            if str(j)[0] in str(i):
                cancelledj = int(str(j)[1])
            else:
                cancelledj = int(str(j)[0])
            if j/i == cancelledj/cancelledi:
                den.append(i)
                nume.append(j)

denominator = 1
numerator = 1
for i in range(len(den)):
    denominator*=den[i]
    numerator*=nume[i]

print(denominator/gcd(numerator,denominator))

