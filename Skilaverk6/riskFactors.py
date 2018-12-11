def openfile(dataFile):
# Athugar hvort file sé til
    try:
        dataFile = open(filename, "r")
        result = []
# fer í gegnum línurnar og splittar á kommuni og tekur í burt línuskiptingar (.replace('\n',''))
# og hendir útkomuni í result[] listan
        for line in dataFile:
            words = line.replace('\n','').split(',')
            result.append(words)
        return result
# Ef csv file finnst ekki þá pass
    except FileNotFoundError:
        pass

def presentation_test(value):
# Athugar hvort value-ið sé með prósentu í endan á sér og ef svo er skilar value-inu ekki með prósentu
    test_list = []
    test_list = [i for i in value]
    if test_list[-1] == "%":
        test_list.pop()
        num_present = "".join(test_list)
    else:
        num_present = value
    return num_present
def find_min(file_name, num):
# Fer í gegnum lista eftir númeri og leitar af minstu töluni í öllum þeim lista
    min_num = 99999999
    min_num_state = ""
    for i in file_name[2:]:
        str_num = i[num]
        placeholder = presentation_test(str_num)
        float_num = float(placeholder)
        float_num = round(float_num, 1)
        str_state = i[0]
        if float_num < min_num:
            min_num = float_num
            min_num_state = str_state
            str_min_num = str(min_num)
    return str_min_num, min_num_state
def find_Max(file_name, num):
# Fer í gegnum lista eftir númeri og leitar af Stærstu töluni í öllum þeim lista
    max_num = 0
    max_num_state = ""
    for i in file_name[2:]:
        str_num = i[num]
        placeholder = presentation_test(str_num)
        float_num = float(placeholder)
        float_num = round(float_num, 1)
        str_state = i[0]
        if float_num > max_num:
            max_num = float_num
            max_num_state = str_state
            str_max_num = str(max_num)
    return str_max_num, max_num_state

def header(Name, filename):
# Ef Name breytan er == None. Þar er að segja að það var enginn csv file fannst undir því nafni
# Þá prentar header-inn x yfir seperator (----)
    if Name == None:
        print("Cannot find file " + filename)
        print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format('Indicator' , 'Min', '', '', 'Max',''))
        print('-' * 87)        
    else:
        print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format('Indicator' , 'Min', '', '', 'Max',''))
        print('-' * 87)      

def items(list1):
# Ef csv file er til þá prentar hann út gögninn á því formatti sem verkefnið krafðist
    try:
        header(list1, filename)
        HDDR = Name[0][1]
        HDDR_num_min , HDDR_state_min = find_min(Name, 1)
        HDDR_num_max , HDDR_state_max = find_Max(Name, 1)
        print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format(HDDR + ":", HDDR_state_min, HDDR_num_min, "", HDDR_state_max, HDDR_num_max))
        MVDR = Name[0][5]
        MVDR_num_min , MVDR_state_min = find_min(Name, 5)
        MVDR_num_max , MVDR_state_max = find_Max(Name, 5)    
        print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format(MVDR + ":", MVDR_state_min, MVDR_num_min, "", MVDR_state_max, MVDR_num_max))
        TBR = Name[0][7]
        TBR_num_min , TBR_state_min = find_min(Name, 7)
        TBR_num_max , TBR_state_max = find_Max(Name, 7)
        print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format(TBR + ":", TBR_state_min, TBR_num_min, "", TBR_state_max, TBR_num_max))
        AS = Name[0][11]
        AS_num_min , AS_state_min = find_min(Name, 11)
        AS_num_max , AS_state_max = find_Max(Name, 11)
        print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format(AS + ":", AS_state_min, AS_num_min, "", AS_state_max, AS_num_max))
        AO = Name[0][13]
        AO_num_min , AO_state_min = find_min(Name, 13)
        AO_num_max , AO_state_max = find_Max(Name, 13)
        print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format(AO + ":", AO_state_min, AO_num_min, "", AO_state_max, AO_num_max))
# Annars ef csv file fannst ekki þá keyrir hann ekki þetta function fyrir utan header() function kallið efst.
    except TypeError:
        pass
# Forrit byrjar hér
filename = input("Enter filename containing csv data: ")
Name = openfile(filename)
items(Name)