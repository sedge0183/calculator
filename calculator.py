#!/usr/bin/env python
import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def divide(x, y):
    return x / y


def main():
    print "-----------------------"
    print "Hacktobercub calculator"
    print "-----------------------"
    print ""

    a = int(sys.argv[1])
    oper = sys.argv[2]
    b = int(sys.argv[3])

    if oper == "+":
        result = add(a, b)
    elif oper == "-":
        result = sub(a, b)
    elif oper == "/" or oper == "\\":
        result = divide(a, b)

    print "Result: " + str(result) + "\n"


if __name__ == "__main__":
    try:
        main()
    except ValueError: 
        print "Invalid input"
