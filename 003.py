
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False

    return True


prime=600851475143
factors=set()
for i in range(2,int(prime**0.5) +1):
    if isPrime(i) and prime%i==0:
        factors.add(i)

print(max(factors))
