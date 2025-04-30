class Student:
    college_name="vaagdevi degree and pg college" #class attribute
    def __init__(self,fullname,rollnumber):
        self.name=fullname  #object attribute
        self.number=rollnumber
print("please enter 1 student's details here..!")
s1=Student(input("Enter your name:- "),int(input("Enter your roll number:- ")))
print("pleasw enter 2 student's details here...!")
s2=Student(input("Enter your name:- "),int(input("Enter your roll number:- ")))
print("Adding a new student's details to database....!")
print(f"1st Student details:-\nName={s1.name}\nRoll Number={s1.number}")
print(f"2nd Student details:-\nName={s2.name}\nRoll Number={s2.number}")