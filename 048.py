num=0
for i in range(1,1001):
    num+=i**i
print(str(num)[len(str(num))-10:])
