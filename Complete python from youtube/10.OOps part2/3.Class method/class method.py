class Person:
    name="anonomous"
    @classmethod
    def changeName(cls,name):
        cls.name=name
        
        
p1=Person()
p1.changeName(input("Enter your name:- "))
print(p1.name)
print(Person.name)