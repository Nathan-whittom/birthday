from datetime import date

print("Welcome,")
m = input("Enter your Birth Month:")
d = input("Enter your Birth Day:")
y = input("Enter your Birth year:")

print("You were born on:"+ m +"," + d +","+ y)
print("Happy Birthday " * 3)
print("Happy birthday to you")

td = date.today()
print(td)