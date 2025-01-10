from functools import lru_cache
import heapq
heapq.heapify()
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

@lru_cache(maxsize=512)
def choose_move(n, group=0, size=0, count=1): #Start from group 0 with size 1 and count of numbers = 1 

    if n < count:
        return group
    else:
        group += 1
        size = (group // 2) + 1
        count += size
        return choose_move(n, group, size, count)

import math

def find_output_constant(n):
    return math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2) - 1

# Example usage
for i in range(25):
    print(f"Input: {i}, Output: {find_output_constant(i)}")
# Example usage
for i in range(25):
    print(f"Input: {i}, Output: {choose_move(i)}")

def expand(spiral:list[list[str]])->list[list[str]]: 
    for i in range(len(spiral)):
        spiral[i]=["0"]+spiral[i]+["0"]
    spiral.insert(0,["0" for _ in range(len(spiral)+2)])
    spiral.append(["0" for _ in range(len(spiral)+1)])
    rc=len(spiral)
    x=rc-2
    y=rc-2
    for i in range((rc-2)**2,(rc)**2):
        move=choose_move(i-1)
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
while find_ratio(spiral)>0.1:
    
    spiral = expand(spiral)
    print(len(spiral))

print(len(spiral))

