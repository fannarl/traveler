def lowestValue(int1,int2):
    if int1 < int2:
        print(int1)
    else:
        print(int2)

def lowest_of_three(a_list):
    a_list.sort()
    lowest = a_list[0]
    return lowest


def lowest_of_dynamic(num_list):
    num_list.sort()
    lowest = num_list[0]
    return lowest


def main():
    int1 = int(input("input a integer: "))
    int2 = int(input("input a integer: "))
    lowestValue(int1,int2)
    a_list = []
    count = 0
    inputs = True
    while inputs == True:     
        a_list.append(int(input("input a integer: ")))
        count += 1
        if count == 3:
            inputs = False
            print(lowest_of_three(a_list))
            
    how_many = int(input("how many inputs?: "))
    num_list = []
    num_of_inputs = 0
    cont = True
    while cont == True:
        num_list.append(int(input("input a integer: ")))
        num_of_inputs += 1
        if num_of_inputs == how_many:
            cont = False
            print(lowest_of_dynamic(num_list))
    
main()