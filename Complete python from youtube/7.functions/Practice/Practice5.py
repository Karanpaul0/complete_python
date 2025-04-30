def oddEvenChecker(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"
checker=oddEvenChecker(int(input("Enter the number for which you want to check for odd/even:= ")))
print(checker)