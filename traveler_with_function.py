# Leikur sem lætur þig ferðast um á grid með að nota höfuðáttirnar.                                             #
# Gridið eru 9 reytir sem þýðir að hægt er að ýminda sér það sem beina línu                                     #
#                1, 2, 3, 4, 5, 6, 7, 8, 9                                                                      #
# Þá myndi gridið líta svona út:                                                                                #
#       | eru veggir                                                                                            #
#               7   8   9                                                                                       #
#               4   5|  6                                                                                       #
#               1  |2|  3                                                                                       #
# Notandi byrjar á 1 og getur ferðast norður                                                                    #
#   |1|, 2, 3, 4, 5, 6, 7, 8, 9                                                                                 #
# Til að fara norður eða suður þarf að bæta 3 við player breytuna til að fara norður og - 3 til að fara suður   #
#   |1|, 2, 3,|4|, 5, 6, 7, 8 ,9                                                                                #                            #
# Til að fara austur eða vestur þarf að bæta 1 við player breytuna til að fara austur eða -1 til að fara vestur #
# Þegar player er = 3 þá vinnur hann                                                                            #
#################################################################################################################


player = 1
valid_direction = 'nsew'
direction = ''
north = 3
south = 3
east = 1
west = 1
victory = False

def not_valid(p_dir, v_dir):
    while p_dir not in v_dir:
        print("Not a valid direction!")
        p_dir = input("Direction: ").lower()
        return p_dir, v_dir

def dir_func(inp_dir, player_int):
        if inp_dir == "n":
            player_int = player_int + north
        elif inp_dir == "s":
            player_int = player_int - south
        elif inp_dir == "e":
            player_int = player_int + east
        elif inp_dir == "w":
            player_int = player_int - west

while not victory:
    if player == 1 or player == 2:
        valid_direction = 'n'
        print("You can travel: (N)orth.")
        direction = input("Direction: " ).lower()
        #meðan direction er ekki í valid_direction halda áfram að byðja um direction              
        not_valid(player, valid_direction)
        dir_func(direction, player)
                    
    elif player == 4:
        valid_direction='nse'
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: " ).lower()
        #checkar á valid direction breytuni og skoðar hvort
        #inputið sé rétt
        not_valid(player, valid_direction)
        dir_func(direction, player)

    elif player == 5:
        valid_direction = 'ws'
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: " ).lower()

        not_valid(player, valid_direction)
        dir_func(direction, player)       

    elif player == 7:
        valid_direction = 'es'
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: " ).lower()

        not_valid(player, valid_direction)
        dir_func(direction, player)

    elif player == 8:
        valid_direction = 'we'
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: " ).lower()

        not_valid(player, valid_direction)
        dir_func(direction, player)

    elif player == 9:
        valid_direction = "ws"
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ").lower()

        not_valid(player, valid_direction)
        dir_func(direction, player)

    elif player == 6:
        valid_direction = 'ns'
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ").lower()

        not_valid(player, valid_direction)
        dir_func(direction, player)

    elif player == 3:
        print("Victory!")
        victory = True


            
    

