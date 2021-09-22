"""
Task 2
Write a Python-script that performs the standard math functions on the data.
The name of function and data are set on the command line when the script is run.
The script should be launched like this:
>>python my_task.py add 1 2
"""

import sys

try:
    operation, num_1, num_2 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

    operations = {'add': num_1 + num_2, 'sub': num_1 - num_2, 'mul': num_1 * num_2, 'div': num_1 / num_2}

    print(operations[operation])
except ZeroDivisionError:
    print("You cannot divide by zero!")
except KeyError:
    print("Dictionary key is not found!")
except IndexError:
    print("Sequence index is out of range or string is empty!")
except ValueError:
    print("You entered wrong arguments!")