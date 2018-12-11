# Write a Python program to remove duplicates from a list.

arr = input("Input a comma seperated list: ").split(',')
arr = [int(i) for i in arr]
arr = sorted(arr)

arr = list(set(arr))

print(arr)