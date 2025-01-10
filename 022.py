import string

file = open("0022_names.txt","r")

text=file.readline().split(",")

u=['"']+[i for i in string.ascii_uppercase]

text.sort()
total=0
for i in range(len(text)):
    print(text[i])
    temp=0
    for j in text[i]:
        temp+=u.index(j)
    total+=(i+1)*temp

print(total)
