class University:
    uName="Kakatiya University"
class College:
    cName="Vaagdevi degree and pg college"
class Student(University,College):
    def __init__(self,sName):
        self.sName=sName
        
s1=Student(input("Enter your name:- "))

print(f"I am {s1.sName}\nI am studing in {s1.cName}\nMy university name is {s1.uName}")