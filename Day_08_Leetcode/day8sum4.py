#Best Time to Buy and Sell Stock

arr = list(map(int, input().split()))
min_price = float("inf")

max_profit = 0
for i in range(len(arr)):
  if arr[i]<min_price:
    min_price=arr[i]
  profit = arr[i] - min_price
  if profit>max_profit:
    max_profit = profit

print(max_profit)