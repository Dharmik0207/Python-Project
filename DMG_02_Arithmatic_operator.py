
#Operator	Purpose	                  Example	      Result
#   +	      Addition	              2 + 4	            6
#   -	      Subtraction	          10 - 2.5	       7.5
#   *	      Multiplication	      -2 * 123	      -246
#   /	      Division(floating pt)    9 / 2	       4.5
#   //	      Division(int result)	   9 // 2	        4
#   %	      Modulo	               9 % 2	        1
#   **	      Exponentiation	       2 ** 3	        8

#The Body Mass Index, or BMI
height = 183.5
weight = 91.70

bmi = weight/ (height/100) ** 2
print(f"The BMI is {bmi}")

x = 5
y = 3

print(f"/ operator {x/y}")
print(f"// operator {x//y}")

#Numbers as input

# converting string--> int --> print.
input_str = input("Which year were you born ?")
year = int(input_str)
print(f"Your age at the end of the year 2021: {2021-year}")

#converting directly into integer --> print.
year = int(input("Which year were you born ?"))
print(f"Your age at end of the year 2021: {2021-year}")

height = float(input("What is your height:"))
weight = float(input("What is your weight:"))

height = height / 100
bmi = weight / height ** 2
print(f"The BMI is: {bmi}")

#Please type in a number: 3
#3 times 5 is 15

#Solution
number1 = int(input("Please type in a number:"))
number2 = int(number1 * 5)
print(f"{number1} times 5 is {number2}")

number3 = int(input("First Number: "))
number4 = int(input("Second Number: "))
number5 = int(input("Third Number: "))

sum = number3 + number4 + number5
print(f"The sum of the numbers: {sum}")

sum = 0

number = int(input("First Number: "))
sum += number

number = int(input("Second Number: "))
sum += number

number = int( input("Third Number: "))
sum += number

print(f"The sum of the numbers: {sum}")

sum += int(input("First Number: "))
sum += int(input("Second Number: "))
sum += int(input("Thid Number: "))

print(f"The sum of the numbers: {sum}")