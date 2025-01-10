import string

file = open("0042_words.txt","r")

text=file.readline().split(",")

letters=['"']+[i for i in string.ascii_uppercase]

def triangle(n):
    return int(n*(n+1)/2)

count=0

for i in text:
    wordValue = 0
    for j in i:
        wordValue+=letters.index(j)
    n=0
    while wordValue>triangle(n):
        n+=1
    if wordValue==triangle(n):
        count+=1
print(count)
file.close()
