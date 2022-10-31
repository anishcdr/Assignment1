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
