# Write a Python program to get the smallest number from a list.

arr = input("Input a comma seperated list: ").split(',')
arr = [int(i) for i in arr]
arr = sorted(arr)

def min_value(arr):
    MIN = arr[0]
    for i in arr:
        if i < MIN:
            MIN = i
    return MIN

print(min_value(arr))