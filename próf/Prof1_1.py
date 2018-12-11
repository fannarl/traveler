month_str = input("Month: ") 
day = input("Day: ")

if month_str + " " + day == "january 1":
    print("New year's day")

elif month_str + " " + day == "june 17":
    print("National holiday")

elif month_str + " " + day == "december 25":
    print("Christmas day")

else:
    print("Not a holiday")