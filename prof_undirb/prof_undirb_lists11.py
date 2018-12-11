# Write a Python function that takes two lists and returns True if they have at least one common member.

arr1 = input("Input a comma seperated list: ").split(',')
arr1 = [int(i) for i in arr1]

arr2 = input("Input a comma seperated list: ").split(',')
arr2 = [int(i) for i in arr2]

def find_common(arr1, arr2):
    result = False
    for i in arr1:
        for j in arr2:
            if i == j:
                result = True
    return result

print(find_common(arr1, arr2))