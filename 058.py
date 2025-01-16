'''import math
rc=1

def isPrime(n) -> bool:
    if n%1!=0: return False
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True

def find_ratio(spiral:list[list[str]])->float:
    numerator=0
    denominator=-1
    for i in range(len(spiral)):
        if isPrime(int(spiral[i][i])):
            numerator+=1
        if isPrime(int(spiral[i][len(spiral)-i-1])):
            numerator+=1
        denominator+=2
    return numerator/denominator

    
count=0
spiral:list[list[str]] = []
for i in range(rc):
    spiral.append([])
    for j in range(rc):
        spiral[i].append("1")

def move_up(x,y):
    return x-1, y
def move_down(x,y):
    return x+1, y
def move_left(x,y):
    return x, y-1
def move_right(x,y):
    return x, y+1


def choose_move(n): #Start from group 0 with size 1 and count of numbers = 1 
    return math.ceil(2*math.sqrt(n)-1)-1


def expand(spiral:list[list[str]])->list[list[str]]: 
    for i in range(len(spiral)):
        spiral[i]=["0"]+spiral[i]+["0"]
    spiral.insert(0,["0" for _ in range(len(spiral)+2)])
    spiral.append(["0" for _ in range(len(spiral)+1)])
    rc=len(spiral)
    x=rc-2
    y=rc-2
    for i in range((rc-2)**2,(rc)**2):
        move=choose_move(i)
        if move%4==0:
            x,y = move_right(x,y)
        elif move%4==1:
            x,y = move_up(x,y)
        elif move%4==2:
            x,y = move_left(x,y)
        else:
            x,y = move_down(x,y)

        spiral[x][y]=str(i+1)
    return spiral

spiral=expand(spiral)
print(spiral)

arr=spiral
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(f"{int(arr[i][j]):8.3f}", end=" ")
    print()
ratio=find_ratio(spiral)
while ratio>0.1:
    
    spiral = expand(spiral)
    print(len(spiral),ratio)
    ratio = find_ratio(spiral)

print(len(spiral))
'''
import math
def isPrime(n) -> bool:
    if n%1!=0: return False
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True

diagonals:list[int]=[False]
def add_diagonals(diagonals,n):
    diagonals.append(isPrime(int(((n-1)**2+1+(n-2)**2)/2)))
    diagonals.append(isPrime((n-1)**2+1))
    diagonals.append(isPrime(int(((n-1)**2+1+n**2)/2)))
    diagonals.append(False)
    return diagonals
diagonals=add_diagonals(diagonals,3)
count=3
ratio=diagonals.count(True)/len(diagonals)
while ratio>0.1:
    count+=2
    diagonals=add_diagonals(diagonals,count)
    ratio = diagonals.count(True)/len(diagonals)
print(ratio,count)
