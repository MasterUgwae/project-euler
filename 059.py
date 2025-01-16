def vernam (s,k):
  print("".join(chr(s[i]^ord(k[i])) for i in range(len(s))))

def decrypt(ascii,key):
    repeat_times = (len(ascii) + len(key) - 1) // len(key)
    # Repeat the short list and slice it to match the length of the target list
    key = (ascii * repeat_times)[:len(ascii)]
    return vernam(ascii,key)
with open("0059_cipher.txt","r") as asc:
    text=list(int(i) for i in asc.readline().split(","))
