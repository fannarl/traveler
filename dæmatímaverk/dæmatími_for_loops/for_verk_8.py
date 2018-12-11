stars = int(input("Max number of stars: ")) # Do not change this line

for i in range(0,stars):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")
for y in range(stars,0,-1):
    for x in range(0,y-1):
        print("*",end="")
    print("\r")
