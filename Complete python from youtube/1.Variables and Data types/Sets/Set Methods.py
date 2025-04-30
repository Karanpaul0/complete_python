set1={1,2,3,4,5,6}
set2={2,4,6,8,10}
newSet=set1.union(set2) #in the union method both sets are compared and creatws a new set and gives output of every elements are present in both the sets
print(newSet)
print(set1,set2)



#intersection method
mySet1={1,2,3,4,5,6}
mySet2={2,4,6,8,10}
myNewSet=mySet1.intersection(mySet2)  #intersection methods compares both the sets and give output of the common elements present in both the sets.
print(myNewSet)


# performing methods on the multiple sets.
karan={6.8,6.5,6.4,7.08,7.7}
sharada={5.9,7.2,6.5,7.5,7.2}
total={6.9,6.8}
unionSet=karan.union(sharada.union(total))
intesectSet=karan.intersection(sharada.intersection(total))
bothSet=karan.union(sharada.intersection(total))
print(unionSet)
print(intesectSet)
print(bothSet)
print(len(unionSet))
print(len(intesectSet))
print(len(bothSet))