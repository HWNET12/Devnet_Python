#!/usr/bin/python3

#Defining a class
class Location:
    #Defining the __init__ function By convention, the first parameter is called self. The self parameter 
    #is a reference to the current instance of the class itself and is used to access variables that belong to the 
    #entire class.

    def __init__(self, name, country):
        self.name = name
        self.country = country

#Define a new method call myLocation and assigned it the self paramater

    def MyLocation(self):
        print(f"Hi my name is {self.name} and I live in {self.country}.")

#Instantiate the Location class multiple times and call the myLocation method.

# First instantiation of the class Location
loc1 = Location("Tomas", "Portugal")
# Three more instantiations and method calls for the Location class
loc2 = Location("Yusuf", "Senegal")
loc3 = Location("Amare", "USA")
loc1.MyLocation()
loc2.MyLocation()
loc3.MyLocation()
