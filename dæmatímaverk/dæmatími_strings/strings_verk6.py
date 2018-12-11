name = input("Input a name: ")

last, first = name.split(" ")


first_upper = first.upper()
first_1 = first_upper[0] + ". "

last_1, throwaway = last.split(",")
last_upper1 = last_1.upper()
last_upper2 = last_upper1[0]
last_lower = last_1[1:]

print(first_1 + last_upper2 + last_lower)