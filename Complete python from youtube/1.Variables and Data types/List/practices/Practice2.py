list=[1,2,3,2,1]
copyList=list.copy()
copyList.reverse()
if(list==copyList):
    print("It is a pallindrome list")
else:
    print("It is not a pallindrome")