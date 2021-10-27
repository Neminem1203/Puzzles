import math
def iteration_generator(coin_list, main_list, target):
    if not target:
        target = math.inf
    new_list = []
    for coin in coin_list:
        for values in main_list:
            if values+coin <= target:
                new_list.append(values+coin)
    return new_list

def counter(main_list):
    ret_list = [0 for _ in range(main_list[-1]+1)]
    for i in main_list:
        ret_list[i] += 1
    return ret_list

def target_finder(coins, target):
    '''
    Makes target value with the coins given
    :param coins: Array of coin_values
    :param target: target you're trying to get to
    :return: number of iterations for target value
    '''
    # coins = [1, 5, 10, 25, 50, 100]
    # target = 100 # target value $1
    main_list = [0] # initial list
    for coin_value in coins:
        if(coin_value <= 0):
            raise "All coin values must be > 0"
        coin_list = [0] # you can always make $0

        # add up to the target value
        curr_val = coin_value
        while curr_val <= target:
            coin_list.append(curr_val)
            curr_val += coin_value

        main_list = iteration_generator(coin_list, main_list, target)
    # how many diff iterations you can make that amount of money in cents
    coin_count_list = counter(main_list)
    return(coin_count_list[target]) # how to make change for target

def change_maker(coins, target=None):
    '''
    Makes target value with the coins given
    :param coins: Array of [coin_value, coin_count]
    :param target: (optional) target you're trying to get to
    :return: array of possibilities on how to generate the index-value or
        number of iterations for target value (if target is specified)
    '''
    main_list = [0] # initial list
    for coin_value, coin_count in coins:
        if(coin_value <= 0):
            raise "All coin values must be > 0"
        coin_list = [0] # you can always make $0

        # add up to the target value
        for i in range(1, coin_count+1):
            coin_list.append(coin_value * i)

        main_list = iteration_generator(coin_list, main_list,target)
    # how many diff iterations you can make that amount of money in cents
    coin_count_list = counter(main_list)
    if target: # if target is specified, return the number of times target occurs
        return coin_count_list[target]
    return(counter(main_list)) # how to make change for target

print(change_maker([[1,3],[3,2]], 6)) # 1 1 1 3 3 making 6
print(change_maker([[1,3],[3,2]])) # 1 1 1 3 3 array
print(target_finder([1,5,10,25,50,100], 100)) # all coins making change for $1
