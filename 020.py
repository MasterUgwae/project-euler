factorial = 1

n=100

for i in range(1,n+1):
    factorial*=i

total=0

for i in str(factorial):
    total+=int(i)#

print(total)
