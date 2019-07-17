'''
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
'''

currencyNames = ['USD', 'CAD', 'YEN', 'RUB', 'EUR']
currencyArray = [
                [1, 1.31, 108.31, 63.00, 0.89],     # USD
                [0.76, 1, 82.74, 48.13, 0.68],      # CAD
                [0.0092, 0.012, 1, 0.58, 0.0082],   # YEN
                [0.016, 0.020, 1.72, 1, 0.014],      # FAKE RUB
                # [0.016, 0.021, 1.72, 1, 0.014],   # RUB
                [1.12, 1.47, 121.37, 70.60, 1]      # EUR
                ] # real prices at time of program 7/16/19 20:34
# Fake RUB was created because RUB -> USD -> RUB and RUB -> CAD -> RUB (without fees) are instant answers
possibilities = 0

def currencyConversion(targetCurrency, amount=1, listOfCurrencies=[]):
    global possibilities
    # print(amount, listOfCurrencies)
    if(listOfCurrencies == []):
        listOfCurrencies = [targetCurrency]
    if(amount * currencyArray[listOfCurrencies[-1]][targetCurrency] > 1):
        possibilities += 1
        for i in listOfCurrencies:
            print(currencyNames[i], " -> ", end="")
        print(currencyNames[targetCurrency])
        return # This makes sure you don't have a bunch of repeating results

    for i in range(0, len(currencyArray)):
        if(i not in listOfCurrencies):
            currencyConversion(targetCurrency, amount*currencyArray[listOfCurrencies[-1]][i], listOfCurrencies+[i])

targetCurr = 0
currencyConversion(targetCurr)
print("Possibilities: ",possibilities)
