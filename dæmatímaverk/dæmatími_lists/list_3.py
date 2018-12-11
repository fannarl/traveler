# Your functions should appear here
def populate_list(inp):
    while inp != "exit":
        inp = input("Enter value to be added to list: ").lower()
        initial_list.append(inp)
        if inp == "exit":
            initial_list.pop()
            break

def triple_list(pop_l):
    return pop_l * 3



# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
