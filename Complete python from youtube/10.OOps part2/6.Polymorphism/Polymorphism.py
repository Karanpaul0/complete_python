class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        
    def showNumber(self):
        print(f"{self.real}i + {self.imag}j")
    
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImag=self.imag+num2.imag
        return Complex(newReal,newImag)
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImag=self.imag-num2.imag
        return Complex(newReal,newImag)
    

n1=Complex(1,2)
n1.showNumber()

n2=Complex(3,4)
n2.showNumber() 

n3=n1+n2
n3.showNumber()

n4=n2+n3
n4.showNumber()

n5=n3-n4
n5.showNumber()