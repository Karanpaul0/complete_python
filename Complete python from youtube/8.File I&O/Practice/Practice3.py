with open("practice.txt", "r") as f:
    data=f.read()
    if(data.find("learning")<=0):
        print("not found..!")
    else:
        print("found...!")