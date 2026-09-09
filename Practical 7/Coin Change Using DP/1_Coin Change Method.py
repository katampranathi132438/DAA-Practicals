def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]
n = int(input("Enter number of coins: "))
coins = []
print("Enter the coin denominations:")
for i in range(n):
    coin = int(input(f"Coin {i + 1}: "))
    coins.append(coin)
amount = int(input("Enter the amount: "))
result = coin_change(coins, amount)
if result == -1:
    print("Amount cannot be formed using the given coins.")
else:
    print("Minimum number of coins required:", result)
