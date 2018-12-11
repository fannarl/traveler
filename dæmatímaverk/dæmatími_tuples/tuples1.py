def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

#Main program

user_list = get_list()
print(user_list)
user_choice = input("Enter choice (m,r): ")
if user_choice == "m":
    input_split = input().split(",")
    index_v = int(input_split[0])
    v = int(input_split[1])
    mutate_list(user_list,index_v,v)
elif user_choice == "r":
    to_pop = int(input())
    remove_ch(user_list,to_pop)
print(user_list)