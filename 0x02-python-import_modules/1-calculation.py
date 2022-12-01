#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    number_arg = len(sys.argv) - 1
    if number_arg == 0:
        print("{} arguments.".format(number_arg))
    elif number_arg == 1:
        print("{} argument:".format(number_arg))
    else:
        print("{} arguments:".format(number_arg))

    for i in range(1, number_arg + 1):
        print("{}: {}".format(i, sys.argv[i]))
