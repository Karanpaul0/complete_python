
# lists are mutable



myList=[1,2,3,4,5,6,7,8,9]
print(myList)
print(myList[:8])
print(myList[-9:-1])
myList.append(41)
myList.remove(4)
print(myList)
myNewList=[9,8,7,6,5,4,3,2,1,0]
myNewList.sort()
print(myNewList)
list2=[1,3,4,5,7,3,9,3,0]
list2.sort()
list2.reverse()
print(list2)

# list.insert(index,value)

list2.insert(0,"karan paul")

# list2.remove() is used to delete the element
# list2.pop() is used to remove index'a element
print(list2)