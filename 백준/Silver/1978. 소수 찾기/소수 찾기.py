import math
import sys


# Erathosthenes' sieve
def erathosthenes_sieve(qty):

    prime_number_sieve = [True] * qty

    for _seq in range(2, int(math.sqrt(qty) + 1)):
        if prime_number_sieve[_seq] == True:                    # If the number we're seeking now is a prime number
            for _not_prime in range(2 * _seq, qty, _seq):       # By the rule of Erathosthenes' sieve, delete elements(n * prime_number) in the sieve
                prime_number_sieve[_not_prime] = False

    return [_prime for _prime in range(2, qty) if prime_number_sieve[_prime] == True]


prime_number_list = erathosthenes_sieve(1000)

_qty       = int(input())
input_list = list(map(int, input().split()))

print(len(set(prime_number_list).intersection(set(input_list))))