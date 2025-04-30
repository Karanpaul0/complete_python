class Student:
     def __init__(self,name,mark1,mark2,mark3):
         self.name=name
         self.mark1=mark1
         self.mark2=mark2
         self.mark3=mark3
        
     def mark_avg(self):
        avg= (self.mark1+self.mark2+self.mark3)/3
        return avg
          
          
          
names=input("Enter your name:-")
marks1=int(input("Enter your mark1:- "))         
marks2=int(input("Enter your mark2:- "))         
marks3=int(input("Enter your mark3:- "))


         
s1=Student(names,marks1,marks2,marks3) 
avg=s1.mark_avg()
print(f"Hello mr. {s1.name} \nYour avg marks is:- {avg}")
