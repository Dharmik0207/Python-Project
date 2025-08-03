# name = input("What is your Name..?")
# print("Hi " +name)

given_name = "Dharmik"
family_name = "Gadhiya"

name = given_name + " " + family_name
print(name)

#Changing the value of a variable

word = input("Please type in a word: ")
print(word)

word = input("And another word: ")
print(word)

word = input("And Last word: ")
print(word)

number1 = 100
number2 = "100"

print(number1 + number1) #200
print(number2 + number2) #100100

result = 10*25
print("The Result is " +str(result)) #The Result is 250
print("The final Result is", result) #The final Result is 250
print(f"The result is {result}.\n") #The result is 250.

#Hi Dharmik , you are 26 years old. You live in Surat,Gujarat.

name = "Dharmik"
age = 26
city = "Surat,Gujarat"
print(f"Hi {name}, you are {age} years old. You live in {city}.")

#my name is Tim Tester, I am 20 years old

#my skills are
# - python (beginner)
# - java (veteran)
# - programming (semiprofessional)

#I am looking for a job with a salary of 2000-3000 euros per month

name = "Tim Tester"
age = 20
skill1 ="python"
level1 ="beginner"
skill2 ="java"
level2 ="veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper =3000

print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")


# Write your solution here
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8

x = 27
y = 15
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

# Fix the code
#print(5)
#print(" + ")
#print(8)
#print(" - ")
#print(4)
#print(" = ")
#print(5 + 8 - 4)


print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)
# 5 + 8 - 4 = 9