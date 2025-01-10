from itertools import permutations
import time

start=time.perf_counter()
def joint(s:tuple[str]):
    return "".join(s)
def checkPermutations(n:str)->bool:
    for i in range(1,7):
        if str(int(n)*i) not in list(map(joint,list(permutations(n)))):
            return False
    return True

x=10
while not checkPermutations(str(x)):
    x+=1

print(f"{x} was found in {time.perf_counter()-start:.3f}s")
