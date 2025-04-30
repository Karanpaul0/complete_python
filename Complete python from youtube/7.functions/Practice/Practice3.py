num=int(input("Enter a number for you want to find a factorial:- "))
def factorial(num):
    fact=1
    for i in range(1,num+1,+1):
        fact*=i
    return fact
fact=factorial(num)
print(f"factorial of {num} = {fact}")