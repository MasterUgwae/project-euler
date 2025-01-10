
def isPrime(n):
    if n%1!=0: return False
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True
def find_prime_fact(n) -> set:
    factors = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.add(n)
    return factors
            

count=3
consec=0
while consec!=4:
    count+=1
    flag=True
    factors=find_prime_fact(count)
    if len(factors)==4:
        for i in find_prime_fact(count):
            print(i)
            if not isPrime(i):
                flag=False
        if flag:
            consec+=1
        else:
            consec=0
    else:
        consec=0
print(count-3)
