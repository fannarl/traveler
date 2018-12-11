# Write a Python program to check a list is empty or not.

arr = input("Input a comma seperated list: ").split(',')
arr = [int(i) for i in arr]
arr = sorted(arr)

def check_if_empty(arr):
    if not arr:
        print("List is empty")

print(check_if_empty(arr))
    