# A1 Q9 Write a program to accept user's name and age to display:
# Hello <name>, you will turn <age+1> next year

name = input("Enter your name : ")
age = int(input("Enter your age : "))

if age <= 0:
    print("Age cannot be 0 or negative")
else:
    print("Hello",name,",you will turn",age + 1,"next year")