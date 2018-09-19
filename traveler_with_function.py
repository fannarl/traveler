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
    if p_dir not in v_dir:
        return True
    return False
    
    
def dir_func(a_dir, a_player):
    if a_dir == "n":
        a_player = a_player + 3
    elif a_dir == "s":
        a_player = a_player - 3       
    elif a_dir == "e":
        a_player = a_player + 1
    elif a_dir == "w":
        a_player = a_player - 1  
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

    elif player == 5 or player == 9:
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

    elif player == 6:
        valid_direction = 'ns'
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ").lower()

    elif player == 3:
        print("Victory!")
        victory = True
        break

    if  not_valid(direction, valid_direction):
        print("Not a valid direction!")
        direction = input("Direction: ").lower()
        if not not_valid(direction, valid_direction):
            player = dir_func(direction, player)
    else:
        player = dir_func(direction, player)

# 1) The First solution was a bit easier since i didnt have to think about how i would implement the functions
# but after I figured it out it became clear that once you understand how to implement them it would be considerbly easier in the long run 

# 2) The second implementation is way more readable than the first since it is considirebly cleaner and not cluttered in while loops and the main
# body of the code only contains conditional statements not the actual algorithm.

# 3) In the latter implementation i could contain all the calculations that are used depending on the user input in one place instead of having to put them in
# individually for each conditional. That saves time and avoids pontential confusion and errors
