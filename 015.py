import math
nums=[]
n=20
for i in range(n+1):
    nums.append(math.comb(n,i))
    #print(i+1,n+1,math.comb(i+1,n+1))
print(nums)
while len(nums)>1:
    temp=[]
    for i in range(len(nums)-1):
        temp.append(nums[i]+nums[i+1])
    nums=temp

print(nums)

