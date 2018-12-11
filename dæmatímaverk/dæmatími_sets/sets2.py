def choice(set1, set2):
    continues = True
    while continues == True:
        print('1. Intersection\n2. Union\n3. Difference\n4. Quit')
        user_choice = int(input("Set operation: "))
        if user_choice == 1:
            print(set_intersection(set1, set2))
        elif user_choice == 2:
            print(set_union(set1, set2))
        elif user_choice == 3:
            print(set_difference(set1, set2))
        elif user_choice == 4:
            continues = False

    return user_choice

def set_intersection(set1, set2):
    return set1.intersection(set2)

def set_union(set1, set2):
    return set1.union(set2)

def set_difference(set1, set2):
    return set1.difference(set2)

# Main program starts here
list1 = input("Input a list of integers separated with a comma: ").split(',')
list2 = input("Input a list of integers separated with a comma: ").split(',')
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
choice(set1 ,set2)