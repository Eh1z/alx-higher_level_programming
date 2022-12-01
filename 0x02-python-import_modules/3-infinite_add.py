#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    number_arg = len(sys.argv)
    add = 0

    for i in range(1, number_arg):
        add += int(sys.argv[i])
    print("{}".format(add))
