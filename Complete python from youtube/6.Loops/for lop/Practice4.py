num=int(input("Enter the number upto you want to print palindrome numbers:- "))
for pali in range(1,num ,+1):
    if (str(pali)==str(pali)[::-1]):
        print(pali, " ")