# Leikur sem lætur þig ferðast um á grid með að nota höfuðáttirnar.

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
        print("You can travel: (N)orth or (S)outh or (E)ast.")
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
        print("You can travel: (W)est or (S)outh.")
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
        print("You can travel: (S)outh or (E)ast.")
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
        print("You can travel: (W)est or (E)ast.")
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
        print("You can travel: (W)est or (S)outh.")
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


            
    

