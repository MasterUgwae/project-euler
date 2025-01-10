
def isPrime(n):
    if n==2 or n==3: 
        return True
    if n%2==0 or n<2: 
        return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False

    return True
primes=0
for i in range(2,1000000):
    string=str(i)
    circ=True
    for j in range(len(string)):
        if not isPrime(int(string)):
            circ=False
            break
        string = string[1:] + string[0]
    if circ:
        primes+=1
print(primes)
