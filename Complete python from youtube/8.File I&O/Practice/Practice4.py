with open("numbers.txt","r") as f:
    data=f.read()
    for i in range(len(data)):
        if(data[i]%2==0):
            print(data[i])