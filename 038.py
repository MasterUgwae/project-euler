maxPan=0
nums="123456789"
def pandig(n:str):
    nums=["1","2","3","4","5","6","7","8","9"]
    if len(n)!=9:
        return False
    for i in n:
        if i in nums:
            nums.remove(i)
        else:
            return False
    return True
    
for i in range(1,10000):
    output=""
    j=1
    while len(output)<9:
        output+=str(i*j)
        j+=1
    if pandig(output):
        if int(output)>maxPan:
            maxPan=int(output)
print(maxPan)
