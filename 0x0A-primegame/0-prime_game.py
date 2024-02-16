#!/usr/bin/python3
def generate_primes_sieve(n):
    ''' generate primes sieve '''
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n+1) if primes[i]]


def isWinner(x, nums):
    ''' determine te winner '''
    primes = generate_primes_sieve(max(nums))
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for prime in primes if prime <= n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
