total = 200

coins = [100, 50, 20, 10, 5, 2, 1]

ways = []
for i in range(total+1):
    ways.append(0)

ways[0]=1

for coin in coins:
    for amount in range(coin,total+1):
        ways[amount]+=ways[amount-coin]

print(ways[200])
