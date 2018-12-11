
def common_letters_list(first, last):
    common = []
    for ch in first:
        if ch in last and ch not in common:
            common.append(ch)

    return common

def common_letters_set(first, last):
    set1 = set(first)
    set2 = set(last)

    return set1.intersection(set2)

# Main program starts here
name = input("Enter name: ").lower()
first, last = name.split()
common_list = common_letters_list(first, last)
common_set = common_letters_set(first, last)
print(sorted(common_list))
print(sorted(common_set))