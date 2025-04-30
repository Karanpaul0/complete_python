tuple=(1,4,9,16,25,36,49,64,81,100,49)
sEl=int(input("Enter the enlement you want to search:- "))
for i in tuple:
    gotEl=tuple.index(i)
    if(i==sEl):
        print(f"your element is found at index number:- {gotEl}")