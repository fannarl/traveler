def where_r_u(l_input, n_loc):
    new_location = 0
    furthest_left = 1
    furthest_right = 10 

    if l_input == "r":
        if n_loc == furthest_right:
            new_location = n_loc
        else:
            new_location = n_loc + 1
    elif l_input == "l":
        if n_loc == furthest_left:
            new_location = n_loc
        else:
            new_location = n_loc - 1

    return new_location


f_position = int(input("Input a position between 1 and 10: " ))
location = f_position
     
while 1 == 1:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    new_pos = input("Input your choice: ")
    if new_pos == "r" or new_pos == "l":
        location = where_r_u(new_pos, location)
        print("New position is: ", location)
    else:
        break
print("New position is: ", location)



