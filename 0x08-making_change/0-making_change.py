#!/usr/bin/python3
'''  Making Change '''


def makeChange(coins, total):
    '''  Making Change '''
    if total <= 0:
        return 0
    bal = total
    count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    leng = len(coins)
    while bal > 0:
        if coin_idx >= leng:
            return -1
        if bal - sorted_coins[coin_idx] >= 0:
            bal -= sorted_coins[coin_idx]
            count += 1
        else:
            coin_idx += 1
    return count