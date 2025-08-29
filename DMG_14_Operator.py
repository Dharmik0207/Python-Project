print(10 + 5)

#Python Arithmetic Operators
# +, -, *, /, %, **, //

#Python Assignment Operators
# =, +=,-=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=
x = 5
x += 5
x **= 5
print(x)
x &= 3
print(x)
print(x := 3)

#Python Comparison Operators
# ==, !=, >, <, >=, <=

#Python Logical Operators
# and, or, not
#and
x = 5
print(x>3 and x<10)
print(x<5 or x<4)
print(not (x<5 and x<10))

#Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   ## returns True because z is the same object as x
print(x is y)   #returns False because x is not the same object as y, even if they have the same content.
print(x == y)   #to demonstrate the difference bet^n "is" and "==": this comparison returns True because x = y

print(x is not z)   # returns False because z is the same object as x
print(x is not y)   # returns True because x is not the same object as y, even if they have the same content.
print(x != y)  #to demonstrate the difference bet^n "is not" and "!=": this comparison returns False because x = y

#Python Membership Operators
x = ["apple", "banana"]
print("banana" in x)

print("pineapple" not in x) #returns True because a sequence with the value "pineapple" is not in the list.

#Python Bitwise Operators

#& 	AND	Sets each bit to 1 if both bits are 1.	x & y
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010

"""
#|	OR	Sets each bit to 1 if one of two bits is 1.	x | y
print(6 | 3)

#^	XOR	Sets each bit to 1 if only one of two bits is 1.	x ^ y
print(6 ^ 3)
#~	NOT	Inverts all the bits	~x
print(~3)
#<<	Zero fill left shift  Shift left by pushing zeros in from the right
# and let the leftmost bits fall off	x << 2
print(3 << 2)
#>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left,
# and let the rightmost bits fall off	x >> 2
print(8 >> 2)

#Operator Precedence | Operator precedence describes the order in which operations are performed.

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))

#Multiplication * has higher precedence than addition +, and
#therefore multiplications are evaluated before additions:

print(100 + 5 * 3)

# The precedence order is described in the table below, starting with the highest precedence at the top:

#1.() | 2. ** | 3. +x -x ~x | 4. * / // % | 5. + - | 6. << >> | 7. & | 8. ^ | 9. |
#10. == != > >= < <= is is not in not in | 11. not | 12. and | 13. or
