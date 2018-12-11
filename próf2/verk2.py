def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
def get_list(a_list):
    try:
        for index, value in enumerate(a_list):
            a_list[index] = int(value)
        return list(a_list)
    except ValueError:
        print("Incorrect input!")
        return ()


def sort_list(sort_int_list):
    sort_int_list.sort()

def if_is_prime(a_list):
    prime_list = []
    unique_prime = []
    for i in a_list:
        if is_prime(i) == True:
            prime_list.append(i)
    for i in prime_list[::]:
        if i not in unique_prime:
            unique_prime.append(i)
    return unique_prime

def list_avarge(a_list):
    avarage = 0
    for i in a_list:
        avarage += i
    return avarage / len(a_list)

# The main program starts here
a_list = input("Enter integers separated with commas:").strip().split(',')
get_list(a_list)
print("Input list:" , a_list)
sort_list(a_list)
print("Sorted list:" , a_list)
print("Prime list:" , if_is_prime(a_list))
print(list_avarge(a_list))
print("Min:" , min(a_list), "," + " Max:", max(a_list), "," + " Average:" , list_avarge(a_list))
