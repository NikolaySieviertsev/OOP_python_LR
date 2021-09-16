"""
Task 3
Write a Python-script that determines whether the input string is the correct entry for the 'formula' according EBNF
syntax (without using regular expressions).

Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)
Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)
"""

import sys


def is_valid(expr: dict):
    return expr["valid"]


def literal(index: list):
    if index[0] == len(sys.argv):
        return {"valid": False, "result": None}

    argument = sys.argv[index[0]]

    index[0] += 1

    if argument.isdigit():
        number = {"valid": True, "result": int(argument)}

        return number
    else:
        return {"valid": False, "result": None}


def multiplicative(index: list):
    num_1 = literal(index)

    if not is_valid(num_1):
        return {"valid": False, "result": None}

    while True:
        if index[0] == len(sys.argv):
            break

        argument = sys.argv[index[0]]

        if argument == "*":
            index[0] += 1

            num_2 = literal(index)

            if not is_valid(num_2):
                return {"valid": False, "result": None}

            num_1 = {"valid": True, "result": num_1["result"] * num_2["result"]}

            continue
        elif argument == "/":
            index[0] += 1

            num_2 = literal(index)

            if not is_valid(num_2):
                return {"valid": False, "result": None}

            num_1 = {"valid": True, "result": num_1["result"] / num_2["result"]}

            continue
        else:
            break

    return num_1


def additive(index: list):
    num_1 = multiplicative(index)

    if not is_valid(num_1):
        return {"valid": False, "result": None}

    while True:
        if index[0] == len(sys.argv):
            break

        argument = sys.argv[index[0]]

        if argument == "+":
            index[0] += 1

            num_2 = multiplicative(index)

            if not is_valid(num_2):
                return {"valid": False, "result": None}

            num_1 = {"valid": True, "result": num_1["result"] + num_2["result"]}

            continue
        elif argument == "-":
            index[0] += 1

            num_2 = multiplicative(index)

            if not is_valid(num_2):
                return {"valid": False, "result": None}

            num_1 = {"valid": True, "result": num_1["result"] - num_2["result"]}

            continue
        else:
            break

    return num_1


def expression(index: list):
    return additive(index)


def parse():
    return expression([1])


print(parse())
