# Leikur sem lætur þig ferðast um á grid með að nota höfuðáttirnar.
# Gridið eru 9 reytir sem þýðir að hægt er að ýminda sér það sem beina línu
#                1, 2, 3, 4, 5, 6, 7, 8, 9
#Þá myndi gridið líta svona út:
#               7   8   9
#               4   5   6
#               1   2   3
# Notandi byrjar á 1 og getur ferðast norður
# Til að fara norður eða suður þarf að bæta 3 við player breytuna til að fara norður og - 3 til að fara suður
# Til að fara austur eða vestur þarf að bæta 1 við player breytuna til að fara austur eða -1 til að fara vestur
# Þegar player er = 3 þá vinnur hann
############################################################################


player = 1
grid = 9
valid_direction = 'nsew'
direction = ''
north = 3
south = 3
east = 1
west = 1
victory = False

while not victory:
    if player == 1 or player == 2:
        valid_direction = 'n'
        print("You can travel: (N)orth.")
        direction = input("Direction: " ).lower()
        #meðan direction er ekki í valid_direction halda áfram að byðja um direction              
        while direction not in valid_direction:
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        
        if direction == "n":
            player = player + north
                    
    elif player == 4:
        valid_direction='nse'
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: " ).lower()
        #checkar á valid direction breytuni og skoðar hvort
        #inputið sé rétt
        while direction not in valid_direction:
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        if direction == "n":
            player = player + north
        elif direction == "s":
            player = player - south
        elif direction == "e":
            player = player + east

    elif player == 5:
        valid_direction = 'ws'
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: " ).lower()
        while direction not in valid_direction:
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        if direction == "w":
            player = player - west
        elif direction == "s":
            player = player - south        

    elif player == 7:
        valid_direction = 'es'
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: " ).lower()
        while direction not in valid_direction:
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        if direction == "e":
            player = player + east
        elif direction == "s":
            player = player - south

    elif player == 8:
        valid_direction = 'we'
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: " ).lower()
        while direction not in valid_direction:
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        if direction == "w":
            player = player - west
        elif direction == "e":
            player = player + east

    elif player == 9:
        valid_direction = "ws"
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ").lower()
        while direction not in valid_direction:
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        if direction == "w":
            player = player - west
        elif direction == "s":
            player = player - south

    elif player == 6:
        valid_direction = 'ns'
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ").lower()
        while direction not in valid_direction:
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        if direction == "n":
            player = player + north
        elif direction == "s":
            player = player - south

    elif player == 3:
        print("Victory!")
        victory = True
        break


            
    

