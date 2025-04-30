class Student:
    college_name="Vaagdevi degree and pg college"
    
    def __init__(self,marks):
        self.marks=marks
    
    def hello(self,name):
        self.name=name
        print("hello", name)
        
    def get_marks(self):
        return self.marks
    
s1=Student(70)
print(s1.college_name)
s1.hello("karan")
print(f"Your marks is {s1.get_marks()}")