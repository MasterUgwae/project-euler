def numerator(x:int)->int:
    a=1
    b=3
    for i in range(x):
        c=b*2+a
        a=b
        b=c
    return b

def denominator(x:int)->int:
    x+=1
    a=0
    b=1
    for i in range(x):
        c=b*2+a
        a=b
        b=c
    return b
count=0
for i in range(0,1000):
    if len(str(numerator(i)))>len(str(denominator(i))):
        count+=1
print(count)

