def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False

    return True

maxSeq=0
maxAB=0
for i in range(-999,1000):
    for j in range(-1000,1001):
        count=0
        check = isPrime(count**2+i*count+j)
        while check:
            count+=1
            check = isPrime(count**2+i*count+j)
        if count>maxSeq:
            maxSeq=count
            maxAB=i*j

print(maxSeq,maxAB)
