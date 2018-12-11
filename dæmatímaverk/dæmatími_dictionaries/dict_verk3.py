def add_to_dict(a_dict):
    key = input("Key: ")
    value = input("Value: ")
    if key in a_dict:
        print("Error. Key already exists.")
    else:
        a_dict[key] = value

def remove_from_dict(a_dict):
    remove_key = input("key to remove: ")
    if remove_key not in a_dict:
        print("No such key exists in the dictionary.")
    else:
        del a_dict[remove_key]

def find_key(a_dict):
    key_to_find = input("Key to locate: ")
    if key_to_find not in a_dict:
        print("Key not found.")
    else:
        print("Value: " , a_dict.get(key_to_find))

def menu_selection():
    print("Menu: ")
    choice = input("add(a), remove(r), find(f): ")
    return choice.lower()

def execute_selection(user_choice, a_dict):
    if user_choice == "a":
        add_to_dict(a_dict)
    elif user_choice == "r":
        remove_from_dict(a_dict)
    elif user_choice == "f":
        find_key(a_dict)

def dict_to_tuples(a_dict):
    dictlist = []
    for key, value in a_dict.items():
        temp = (key,value)
        dictlist.append(temp)
    return dictlist

# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()