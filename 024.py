def permute(lst):
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permute(remLst):
            result.append([m] + p)
    return result
original = ["0","1","2","3","4","5","6","7","8","9"]

permutations = sorted(permute(original))

print(permutations[999999])
