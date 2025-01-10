maxSol=0
maxP=0
for i in range(2,1001):
    print(i)
    pSol=0
    for j in range(1,i):
        for k in range(1,i-j):
            if j**2+k**2==(i-j-k)**2:
                pSol+=1
    if pSol>maxSol:
        maxSol=pSol
        maxP=i
print(maxP)

