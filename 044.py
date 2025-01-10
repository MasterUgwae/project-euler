import math
def p(n:int)->int:
    return int(n*(3*n-1)/2)
def check_pentagonal(n:int) ->bool:
    return (1+math.sqrt(1+24*n))/6 %1==0
d=100000000000000000000000000000000
for i in range(1,10000):
    for j in range(1,i):

        if not check_pentagonal(p(i)+p(j)):
            continue
        if check_pentagonal(abs(p(i)-p(j))):
            print(i,j)

            if d>p(i)-p(j):
                d=p(i)-p(j)
print(d)


