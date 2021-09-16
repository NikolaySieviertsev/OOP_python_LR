"""
Task 4
You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not (hence you cannot take a fraction
of a bar).
Write a function that returns the maximum weight of gold that fits into a knapsack's capacity.
The first parameter contains 'capacity' - integer describing the capacity of a knapsack.
The next parameter contains 'weights' - list of weights of each gold bar.
Output : Maximum weight of gold that fits into a knapsack with capacity of W.
"""

def knapsack(weight: int, capacity: list):

    array = [1] + [0]*weight
    for index1 in range(len(capacity)):
        for index2 in range(weight, capacity[index1] - 1, -1):
            if array[index2 - capacity[index1]] == 1:
                array[index2] = 1

    index1 = weight
    while array[index1] == 0:
        index1 -= 1
    print(index1)


knapsack(20, [10,7,7,2])