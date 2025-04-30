class Student:
    def __init__(self,phy,bio,math):
        self.phy=phy
        self.bio=bio
        self.math=math
    
    @property
    def percentage(self):
        return str((self.phy + self.bio+self.math)/3)+"%"
    
    
s1=Student(90,91,93)
s1.phy=10
print(s1.percentage)