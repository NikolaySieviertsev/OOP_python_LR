"""
Task 1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
>>python my_task.py 1 * 2
"""

import sys

num_1, operation, num_2 = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

operations = {'+': num_1 + num_2, '-': num_1 - num_2, '*': num_1 * num_2, '/': num_1 / num_2}

print(operations[operation])