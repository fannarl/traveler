# is_prime function definition goes here
def is_prime(num_input):
    div_count = 0
    for i in range(1, num_input + 1):
        if(num_input % i) == 0:
            div_count = div_count + 1
                
    if div_count == 2:
        print(num_input,"is a prime")
    else:
        print(num_input, "is not a prime")
                
    
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
is_prime(num)