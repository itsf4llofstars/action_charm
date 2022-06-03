#!/usr/bin/env python3
"""main.py file"""


def get_max_primes():
    return int(input("Enter the maximum number of primes to calculate: "))


def main():
    """main function"""
    max_primes = get_max_primes()

    chk_prime = 1
    if_prime = 2
    primes = max_primes
    total_primes = 0
    iterations = 0

    while primes > 0:
        chk_prime += 1
        iterations += 1

        if if_prime % chk_prime == 0:
            if if_prime == chk_prime:
                primes -= 1
                total_primes += 1
                print(f"Prime: {total_primes} = {if_prime}")

            chk_prime = 1
            if_prime += 1

    print(f"\nIterations: {iterations}")


if __name__ == "__main__":
    import sys
    sys.exit(main())
