#!/usr/bin/python3
''' Minimum Operations '''


def minOperations(n):
    ''' obtain pfs and return their sum '''
    pf_list = generate_pf(n)
    return sum(pf_list)


def generate_pf(n):
    ''' find pfs '''
    pfs = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            pfs.append(i)

    if n > 1:
        pfs.append(n)
    return pfs
