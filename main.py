#!/usr/bin/env python3
"""main.py file"""


def add_num(a: int, b: int) -> int:
    return a + b


def main():
    """main function"""
    x: int = 33
    y: int = 44
    z = add_num(x, y)
    print(f'{x} + {y} = {z}')


if __name__ == "__main__":
    import sys
    sys.exit(main())
