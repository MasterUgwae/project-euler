
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False

    return True
def pandig(n:str):
    nums=["1","2","3","4","5","6","7","8","9"]
    #if len(n)!=9:
    #    return False
    nums=nums[:len(n)]
    if n==987654321:
        print(nums)
    for i in n:
        if i in nums:
            nums.remove(i)
        else:
            return False
    return True
maxNum=0
for i in range(1000,100000000):
    if pandig(str(i)):
        if isPrime(i):
            maxNum=i
print(maxNum)
