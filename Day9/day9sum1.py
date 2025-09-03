def maxProfit(prices):
    n = len(prices)
    profit = 0
    
    for i in range(1, n):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    
    return profit


prices1 = [100, 180, 260, 310, 40, 535, 695]
print(maxProfit(prices1))

prices2 = [4, 2, 2, 2, 4]
print(maxProfit(prices2)) 
