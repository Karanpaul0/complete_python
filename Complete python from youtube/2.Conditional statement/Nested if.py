gender=input("enter your gende(male/female):- ")
age=int(input("enter your age:- "))
if(gender=="male"):
    if(age>=18):
        print("You are eligible for applying the voter id card...!")
    elif(age<18 and age>0):
        print("your not eligible for applying the voter id card..!")
    else:
        print("you entered an invalid age madarchor gandu laude...!")
elif(gender=="female"):
    if(age>=21):
        print("You are eligiblefor apply for the voter id card..!")
    elif(age<21 and age>0):
        print("your not eligible for applying the voter id card..!")
    else:
        print("you entered an invalid age madarchor gandu laude...!")
else:
    print("you entered an invalid gender madarchor gandu laude...!")