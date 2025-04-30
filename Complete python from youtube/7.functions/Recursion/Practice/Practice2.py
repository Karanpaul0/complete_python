list=[1,2,3,4,5,6,7,8,9]
def print_list(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)
print_list(list)