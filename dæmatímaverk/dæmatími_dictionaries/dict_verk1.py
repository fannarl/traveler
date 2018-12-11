
def askForInfo(a_dict):
    name = input("Name: ")
    number = input("Number: ")
    a_dict[name] = number

def more_data():
    cont = input("More data (y/n)? ")
    return cont.lower() == 'y'

def dict_to_tuples(a_dict):
    dictlist = []
    for key, value in a_dict.items():
        temp = (key,value)
        dictlist.append(temp)
    return dictlist

the_dict = {}
go_again = True
while go_again:
    askForInfo(the_dict)
    go_again = more_data()

dictlist = dict_to_tuples(the_dict)
print(sorted(dictlist))