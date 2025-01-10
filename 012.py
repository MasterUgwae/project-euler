def count_factors(n):
    factors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors += 2  # count both i and n/i as factors
    return factors

num=1
total=0
while count_factors(total)<=500:
    total+=num
    num+=1
print(total)
