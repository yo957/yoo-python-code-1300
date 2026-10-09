""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        print(f"{self.brand} brand")
        print(f"{self.model} model")
        print(f"{self.year} year")
class Car(Vehicle):
    def __init__(self,brand, model, year,number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
    def get_info(self):
        super().get_info()
        print(self.number_of_doors,"Number of doors")
car1 = Car("Toyota","Camry" , 2024,4)
car1.get_info()