class Car:
    
    @staticmethod
    def start():
        return "Car Started...!"
    @staticmethod
    def stop():
        return "Car Stoped..!"
    
    
class ToyotaCar(Car):
    
    def __init__(self, fType):
        self.fType=fType
    
class Fortuner(ToyotaCar):
    def __init__(self, noOfSeats):
        self.noOFSeats=noOfSeats
        super().fType
        
car1=ToyotaCar(input("Enter your car's fuel type:- "))

car2=Fortuner(int(input("Enter no of seats you want in your car:- ")))


print(car1.fType)