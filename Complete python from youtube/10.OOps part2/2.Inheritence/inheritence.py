class Car:
    colour="black"
    
    @staticmethod
    def start():
        return "Car Startedd...!"
    
    
    @staticmethod
    def stop():
        return "Car Stoped..!"
    
class mahindra(Car):
    def __init__(self,name):
        self.name=name
        
    
    
car1=mahindra(input("Enter your car name:- "))
print(car1.start())
print(car1.name)
print(car1.stop())
print(car1.colour)