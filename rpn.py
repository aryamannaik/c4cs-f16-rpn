#!/usr/bin/env python3

import operator

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            fn = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = fn(arg1, arg2)
            stack.append(result)
        print stack

    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print "Result: ", result

if __name__ == '__main__':
    main()

