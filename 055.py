def check_palindrome(s:str)->bool:
    return s[::-1]==s

def check_lychrel(n:int)->bool:
    for _ in range(50):
        n=int(str(n)[::-1])+n
        if check_palindrome(str(n)):
            return True
    return False
count=0
for i in range(1,10000):
    if not check_lychrel(i):
        count+=1
print(count)
