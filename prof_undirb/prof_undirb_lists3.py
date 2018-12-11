# Write a Python program to get the largest number from a list.

arr = input("Input a comma seperated list: ").split(',')
arr = [int(i) for i in arr]
arr = sorted(arr)

def max_value(arr):
    MAX = arr[0]
    for i in arr:
        if i > MAX:
            MAX = i
    return MAX

print(max_value(arr))