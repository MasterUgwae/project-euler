import math

def d(n):
    factors = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            factors.append(i)

    return sum(factors)

total=0
for i in range(1,10000):
    if i==220:
        print(i,d(i),d(d(i)))
    if d(d(i))==i and d(i)!=i:
        total+=i

print(total)

