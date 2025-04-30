print("Welcome to pallindrome checker..!")
num=int(input("Enter the number you want to check for the pallindrome:- "))
def isPallindrome(num):
    rev=0
    i=1
    while(i<=int(num)):
        dig=int(num%10)
        rev=(rev*10)+dig
        num/=10
        num=int(num)
    return rev
pallindrome=isPallindrome(num)
if(num==pallindrome):
    print("your number is a pallindrome")
else:
    print("your number is not a pallindrome")