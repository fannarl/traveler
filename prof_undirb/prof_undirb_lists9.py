# Write a Python program to clone or copy a list. 

arr = input("Input a comma seperated list: ").split(',')
arr = [int(i) for i in arr]
arr = sorted(arr)

def clone_list(arr):
    arr2 = []
    for i in arr:
        arr2.append(i)
    return arr2

print("Original list: {0}".format(arr))
print("Copied list: {0}".format(clone_list(arr)))
