#Variable Type
x = str(3)
y = int(3)
z = float(3)
print(type(x))
print(type(y))
print(type(z))

#Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python Output Variable
x = "Python is awsome"
print(x)

x = "Python "
y = "is "
z = "Awsome "
print(x, y, z)
print(x + y + z)

x = 5
y = "John"
# In the print() function,
# when you try to combine a string and a number with the + operator, Python will give you an error:
#print(x + y)
print(x , y)

#Global Variables
#1
x = "awsome"

def myfunc():
    print("Python is " +x)

myfunc()

#2
x = "awsome"

def myfunc():
    x = "Fantastic"
    print("Python is " +x)

myfunc()

print("Python is " +x)

#The global Keyword

def myfunc():
    global x
    x = "Fantastic"

myfunc()

print("Python is " + x)

x = "Awsome"

def myfunc():
    global x
    x = "Fantastic"

myfunc()

print("Python is " +x)


