def summed(a:int,b:int)->int:
    return sum(int(i) for i in str(a**b))

maxSum=0
for a in range(1,100):
    for b in range(100):
        t=summed(a,b)
        if t>maxSum:
            maxSum=t
print(maxSum)
