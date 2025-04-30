def print_num (num):
    if(num==0):
        return
    print(num)
    print_num(num-1)
print_num(int(input("Enter the number:- ")))