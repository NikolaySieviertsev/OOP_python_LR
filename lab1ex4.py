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

bagpack_capacity = int(input("Enter the knapsack capacity: "))
num_of_bars = int(input("Enter the number of golden bars: "))


def knapsack(bagpack_capacity, num_of_bars):
    max_weight = 0
    list_of_bars_weight = []
    list_max_weight = []
    print("Enter the weight of each golder bar: ")
    for index1 in range(1, num_of_bars + 1):
        bar_weight = int(input())
        list_of_bars_weight.append(bar_weight)

    list_of_bars_weight.sort()
    list_of_bars_weight.reverse()

    for index2 in range(len(list_of_bars_weight)):
        for index3 in range(index2, len(list_of_bars_weight)):
            max_weight += list_of_bars_weight[index3]
            if max_weight > bagpack_capacity:
                max_weight = max_weight - list_of_bars_weight[index3]
        list_max_weight.append(max_weight)
        max_weight = 0

    print("Max weight of gold that fits into a knapsack with capacity of", bagpack_capacity, "is", max(list_max_weight))
    # print(list_of_bars_weight)
    # print(list_max_weight)
    # print(max(list_max_weight))

    return bagpack_capacity, num_of_bars


knapsack(bagpack_capacity, num_of_bars)
