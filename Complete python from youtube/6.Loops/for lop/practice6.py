num=int (input("Enter the number for which you wnat factorial:- "))
fact=1
for i in range(1,num+1,+1):
    fact*=i
print(fact)