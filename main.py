#!/usr/bin/env python3
"""main.py file"""


def get_max_primes():
    return int(input("Enter the maximum number of primes to calculate: "))


def check_mod(if_prime_num, chk_prime_num):
    return not if_prime_num % chk_prime_num


def check_equal(if_prime_num, chk_prime_num):
    return if_prime_num == chk_prime_num


def change_num(number, plus=True):
    if plus:
        return number + 1
    return number - 1


def main():
    """main function"""
    max_primes = get_max_primes()

    chk_prime = 1
    if_prime = 2
    primes = max_primes
    total_primes = 0
    iterations = 0

    while primes > 0:
        chk_prime = change_num(chk_prime)
        iterations = change_num(iterations)

        if check_mod(if_prime, chk_prime) and check_equal(if_prime, chk_prime):
            primes = change_num(primes, False)
            total_primes = change_num(total_primes)
            print(f"Prime: {total_primes} = {if_prime}")
            chk_prime = 1
            if_prime = change_num(if_prime)
        elif check_mod(if_prime, chk_prime) and not check_equal(if_prime, chk_prime):
            chk_prime = 1
            if_prime = change_num(if_prime)

    print(f"\nIterations: {iterations}")


if __name__ == "__main__":
    import sys
    sys.exit(main())
