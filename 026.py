
def recipPeriod(prime):
    remainders = []
    remainder = 1
    while True:
        remainder = (remainder * 10) % prime
        if remainder in remainders:
            return len(remainders) - remainders.index(remainder)
        remainders.append(remainder)


def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False

    return True

   

maxRecip=0

for i in range(1,1000):
    if isPrime(i):
        if recipPeriod(i)==i-1:
            maxRecip=i


print(maxRecip)
