class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print(f"Role:-{self.role}\nDept:-{self.dept}\nSalary:-{self.salary}")
        
class Engineer(employee):
     def __init__(self,name,age):
         self.name=name
         self.age=age
         print(f"Name:-{self.name}\nAge:-{self.age}")
         super().__init__("Engineer","IT","70,000")
         
         
e1=Engineer("kara paul","20")
e1.showDetails()