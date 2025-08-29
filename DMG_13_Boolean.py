from operator import truediv

print(bool("Hello"))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool())
print(bool([]))
print(bool({}))
print(10>9)
print(10==9)
a = 200
b = 33

if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

def myfunction() :
    return True
print(myfunction())

def myfunction() :
    return True

if myfunction() :
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x,int))