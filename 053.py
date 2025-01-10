def factorial(n:int)->int:
    out=1
    for i in range(n):
        out*=i+1
    return out
count=0
for i in range(1,101):
    for j in range(1,i):
        if factorial(i)/(factorial(j)*factorial(i-j))>1_000_000:
            count+=1
print(count)
