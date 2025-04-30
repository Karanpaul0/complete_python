tuple=(1,4,9,16,25,36,48,64,81,100)
num=int(input("enter the number you want to search in the tuple:- "))
i=0
while(i<(len(tuple)-1)):
    if(num==tuple[i]):
        store=tuple[i]
        print(f" Found at index number:- {tuple.index(store)}")
    i+=1
