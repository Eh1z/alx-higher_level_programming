#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

        a = sys.argv[1]
        b = sys.argv[3]
        operator = sys.argv[2]

        if operator != '+' and operator != '-' \
           and operator != '*' and operator != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        if operator == '+':
            print("{} + {} = {}".format(int(a), int(b), add(int(a), int(b))))
        elif operator == '-':
            print("{} - {} = {}".format(int(a), int(b), sub(int(a), int(b))))
        elif operator == '*':
            print("{} * {} = {}".format(int(a), int(b), mul(int(a), int(b))))
        elif operator == '/':
            print("{} / {} = {}".format(int(a), int(b), div(int(a), int(b))))
