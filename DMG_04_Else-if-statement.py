'''
goals_home = int(input("Home goal scored..."))
goals_away = int(input("Away goal scored..."))

if goals_home > goals_away:
    print("The home team won!..")
elif goals_away > goals_home:
    print("The away team won!..")
else :
    print("It's a Tie!..") '''

# Holiday Calander :
'''
print("Holiday calendar")
date = input("What is the date today..?")

if date == "Dec 26":
    print("It's Boxing Day..")
elif date == "Dec 31":
    print("It's Hogmanay..")
elif date == "Jan 1":
    print("It's new year..")
print("Thanks and bye..") '''

n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4 :
    greatest = n1
elif n2 > n3 and n2 > n4 :
    greatest = n2
elif n3 > n4 :
    greatest = n3
else:
    greatest = n4

print(f" {greatest} is the greatest of the numbers.")