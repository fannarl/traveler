Vehicals = []

class Vehicle(object):
    def __init__(self, vehicle_license, year, weight = 0, fee = 0):
        self.vehicle_license = vehicle_license
        self.year = year
        self.weight = weight
        self.fee = fee
    
    def get_year(self):
        return self.year

    def get_license(self):
        return self.vehicle_license

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight):
        self.weight = new_weight

    def get_fee(self):
        return self.fee

    def set_fee(self, new_fee):
        self.fee = new_fee


    def __str__(self):
        Return_stirng = "Vehicle: {} {} Weight={:.2f} Fee=${:.2f}".format(self.get_license(), self.get_year(), self.get_weight(), self.get_fee())
        Vehicals.append(Return_stirng)
        return Return_stirng
####################################################################################################
class Car(Vehicle):
    def __init__(self, vehicle_license, year, style, weight = 0, fee = 0):
        super().__init__(vehicle_license, year)
        self.style = style 

    def set_weight(self, new_weight):
        self.weight = new_weight
        
        if new_weight < 3000:
            self.fee = 30
        elif 3000 <= new_weight < 5000:
            self.fee = 40
        else:
            self.fee = 50

    def __str__(self):
        Return_stirng = "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(self.get_license(), self.get_year(), self.style, self.get_weight(), self.get_fee())
        Vehicals.append(Return_stirng)
        return Return_stirng
####################################################################################################
class Truck(Vehicle):
    def __init__(self, vehicle_license, year, wheels, weight = 0, fee = 0):
        super().__init__(vehicle_license, year)
        self.wheels = wheels

    def set_weight(self, new_weight):
        self.weight = new_weight
        
        if new_weight < 3000:
            self.fee = 40
        elif 3000 <= new_weight < 5000:
            self.fee = 50
        elif 5000 <= new_weight < 10000:
            self.fee = 60
        else:
            self.fee = 70

    def __str__(self):
        Return_stirng = "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(self.get_license(), self.get_year(), self.wheels, self.get_weight(), self.get_fee())
        Vehicals.append(Return_stirng)
        return Return_stirng
####################################################################################################
class Motorbike(Vehicle):
    def __init__(self, vehicle_license, year):
        super().__init__(vehicle_license, year)

    def __str__(self):
        Return_stirng = "Motorbike: {} {} {} cc Fee=${:.2f}".format(self.get_license(), self.get_year(), self.get_CC(), self.get_fee())
        Vehicals.append(Return_stirng)
        return Return_stirng
    def get_CC(self):
        return self.cc
    
    def set_CC(self, new_cc):
        self.cc = new_cc

        if new_cc < 50:
            self.fee = 10
        elif 50 <= new_cc < 200:
            self.fee = 20
        else:
            self.fee = 35

####################################################################################################
def main():
#     # Create some vehicles    
#     v1 = Vehicle("AB 123", 2010)
#     c1 = Car("SF 735", 2007, "Station")
#     t1 = Truck("TU 765", 1994, 6)
#     b1 = Motorbike("XY 666", 2005)

#     c1.set_weight(3500)
#     t1.set_weight(9000)
#     b1.set_CC(250)
        
    # Print info    
    # print(v1)
    # print(c1)
    # print("The weight of the car is: {:.2f}".format(c1.get_weight() ))
    # print(t1)
    # print("The fee for the truck is: {:.2f}".format(t1.get_fee() ))
    # print(b1)
    # print("The CC of the bike is: {:.2f}".format(b1.get_CC() ))
    # print()
    # Put the four vehicles into a list.     
    # Then loop through the list and call the print function for each of the vehicles.   
    # You have to implement this part of the main program!
    # YOUR CODE GOES HERE  
    for index in Vehicals:
        print(index)
    # v1 = c1
    # print(v1)
    # print()
main()

# Vehicle: AB 123 2010 Weight=0.00 Fee=$0.00 
# Car: SF 735 2007 Station Weight=3500.00 Fee=$40.00 
# The weight of the car is: 3500.00 
# Truck: TU 765 1994 6 wheels Weight=9000.00 Fee=$60.00 
# The fee for the truck is: 60.00 
# Motorbike: XY 666 2005 250 cc Fee=$35.00 
# The CC of the bike is: 250.00 

# Vehicle: AB 123 2010 Weight=0.00 Fee=$0.00 
# Car: SF 735 2007 Station Weight=3500.00 Fee=$40.00 
# Truck: TU 765 1994 6 wheels Weight=9000.00 Fee=$60.00 
# Motorbike: XY 666 2005 250 cc Fee=$35.00 
# Car: SF 735 2007 Station Weight=3500.00 Fee=$40.00 

# Vehicle: AB 123 2010 Weight=0.00 Fee=$0.00
# Car: SF 735 2007 Station Weight=3500.00 Fee=$40.00
# The weight of the car is: 3500.00
# Truck: TU 765 1994 6 wheels Weight=9000.00 Fee=$60.00
# The fee for the truck is: 60.00
# Motorbike: XY 666 2005 250 cc Fee=$35.00
# The CC of the bike is: 250.00

# Vehicle: AB 123 2010 Weight=0.00 Fee=$0.00
# Car: SF 735 2007 Station Weight=3500.00 Fee=$40.00
# Truck: TU 765 1994 6 wheels Weight=9000.00 Fee=$60.00
# Motorbike: XY 666 2005 250 cc Fee=$35.00
# Car: SF 735 2007 Station Weight=3500.00 Fee=$40.00