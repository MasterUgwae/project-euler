def f(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    return factorial
total=0
for i in range(3,10000000):
    digitSum=0
    for j in str(i):
        digitSum+=f(int(j))
    if digitSum==i:
        total+=i
print(total)
