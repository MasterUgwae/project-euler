import math
count=0
def check_triangle(n:int)-> bool:
    return (-1+math.sqrt(1+8*n))/2 %1==0
def check_pentagonal(n:int) ->bool:
    return (1+math.sqrt(1+24*n))/6 %1==0
def H(n:int)->int:
    return n*(2*n-1)
i=1
while count<3:
    if check_pentagonal(H(i)):
        if check_triangle(H(i)):
            print(i,H(i))
            count+=1
    i+=1
