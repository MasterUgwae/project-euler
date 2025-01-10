
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False

    return True

sumPrime=0
count=11
n=10
while count>0:
    string=str(n)
    #check prime
    if isPrime(n):
        prime=True
        #check L2R
        while len(string)>1 and prime == True:
            string=string[1:]
            if not isPrime(int(string)):
                prime=False
        #check left
        string=str(n)
        while len(string)>1 and prime == True:
            string=string[:len(string)-1]
            if not isPrime(int(string)):
                prime=False
        if prime:
            sumPrime+=n
            count-=1
    n+=1
print(sumPrime)
