prods=set()

NUMS=["1","2","3","4","5","6","7","8","9"]

def permute(lst):

    if len(lst) <= 1:
        perms = [lst]
    else:
        perms = []
        for i in range(len(lst)):
            sub = permute(lst[:i]+lst[i+1:]) 
            for p in sub:
                perms.append(lst[i:i+1]+p)

    return perms


for i in permute(NUMS):
    for j in range(1,8):
        multiplicand = "".join(i[:j])
        multProd = i[j:]
        for k in range(1,8-j):
            multiplier = "".join(multProd[:k])
            product = "".join(multProd[k:])
            if int(multiplicand)*int(multiplier)==int(product):
                prods.add(int(product))

print(sum(prods))
