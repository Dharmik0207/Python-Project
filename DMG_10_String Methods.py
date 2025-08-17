# capitalize() | Converts the first character to upper case
text = "hello, and welcome to my world."
x = text.capitalize()
print(x)

# casefold() | convererts string into lower case
text = "Hello, And Welcome To My World."
x = text.casefold()
print(x)

#center() | Returns a centered string
text = "banana"
x = text.center(20, "O")
print(x)

#count()  | Returns the number of times a specified value occurs in a string
text = "I love apples, apple are my favorite fruit"
x = text.count("apple")
x = text.count("apple",10,24)
print(x)

#encode() | Returns an encoded version of the string

text = "My name is Ståle"
x = text.encode()
print(x)


