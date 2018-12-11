def board(dim_list):
    for i in dim_list:
        for x in i:
            print('{:>5}'.format(x), end='')
        print('')

def dimension_list(dim_inp):
    dim_list = []
    dim_list1 = []
    dim_list2 = []
    dim_list_down = []
    dimension = dim_inp * dim_inp
    for i in range(1,dimension + 1):
        dim_list.append(i)
    while dim_list:
        for x in dim_list[:dim_inp]:
            dim_list1.append(x)
            dim_list.remove(x)
        dim_list2.append(dim_list1)
        dim_list1 = []
    dim_list_down = [[row[i] for row in dim_list2] for i in range(len(dim_list2[0]))]
    return dim_list2, dim_list_down

def player_x(dim_list):
    player_inp = input("X position: ")
    result = player(dim_list, player_inp, "X")
    return result

def player_o(dim_list):
    player_inp = input("O position: ")
    result = player(dim_list, player_inp, "O")
    return result

def player(seq, inp, player):
    #### virkar ekki fyrir 4 plús þar sem það splittar upp tölustöfum með 2 eða leyrri stöfum í ####
    chk = False
    for i in inp:
        if inp == i:
            chk = True
    result = seq
    if chk == True:
        result = sequence(dim_list, inp, player)
        board(seq)
    return result

def sequence(seq, inp, player):
    in_put = inp
    for lst in seq:
        for i, x in enumerate(lst):
            if x == int(in_put):
                lst[i] = player
    return seq

def number_of_moves(moves):
    moves -= 1
    return moves

def all_same(items):
    return all(x == items[0] for x in items)

def line_victory(dim_list):
    satt = all_same(dim_list[0])
    print(satt)


def play(dim_list,dim_inp):
    victory_royale = False
    NumberOfMoves = dim_inp * dim_inp
    while not victory_royale:
        if NumberOfMoves == 0:
            victory_royale = True
            print("Draw!")
            return victory_royale
        else:
            dim_list = player_x(dim_list)
            line_victory(dim_list)
            NumberOfMoves = number_of_moves(NumberOfMoves)
            if victory_royale == True:
                return victory_royale
            if NumberOfMoves == 0:
                victory_royale = True
                print("Draw!")
                return victory_royale
            dim_list = player_o(dim_list)
            line_victory(dim_list)
            NumberOfMoves = number_of_moves(NumberOfMoves)


dimension_inp = int(input("Input dimension of the board:"))
dim_list, dim_list_down = dimension_list(dimension_inp)
board(dim_list)
play(dim_list,dimension_inp)
# except TypeError:
#     print("Illegal move!")