# Write a Python program to multiplies all the items in a list

arr = input("Input a comma seperated list: ").split(',')
arr = [int(i) for i in arr]
arr = sorted(arr)

def multiplies_list(arr):
    list_multible = arr[0]

    for i in arr:
        list_multible *= i
    return list_multible

print(multiplies_list(arr))