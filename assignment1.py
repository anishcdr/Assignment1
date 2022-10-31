#Assignment1

#List
mylist=[1,"a",True]
print(mylist)

print(type(mylist))

#Use of positive and negative indexing
string="="
for i in range(3):
  print(mylist[i],string,mylist[i-3])

#Updating the data
n=input("Enter the index number of the data you want to change ")
data=input("Enter the data you want to replace with ")
mylist[int(n)]=data
print("New list=",mylist)

#Appending the data
add=input("Enter the data which you want to add ")
mylist.append(add)
print("New list=",mylist)

#Inserting
i=input("Enter the position you want to insert the data at ")
insert=input("Enter the data you want to insert ")
mylist.insert(int(i),insert)
print("New list=",mylist)

#Deleting particular elements on a list
n=input("Enter the index number of the element you want to delete")
del mylist[int(n)]
print(mylist)

#Or

mylist.pop(int(n))

data=input("Enter the data you want to remove")
mylist.remove(data)

#Dictionary
mydic={"First element":1,
       "Second element":"a",
       "Third element":True}
print(mydic)

#Updating the dictionary
index=input("Enter the index of the element you want to change ")
data=input("Enter the element you want to update with ")
mydic[index]=data
print(mydic)

#Deleting certain values
index=input("Enter the index of the element you want to delete ")
del mydic[index]
print(mydic)

#Sets
myset={1,"a",True}
print(myset)

#Union of sets
set2={2,"b",False}
myset.union(set2)
print(myset)

#Intersection of sets
set3={3,"c",True}
myset.intersection(set3)
print(myset)


#Deleting all elements in a set
set2.clear()
print(set2)

#Or

del set3
#print(set3) gives error

#Or

set4={1,"d",True}
set4.pop
print(set4)

#Appending or adding or updating in a set
data=input("Enter the element you want to append ")
myset.add(data)
print(myset)

#Or

myset.update(data)
print(myset)

#Sets
myset={1,"a",True}
print(myset)

#Union of sets
set2={2,"b",False}
myset.union(set2)
print(myset)

#Intersection of sets
set3={3,"c",True}
myset.intersection(set3)
print(myset)


#Deleting all elements in a set
set2.clear()
print(set2)

#Or

del set3
#print(set3) gives error

#Or

set4={1,"d",True}
set4.pop
print(set4)

#Appending or adding or updating in a set
data=input("Enter the element you want to append ")
myset.add(data)
print(myset)

#Or

myset.update(data)
print(myset)

#Functions
def array(n):
  yourlist=[]
  for i in range(n):
    print("No.",i)
    element=input("element in the list is ")
    yourlist.append(element)
  print("Your list is=",yourlist)
n=input("Number of elements= ")
array(int(n))

#Mutability of a set
myset={"Data", 213,253}
myset[1]=1 
#Conclusion: Gives an error as a set is not ordered

set1={1,2,3}
set2={'a','b'}
print(set1.union(set2))
#Or
print(set1|set2)
#Conclusion: Union of sets is possible

#Intersection of sets
print(set1.intersection(set2))
#Or
print(set1&set2)
#Conclusion: Intersection of sets is possible

#Deleting all elements in a set
set1.clear()
print(set1)
#Or
del set2
#print(set2) gives an error as it is undefined now
#Or
set1.pop
print(set1)
#Conclusion: Elements in a set can be deleted

#Appending or adding or updating in a set
tuple1=(1,2,3)
myset.add(tuple1)
print(myset)
#Or
dic1={1:10,
      2:11}
myset.update(dic1)
print(myset)
#Conclusion: Elements in a set can be updated

'''This shows that in a set, although, the elements cannot be updated individually, they can be modified by other means, thus we can say that a set is mutable'''
