#format() | Formats specified values in a string
#1. What .format() does
# The .format() method replaces {} placeholders in the string with the values you give it.

text = "For only {price:.2f} dollars!"
print(text.format(price = 49))

#named indexes:
text = "My name is {fname}, I'm {age}".format(fname = "John",age = 36 )
print(text)

#numbered indexes:
text1 = "My name is {0}, I'm {1}".format("John",36)
print(text1)

#empty placeholder:
text2 = "My name is {}, I'm {}".format("John",36)
print(text2)

# :< | Left aligns the result (within the available space)
text = "we have {:<8} chickens."
print(text.format(49))

# :> | Right aligns the result (within the available space)
text ="we have {:>8} chickens."
print(text.format(49))

# :^ | Center aligns the result (within the available space)
text = "we have {:^8} chickens."
print(text.format(49))

# := | Places the sign to the left most position
text = "The temperature is {:=8} degree celsius."
print(text.format(-5))

# :+ | Use a plus sign to indicate if the result is positive or negative
text = "The temperature is between {:+} and {:+} degree celsius."
print(text.format(-3, 7))

# :-	Use a minus sign for negative values only
text = "The temperature is between {:-} and {:-} degree celsius."
print(text.format(-3, 7))

# : | Use a space to insert an extra space before +ve numbers (and a minus sign before -ve numbers)

text = "The temperature is between {: } and {: } degree celsius."
print(text.format(-3, 7))

# :, | Use a comma as a thousand separator
#Use "," to add a comma as a thousand separator:

text = "The universe is {:,} years old."
print(text.format(13800000000))

#:_	| Use a underscore as a thousand separator

text = "The universe is {:_} years old."
print(text.format(13800000000))

# :b | Binary format
text = "The binary version of {0} is {0:b}"
print(text.format(5))

# :c | Converts the value into the corresponding unicode character
text =  "The unicode version of {0} is {0:c}"
print(text.format(5))

# :d | Decimal format
text =  "We have {:d} chickens."
print(text.format(0b101)) # 0b101 : binary of 5.

# :e | Scientific format, with a lower case e
text = "we have {:e} chickens."
print(text.format(5))

# :E | Scientific format, with an upper case E
text = "We have {:E} chickens."
print(text.format(5))

# :f | Fix point number format
text = "The price is {:.2f} dollars."
print(text.format(45))

# without the ".2" inside the placeholder, this number will be displayed like this:
text = "The price is {:f} dollars."
print(text.format(45))

#:F	| Fix point number format, in uppercase format (show inf and nan as INF and NAN)
x =  float('inf')
text = "The price is {:F} dollars."
print(text.format(x))

#same example, but with a lower case f:
text = "The price is {:f} dollars."
print(text.format(x))

# :o | Octal format
text = "The octal version of {0} is {0:o}"
print(text.format(10))

# :x | Hex format, lower case
text = "The Hexa version of {0} is {0:x}"
print(text.format(255))

# :X | Hex format, upper case
text = "The Hexadecimal version of {0} is {0:X}"
print(text.format(255))

# Use "%" to convert the number into a percentage format:
text = "You scored {:%}"
print(text.format(0.25))

#Or, without any decimals:
text = "You scored {:.0%}"
print(text.format(0.25))

# format_map()	Formats specified values in a string

person = {'name' : 'Alice', 'age' : 25}
text = "My name is {name} and I am {age} years old."
print(text.format_map(person))

values = {'x':5, 'y':10}
text = "Coordinates: X ={x}, Y={y}"
print(text.format_map(values))

# index() | Searches the string for a specified value and returns the position of where it was found

text = "Hello, welcome to my world."
x = text.index("welcome")
print(x)

# isalnum()	| Returns True if all characters in the string are alphanumeric.
#Check if all the characters in the text is alphanumeric:
text = "Company12"
x = text.isalnum()
print(x)
