import string

def get_risk_factors(dataFile):
    try:
        dataFile = open(filename, "r")
        result = []
        for line in dataFile:
            words = line.replace('\n','').split(',')
            result.append(words)
        print(result)
    except FileNotFoundError:
        print("Cannot find file " + dataFile)
    
def header():
    print('{:<33} {:<21} {:<6} {:<15}'.format('Indicator' , 'Min', '', 'Max'))
    length = 87
    print('-' * length)


filename = input("Enter filename containing csv data:")
#csv_list = get_risk_factors(filename)
get_risk_factors(filename)    


# Indicator                        Min                              Max
# ---------------------------------------------------------------------------------------
# Heart Disease Death Rate (2007): Minnesota             129.8      Mississippi     266.5
# Motor Vehicle Death Rate (2009): District of Columbia    4.8      Wyoming          24.6
# Teen Birth Rate (2009):          New Hampshire          16.4      Mississippi      64.2
# Adult Smoking (2010):            Utah                    9.1      West Virginia    26.8
# Adult Obesity (2010):            Colorado               21.4      Mississippi      34.5


# Indicator                        Min                              Max 
# --------------------------------------------------------------------------------------- 
# Heart Disease Death Rate (2007): Minnesota             129.8      Mississippi     266.5 
# Motor Vehicle Death Rate (2009): District of Columbia    4.8      Wyoming          24.6 
# Teen Birth Rate (2009):          New Hampshire          16.4      Mississippi      64.2 
# Adult Smoking (2010):            Utah                    9.1      West Virginia    26.8 
# Adult Obesity (2010):            Colorado               21.4      Mississippi      34.5 