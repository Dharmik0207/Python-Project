# Partition() & rpartition()| Returns a tuple where the string is parted into three parts

text = "I could eat bananas all day"
x = text.partition("bananas")
print(x)

text = "My name is Dharmik Gadhiya"
x = text.partition("Dharmik")
print(x)

# replace() | Returns a string where a specified value is replaced with a specified value

text = "My Name is Kirti"
print(text)
x = text.replace("Kirti","Dharmik")
print(x)

# rfind() & rindex() |
# Searches the string for a specified value and returns the last position of where it was found

# Where in the text is the last occurrence of the letter "e"?:
text = "Saiyaara tu to badla nahi hain..."
x = text.rfind("badla")
print(x)
# Where in the text is the last occurrence of the letter "a" when you only search between position 1 and 5?:
y = text.rfind("a",1,5)
print(y)
# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
z = text.rfind("q")
print(z)

# rjust() | Returns a right justified version of the string

text = "banana"
x = text.rjust(20)
print(x,"is my favorite fruit.")
x = text.rjust(20,"O")
print(x)

# rsplit() | Splits the string at the specified separator, and returns a list.

text = "apple, banana, cherry"
x = text.rsplit(",")
print(x)

# setting the maxsplit parameter to 1, will return a list with 2 element!
text = "apple, banana, cherry"
x = text.rsplit(",", 1)
print(x)

# rstrip() | Returns a right trim version of the string.

text = "    banana      "
x = text.rstrip()
print("of all fruits", x, "is my favorite.")

# split() | Splits the string at the specified separator, and returns a list.

text = "welcome to the jungle"
x = text.split()
print(x)

text = "apple#banana#cherry#orange"
x = text.split("#",1)
print(x)

# splitlines() | Splits the string at line breaks and returns a list.

text = "Thank you for the music\nWelcome to the jungle"
x = text.splitlines()
print(x)

# startswith() | Return true if the string starts with the specified value.

text = "Hello, welcome to my world."
x = text.startswith("Hello")
print(x)

# Check if the string starts with either "Hello" or "Hi":
y = text.startswith(("Hello", "Hi"))
print(y)

# Check if position 7 to 20 starts with the characters "wel":
text = "Hello, welcome to my world."
z = text.startswith("wel",7 , 20)
print(z)


# strip() | Returns a trimmed version of the string.
# The strip() method removes any leading, and trailing whitespaces.
text = "    banana  "
x = text.strip()
print("of all fruits",x , "is my favorite")

text = ",,,,,,rrrrtttttggggg.....banana...,,,rr"
x = text.strip(",rtg.r")

# swapcase() | Swap cases, lower case becomes upper case and vice versa.

text = "Hello, My Name Is PETER"
x = text.swapcase()
print(x)

# title() | Converts the first character of each word to upper case.

text = "Welcome to my 2nd world"
x = text.title()
print(x)

text = "hello b2b2b2b and g3g3g3g"
x = text.title()
print(x)

# translate() | Returns a translated string.

#use a dictionary with ASCII codes to replace 83 (S) to 80 (P) :

mydict = {83: 80}
text = "Hello Sam!"
print(text.translate(mydict))

text = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(text.translate(mytable))

text = "Dharmik!"
mytable = text.maketrans("k", "D")
print(text.translate(mytable))

text = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(text.translate(mydict))

# upper() | Converts a string into upper case.
#The upper() method returns a string where all characters are in upper case.
#Symbols and Numbers are ignored.

text = "Hello, my friends"
x = text.upper()
print(x)

# zfill() | Fills the string with a specified number of 0 values at the beginning.

text = "50"
x = text.zfill(10)
print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
