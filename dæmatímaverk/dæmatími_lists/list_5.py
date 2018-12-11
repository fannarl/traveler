def input_vector(size):
    how_big = []
    for i in range (size):
        i = float(input("Element no " + str(i+1) + ": "))
        how_big.append(i)
    return how_big

def dot_product(item1,item2):
    how_big = 0
    for x in range(len(item1)):
        how_big += (item1[x]*item2[x])
    return how_big

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))