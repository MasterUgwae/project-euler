maxPrimeSeries=0
def isPrime(n) -> bool:
    if n%1!=0: return False
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True



primes=[]
i=2
while sum(primes)<1000000:
    if isPrime(i):
        primes.append(i)
    i+=1
print(sum(primes))

primeSums=[]
l=len(primes)
j=l
while j!=0:
    i=0
    while i+j<l+1:
        seq= primes[i:i+j]
        if sum(seq)<=1000000:
            if isPrime(sum(seq)):
                if len(seq)>len(primeSums):
                    primeSums=seq
        i=i+1
    j=j-1

print(sum(primeSums))
