power=set()

for i in range(2,101):
    for j in range(2,101):
        power.add(i**j)

print(len(power))
