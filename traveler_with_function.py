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

#meðan direction er ekki í valid_direction halda áfram að byðja um direction 
def not_valid(p_dir, v_dir):
    while p_dir not in v_dir:
        print("Not a valid direction!")
        p_dir = input("Direction: ").lower()
        return p_dir, v_dir

def dir_func(a_dir, a_player):
        for a_dir in valid_direction:
            if a_dir == "n":
                a_player = a_player + 3
                print("n")
            elif a_dir == "s":
                a_player = a_player - 3       
                print("s")     
            elif a_dir == "e":
                a_player = a_player + 1
                print("e")
            elif a_dir == "w":
                a_player = a_player - 1  
                print("w") 
            return a_player                       

while not victory:
    if player == 1 or player == 2:
        valid_direction = 'n'
        print("You can travel: (N)orth.")
        direction = input("Direction: " ).lower()
                     
                    
    elif player == 4:
        valid_direction='nse'
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: " ).lower()
        #checkar á valid direction breytuni og skoðar hvort
        #inputið sé rétt

    elif player == 5:
        valid_direction = 'ws'
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: " ).lower()
    

    elif player == 7:
        valid_direction = 'es'
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: " ).lower()


    elif player == 8:
        valid_direction = 'we'
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: " ).lower()


    elif player == 9:
        valid_direction = "ws"
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ").lower()


    elif player == 6:
        valid_direction = 'ns'
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ").lower()


    elif player == 3:
        print("Victory!")
        victory = True
        break
    not_valid(direction, valid_direction)
    player = dir_func(direction, player)

            
    

