#!/usr/bin/env python3
"""main.py file"""


def get_max_primes():
    return int(input("Enter the maximum number of primes to calculate: "))


def main():
    """main function"""
    max_primes = get_max_primes()


if __name__ == "__main__":
    import sys
    sys.exit(main())
