# BRIX BROY IDANAN

# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2021 - year)

# *Be sure to return the age, not print 

class Car:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        currentyear = 2021
        age = currentyear-int(self.year)
        self.year = age
        return age

print("Input Car Details")
print("Make: ")
make = input()
print("\nModel: ")
model = input()
print("\nYear: ")
year = input()

car = Car(year,make,model)
print("\n\nYour car is",car.age(), "year's old\n")
    

