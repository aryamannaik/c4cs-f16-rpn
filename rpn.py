#!/usr/bin/env python3

import operator
from termcolor import colored

def concat(arg1, arg2):
    return int(str(arg1) + str(arg2))

def col_print(stk):
    print("[ ", end="")
    for ele in stk:
        if ele in operators:
           print(colored(ele, "green"), end=" ]\n")
        elif int(ele) < 0:
            print(colored(ele, "red"), end=", ")
        else:
            print(ele, end=", ")

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '**' : operator.pow,
    '++' : concat,
}

def calculate(arg):
    stack = list()
    col_print(arg.split())
    for token in arg.split():
        try:
            token = int(token)
            stack.append(token)
        except:
            fn = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = fn(arg1, arg2)
            stack.append(result)

    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()

