def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def get_integer(prompt):
    val = int(input(prompt))
    return val

def transform(list1, list2, r1, r2):
    new_list = []
    for i in range(r1,r2):
        new_list.append(list1[i])
    for i in range(len(new_list)):
            list1.remove(list1[r1])
    list2.extend(reversed(new_list))
    

# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)