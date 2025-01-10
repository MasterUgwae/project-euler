from itertools import permutations
from threading import Thread, Event
import time

start=time.perf_counter()
out=[]
def joint(s:tuple[str]):
    return "".join(s)
def checkPermutations(n:str)->bool:
    for i in range(1,7):
        if str(int(n)*i) not in list(map(joint,list(permutations(n)))):
            return False
    return True
def main(sVal,event):
    while not checkPermutations(str(sVal)) and not event.is_set():
        sVal+=4
    out.append(sVal)
    event.set()
x=1

threads:list[Thread]=[]
event=Event()


for i in range(1,5):
    threads.append(Thread(target=main,args=[i,event]))

for thread in threads:
    thread.start()
event.wait()

print(f"{out[0]} was found in {time.perf_counter()-start:.3f}s")

