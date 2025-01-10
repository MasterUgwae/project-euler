spiral = []
rc=1001
for i in range(rc):
    spiral.append([])
    for j in range(rc):
        spiral[i].append("0")


def move_up(x,y):
    return x-1, y

def move_down(x,y):
    return x+1, y
def move_left(x,y):
    return x, y-1
def move_right(x,y):
    return x, y+1
x=int((rc-1)/2)
y=int((rc-1)/2)
adder=-1
temp=1
move=3
for i in range(rc**2):
    spiral[x][y]=str(i+1)
    temp-=1
    if temp==0:
        move = (move+1)%4
        adder+=1
        temp = adder//2 +1

    if move==0:
        x,y = move_right(x,y)
    elif move==1:
        x,y = move_down(x,y)

    
    elif move==2:
        x,y = move_left(x,y)
    else:
        x,y = move_up(x,y)

total=-1
for i in range(rc):
    total+=int(spiral[i][i])
    total+= int(spiral[i][rc-i-1])


print(total)
