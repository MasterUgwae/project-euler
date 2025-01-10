def isPrime(n):
    if n%1!=0: return False
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True

found=0
i=1
while found<1:
    i+=2
    if not isPrime(i):
        flag=False
        for j in range(1,int((i**0.5)+1)):
            if i==5777:
                print(j,i-(2*(j**2)),isPrime(i-(2*(j**2))))
            if isPrime(i-(2*(j**2))):
                flag = True
        if not flag:
            print(i)
            found+=1

