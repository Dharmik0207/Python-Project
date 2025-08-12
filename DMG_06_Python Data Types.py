'''
Built-in Data Types
Text Type : str
Numeric Type : int, float, complex
Sequence Type : list, Tuple, range
Mapping Type : dict
Set Type : set, frozenset
Boolean Type :  bool
Binary Type : bytes, bytearray, memoryview
None Type : NoneType
'''

# str
x = "Hello World!"
x = str("Hello World!")
#display x:
print(x)
#display the data type of x:
print(type(x))

# int
x = 20
x = int(20)
print(x)
print(type(x))

# float
x = 20.5
x = float(20.5)
print(x)
print(type(x))

# complex
x = 1j
x = complex(1j)
print(x)
print(type(x))


#	list []
x = ["apple", "banana", "cherry"]
x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))

#	tuple ()
x = ("apple", "banana", "cherry")
x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))

# range
x = range(6)
print(x)
print(type(x))

#	dict
x = {"name" : "John", "age" : 36}
x = dict(name="John", age = 36)
print(x)
print(type(x))

#	set {}
x = {"apple", "banana", "cherry"}
x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))

#	frozenset({})
x = frozenset({"apple", "banana", "cherry"})
x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))

# bool
x = True
x = bool(5)
print(x)
print(type(x))

# bytes
x = b"Hello"
x = bytes(5)
print(x)
print(type(x))

# bytearray
x = bytearray(5)
print(x)
print(type(x))

# memoryview
x = memoryview(bytes(5))
print(x)
print(type(x))

# NoneType
x = None
print(x)
print(type(x))