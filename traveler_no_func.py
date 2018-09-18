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
    if player == 1 and player == 2 and player == 3:
        valid_direction = 'n'
        print("You can travel: (N)orth.")
        direction = input("Direction: " )
        player += 3
    elif player == 4:
        valid_direction='nse'
        print("You can travel: (N)orth or (S)outh or (E)ast.")
        direction = input("Direction: " )
        #checkar á valid direction breytuni og skoðar hvort
        #inputið sé rétt
        for i in valid_direction:
            if direction == i:
                if i == "n":
                    player += north
                elif i == "s":
                    player -= south
                    break
                elif i == "e":
                    player += east
                else:
                    print("not a valid direction!")
    elif player == 5:
        valid_direction = 'ws'
        print("You can travel: (W)est or (S)outh.")
        direction = input("Direction: " )
        for i in valid_direction:
            if direction == i:
                if i == "w":
                    player -= west
                elif i == "s":
                    player -= south


            
    

