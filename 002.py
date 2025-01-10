total=0
a=1
b=1
while b<4000000:
    c=a+b
    a=b
    b=c
    if b%2==0:
        total+=b
print(total)


