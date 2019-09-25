'''
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

def stocktrade(company):
    current_low = company[0]
    profit = 0
    for price in company:
        if(price - current_low > profit):
            profit = price-current_low
        if(current_low > price):
            current_low = price
    return profit

print(stocktrade([9, 11, 8, 5, 7, 10]))
print(stocktrade([9, 20, 1, 5, 7, 11]))