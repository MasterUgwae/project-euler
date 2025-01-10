total=0
for i in range(2,1000000):
    string=str(i)
    power=0
    for j in string:
        power+=int(j)**5
    if power ==i:
        total+=i

print(total)
