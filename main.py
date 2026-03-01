# == Initial ==

print("Secure Acces Control System")

# Part one: Age Validation

name= input("Enter your name: ")
age= int(input("Now, enter your age: "))

if age < 12:
    print(f"Hi, {name}! We are sorry but you do not meet the age requirement.")
else:
    print(f"Hi, {name}! You meet the age requirement.")



