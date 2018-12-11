#game_of_eights() function goes here
def game_of_eights(list1):
    check = False
    for i in range(len(list1)):
        if list1[i] == "8" and list1[i-1] == "8":
            check = True
    return check

def is_number(a_list):
    try:
        str1 = ''.join(str(i) for i in a_list)
        int1 = int(str1)
        print(game_of_eights(a_list))
    except ValueError:
        print("Error. Please enter only integers.")


def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    is_number(a_list)

main()