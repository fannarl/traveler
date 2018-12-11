# Assume that the current US population is 307,357,870 and that these rates of change are provided:
# a birth every 7 seconds
# a death every 13 seconds
# a new immigrant every 35 seconds
# Write a program that takes years as input (as an integer) and prints out an estimated population (as an integer).  
# Assume that there are exactly 365 days in a year.

years_str = input("Years: ") # do not change this line

# Missing lines here
original_population = 307357870
years_int = int(years_str)
seconds = years_int * 365 * 24 * 60 * 60

births = seconds // 7
deaths = seconds // 13
immigrant = seconds // 35

new_population = original_population + births + immigrant - deaths


print("New population after", years_int, " years is ", int(new_population)) # do not change this line
