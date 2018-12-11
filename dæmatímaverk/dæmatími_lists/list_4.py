def make_new_row(row, n):
    row = [1]
    y = [0]
    for n in range(max(n,0)):
        print(row)
        row=[l+r for l,r in zip(row+y,y+row)]
    return n>=1
# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []

new_row = make_new_row(new_row, height)