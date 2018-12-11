# Hlutlisti (e. sublist) er listi sem hluti af lengri lista.
# Tómi listinn, [], er hlutlisti í öllum listum.
 
# Dæmi: Eftirfarandi eru hlutlistar í listanum ['1','2','3']: 
# [], ['1'], ['1', '2'], ['1', '2', '3'], ['2'], ['2', '3'], ['3']
 
# Skrifið Python forrit sem prentar út alla hlutlista gefins lista.
# Forritið á að innihalda a.m.k. eitt fall, make_sublists(a_list), sem skilar lista af öllum hlutlistum í a_list.
 
# Ábending: "List slicing" er þinn vinur!

def make_sublists(a_list):      
    result = [[]]
    for i in range(len(a_list)):
        for j in range(i, len(a_list)):
            sublist = a_list[i:j+1]
            result.append(sublist)
    return result


def read_list():
    lst = input('Input a comma seperated list: ')
    return lst.split(',')

my_list = read_list()
sub_list = make_sublists(my_list)
print(sub_list)