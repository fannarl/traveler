count = 1
while count <= 18:
    par = int(input("Par of hole " + str(count) + ": " ))
    score = int(input("Score on hole " + str(count) + ": "))
    count = count + 1
    if par == score:
        print("par")
    elif (par + 1) == score:
        print("bogey")
    elif (par + 2) == score:
        print("double bogey")
    elif (par + 3) == score:
        print("triple bogey")
    elif (par + 4) <= score:
        print("bad hole")
    elif (par - 1) == score:
        print("birdie")
    elif (par - 2) == score:
        print("eagle")
    elif (par - 3) == score:
        print("albatross")
    else:
        print("invalid score")