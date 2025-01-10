uBound=28123

abundant=set()

for i in range(3,uBound):
    factors=0
    for j in range(1,i):
        if i%j==0:
            factors+=j
    if factors>i:
        abundant.add(i)
total=0
for i in range(1,uBound+1):
    found = False
    for j in abundant:
        if i-j in abundant:
            found=True
            break
    if not found:
        total+=i

print(total)
