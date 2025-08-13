print("Hello!")
print('Hello!')

#Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String to a variable

a = "Hello"
print(a)

# Multi-line String
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(a)

#Strings are Arrays

a = "Hello, world!"
print(a[1])

#Looping Through a String

for x in "banana":
    print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

text = "Dharmik Mukeshbhai Gadhiya"
if "Dharmik" in text:
    print("Yes, 'Dharmik' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

text = "Dharmik Mukeshbha Gadhiya"
if "Kirti" not in text:
    print("No, 'Kirti' is NOT present.")

# Python - Slicing Strings
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5]) #Note: The first character has index 0.

#Slice From the Start
print(b[ :5])

#Slice To the End
print(b[2:])

#Negative Indexing
print(b[-5:-2])
