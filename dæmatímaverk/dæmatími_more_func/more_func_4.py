def merge_lists(list1, list2):
    merge = list1 + list2
    list3 = []
    for i in merge:
        if i not in list3:
            list3.append(i)
    list3.sort()
    return list3
    

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
