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
from ultrasplit import split_by_symbol


def check_result(term, index=0):
    math_sign = "+-*/"
    if term[0] not in math_sign:
        term = "+" + term

    if not isinstance(term, list):
        term = split_by_symbol(term)
    try:
        if term[index] in math_sign:
            if (term[index + 1]).isdigit():
                return check_result(term, index + 2)
            return False, None
        else:
            return False, None
    except IndexError:
        return True, eval("".join(index2 for index2 in term))


term = "".join(index2 for index2 in sys.argv[1:])
print(check_result(term) if term else (False, None))