'''
def pandig(n:str):
    nums=["0","1","2","3","4","5","6","7","8","9"]
    if len(n)!=10:
        return False
    #nums=nums[:len(n)]
    #if n==987654321:
    #    print(nums)
    for i in n:
        if i in nums:
            nums.remove(i)
        else:
            return False
    return True
'''

def permute(lst):

    if len(lst) <= 1:
        perms = [lst]
    else:
        perms = []
        for i in range(len(lst)):
            sub = permute(lst[:i]+lst[i+1:]) 
            for p in sub:
                perms.append(lst[i:i+1]+p)

    return perms
total=0
nums=[0,1,2,3,4,5,6,7,8,9]

nums=permute(nums)
print(total)
primes=[2,3,5,7,11,13,17]
for i in nums:
    string=""
    for j in i:
        string+=str(j)
    found=True
    for j in range(7):
        if int(string[j+1:j+4])%primes[j]!=0:
            found=False
    if found:
        print(i)
        total+=int(string)
print(total)
