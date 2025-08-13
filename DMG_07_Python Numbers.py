# Integer
x = 1
y = 836377383628292
z = -7356383

print(type(x))
print(type(y))
print(type(z))

#Float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion

x = 1
y = 2.8
z = 1j

#convert from int to float
a = float(x)
print(a)
print(type(a))

#convert from float to int
b = int(y)
print(b)
print(type(b))

#convert from int to complex
c = complex(z)
print(c)
print(type(c))

#Random Number
import random
print(random.randrange(1,10))

import random
print(random.randrange(1,100))
