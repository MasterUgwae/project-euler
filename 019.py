def find_index_1st(january1, month, year):
    if month == 0:
        return january1 #january
    if month == 1:
        return (january1+31)%7 #february


    if year%400==0:
        feb=29
    elif year%100==0:
        feb=28
    elif year%4==0:
        feb=29
    else:
        feb=28

    if month==2:
        return (january1+31+feb)%7 # March
    if month==3:
        return (january1+feb+62)%7 # April
    if month==4:
        return (january1+92+feb)%7 # May
    if month==5:
        return (january1+feb+123)%7 # June
    if month==6:
        return (january1+153+feb)%7 # July
    if month==7:
        return (january1+feb+184)%7 # August
    if month==8:
        return (january1+215+feb)%7 # September
    if month==9:
        return (january1+feb+245)%7 # October
    if month==10:
        return (january1+276+feb)%7 # November
    if month==11:
        return (january1+feb+306)%7 # December
    if month==12:
        return (january1+feb+337)%7



jan1900=1

jan1st=(366+jan1900)%7

firsts=[]

for i in range(100):
    for j in range(12):
        firsts.append(find_index_1st(jan1st,j,i+1901))
    jan1st=find_index_1st(jan1st,12,i+1901)

print(firsts.count(0))
