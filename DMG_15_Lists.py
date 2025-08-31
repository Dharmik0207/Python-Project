mylist = ["apple", "banana", "cherry"]
# Lists are used to store multiple items in a single variable.

print(mylist)

#List Items :
#List items are ordered, changeable, and allow duplicate values.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
print(len(thislist))

# List Items - Data Types :
#List items can be of any data type:    String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# A list can contain different data types:

list1 = ["abc", 34, True, 40, "male"]
print(list1)

# type() :
#From Python's perspective, lists are defined as objects with the data type 'list':

print(type(list1))

# The list() Constructor :

thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Python Collection (Arrays)

# List : List is a collection which is ordered and changeable.Allows duplicates members.
# Tuple : Tuple is a collection which is ordered and unchangeable. Allows duplicates members.
# Set : Set is a collection which is unordered, unchangeable*,(but you can remove and/or add items whenever you like.)
# Dictionary : Dictionary is a collection which is ordered and changeable. No duplicates members.

# Python - Access List Items
# The first item has index 0.
mylist = ["apple", "banana", "cherry"]
print(mylist[1])

#Negative Indexing : Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

print(mylist[-1]) #Ans : cherry

#Range of Indexes
mylist = ["Dharmik", "Kirti", "Brijesh", "Harsh", "Mayur", "Hardik"]
print(mylist[0:4]) #Ans : ['Dharmik', 'Kirti', 'Brijesh', 'Harsh']
# Note: The search will start at index 2 (included) and end at index 5 (not included).

#By leaving out the start value, the range will start at the first item:
#This example returns the items from the beginning to, but NOT including, "Mayur".
print(mylist[:4])
#This example returns the items from "Brijesh" to the end.
print(mylist[2:])

#Range of Negative Indexes.
#This example returns the items from "Brijesh" (-4) to, but NOT including "Hardik" (-1):
print(mylist[-4:-1])

#Check if Item Exists
mylist = ["Dharmik", "Kirti", "Brijesh", "Harsh", "Mayur", "Hardik"]
if "Kirti" in mylist:
    print("Yes, 'Kirti' is in the name list.")
else:
    print("No, 'Kirti' is not in the name list.")


# NEW TOPIC ::

# Change List Items

mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist)

# Change a Range of Item Values

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)
#Note: The length of the list will change when the no. items inserted does not match the no. items replaced.

mylist = ["apple", "banana", "cherry"]
mylist[1:3] = ["watermelon"]
print(mylist)
#Note: The length of the list will change when the no. items inserted does not match the no. items replaced.

# Insert Items :
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# Insert "watermelon" as the third item:

mylist = ["apple", "banana", "cherry"]
mylist.insert(2, "watermelon")
print(mylist) # Note: As a result of the example above, the list will now contain 4 items.

# NEW TOPIC : Python - Add List Items

# To add an item to the end of the list, use the append() method:

mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist)

# Insert Items

# To insert a list item at a specified index, use the insert() method.

mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "orange")
print(mylist)

# Extend List

# To append elements from another list to the current list, use the extend() method.

mylist = ["apple", "banana", "cherry"]
mylist1 = ["orange", "blueberry", "Mango"]
mylist.extend(mylist1)
print(mylist)   #The elements will be added to the end of the list.

# Add Any Iterable

mylist = ["apple", "banana", "cherry"]
mytuple = ("kiwi", "orange")
mylist.extend(mytuple)
print(mylist)



# NEW TOPIC : Python - Remove List Items.

# Remove Specified Item | Remove : "banana".

mylist = ["apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "apple"]
mylist.remove("apple")
print(mylist)

# Remove Specified Index | The pop() method removes the specified index.

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "apple"]
mylist.pop(1)
print(mylist)

#If you do not specify the index, the pop() method removes the last item.

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "apple", "mango"]
mylist.pop()
print(mylist)

# The del keyword also removes the specified index:

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "apple", "mango"]
del mylist[0]
print(mylist)

# The del keyword can also delete the list completely.

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "apple", "mango"]
del mylist

# Clear the List    | The clear() method empties the list.

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "apple", "mango"]
mylist.clear()
print(mylist)


# NEW TOPIC | Python - Loop Lists

#You can loop through the list items by using a for loop:
# print all items in the list, one by one:
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "apple", "mango"]
for x in mylist:
    print(x)

# Loop Through the Index Numbers
# Print all items by referring to their index number:
mylist = ["Dharmik", "Kirti", "Brijesh", "Harsh", "Mayur", "Hardik"]
for i in range(len(mylist)) :
    print(mylist[i])    #The iterable created in the example above is [0, 1, 2].

# Using a While Loop

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "apple", "mango"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

# Looping Using List Comprehension.

mylist = ["apple", "banana", "cherry"]
[print(x) for x in mylist]

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "apple", "mango"]
[print(x) for x in mylist]