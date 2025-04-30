# sets are mutable, but the elements are immutable,and duplicates values are not allowed in sets.
# we can store every type of "data types" in the sets except "lists" and "dictionary"

collections={1,2,3,4,3,2,1}

print(collections)

# for creating an empty set we have to use "variable_name=set()"

emptySet=set()
emptySet.add(1)
emptySet.add(2)
emptySet.add(3)
emptySet.add("karan")
emptySet.add("paul")
emptySet.remove(2)
emptySet.pop()
#.pop() method doesnot take any arguments its deletes any elements randomly from the set.

print(emptySet)
print(len(emptySet))
print(type(emptySet))
emptySet.clear()
print(emptySet)