def isPrime(n) -> bool:
    if n%1!=0: return False
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True
def permute(n:list)->list:
    if len(n)==1:
        return [n]
    perm_list = []
    for i in permute(n[1:]):
         for j in range(len(n)):
            perm_list.append(i[:j]+n[0:1]+i[j:])

    return perm_list
def list2int(lst:list)->int:
    return sum([int(i)*10**index for index,i in enumerate(lst)])
arith_perms=[]
allPerms=[]
for i in range(1000,10000):
    if isPrime(i):
        flag=True
        strperms=sorted(permute([j for j in str(i)]))
        perms=[]
        for j in strperms:
            if len(str(list2int(j)))==4:
                perms.append(list2int(j))
        perms.sort()
        if i==1487:
            print(perms)
        for j in range(len(perms)):
            for k in range(1,j):
                thirdNum=2*perms[j]-perms[k]
                if perms[k]==1487 and perms[j]==4817:
                    print(perms[k],perms[j],thirdNum)
                if thirdNum in perms and perms[k]!=perms[j] and 2*perms[j]-perms[k]>0:
                    print(perms[j]-perms[k])

                    print(perms[k],perms[j],2*perms[j]-perms[k])
                    if sorted([perms[k],perms[j],thirdNum]) not in arith_perms and len(str(thirdNum)+str(perms[j])+str(perms[k]))==12:
                        #print(len(thirdNum+perms[j]+perms[k]))
                        arith_perms.append(sorted([perms[k],perms[j],thirdNum]))
arith_perms.sort()
print(arith_perms)

for i in arith_perms:
    prime=True
    for j in i:
        if not isPrime(j):
            prime=False
    if prime:
        print(i)
