
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    bought_stock = False
    bought_at = 0
    profit = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i + 1] and bought_stock == False: # If price is increasing, buy it now (if not bought yet)
            bought_stock = True
            bought_at = prices[i]
        elif prices[i] > prices[i+1] and bought_stock == True: # If the price decreases, sell the stock now (if bought is true)
            bought_stock = False
            profit += prices[i] - bought_at
            bought_at = 0
        elif i == (len(prices) - 2) and bought_stock == True: # Last item is still increasing
            profit += prices[i + 1] - bought_at
    return profit

# print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))