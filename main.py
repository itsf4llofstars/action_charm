#!/usr/bin/env python3
"""main.py file"""
import math


def add_num(a: int, b: int) -> int:
    return a + b


def hypot(a: float, b: float) -> float:
    return math.sqrt(a ** 2 + b ** 2)


def main():
    """main function"""
    x: int = 30
    y: int = 40
    z = add_num(x, y)
    print(f'{x} + {y} = {z}')

    pythag = hypot(x, y)
    print(pythag)


if __name__ == "__main__":
    import sys
    sys.exit(main())
