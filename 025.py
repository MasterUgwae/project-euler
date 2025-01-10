a=1
b=1
count=2
while len(str(a))<1000:
    c=a+b
    b=a
    a=c
    count+=1
print(count)
