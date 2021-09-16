"""
Task 2
Write a Python-script that performs the standard math functions on the data.
The name of function and data are set on the command line when the script is run.
The script should be launched like this:
>>python my_task.py add 1 2
"""

import sys

operation, num_1, num_2 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

operations = {'add': num_1 + num_2, 'sub': num_1 - num_2, 'mul': num_1 * num_2, 'div': num_1 / num_2}

print(operations[operation])