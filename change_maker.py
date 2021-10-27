# coin_value
coins = [1, 5, 10, 25, 50, 100]
target = 100 # target value $1
main_list = [0] # initial list
for coin_value in coins:
    coin_list = [0] # you can always make $0
    # add up to the target value
    curr_val = coin_value
    while curr_val <= target:
        coin_list.append(curr_val)
        curr_val += coin_value
    # the new list we will replace main with
    new_list = []
    for coin in coin_list:
        for values in main_list:
            new_list.append(values+coin)
    main_list = new_list
# how many diff iterations you can make that amount of money in cents
coin_count_list = [0 for _ in range(main_list[-1]+1)]
for i in main_list:
    coin_count_list[i] += 1
print(coin_count_list[target]) # how to make change for target