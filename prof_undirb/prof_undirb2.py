def table(size):
    MAX = size
    for i in range(1,MAX+1):
        print("{}".format(i), end="|")
        for j in range(1,MAX+1):
            print("{:>8d}".format(i*j), end="")
        print("")

def table_size():
    size = int(input("Input table size: "))
    return size

def main():
    again = True
    while again:
        size = table_size()
        if size <= 0 or size > 8:
            print("Invalid size!")
        else:
            again = False
    table(size)

main()