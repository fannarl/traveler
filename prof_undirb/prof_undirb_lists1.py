# Write a Python program to sum all the items in a list.

arr = input("Input a comma seperated list: ").split(',')
arr = [int(i) for i in arr]
arr = sorted(arr)

def sum_of_list(arr):
    sum_of_num = 0
    for i in arr:
        sum_of_num += i
    return sum_of_num

print(sum_of_list(arr))