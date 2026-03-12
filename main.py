print("Secure Access Control System")

users = []  # list of users
authorized_count = 0 

while True:

    # User's data
    name = input("Enter your name: ")

    try:
        age = int(input("Now, enter your age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        continue

    registered = input("Are you registered? (yes/no): ").strip().lower()
    vaccinated = input("Are you vaccinated? (yes/no): ").strip().lower()

    # Creating user's dictionary
    new_user = {
        "name": name,
        "age": age,
        "registered": registered,
        "vaccinated": vaccinated
    }

    # Adding to list
    users.append(new_user)

    # Access verification
    if age < 12:
     print("Access denied. Minimum age requirement not met.")

    elif registered == "no":
     print("You need to create an account to access.")
     
    elif vaccinated == "no":
     print("Access denied. Vaccination requirement not met.")

    else:
     print(f"Access authorized. Welcome, {name}!")
    authorized_count += 1


    # Continue option
    continue_option = input("Do you want to add another user account? (yes/no): ").strip().lower()


    if continue_option != "yes":
        break
    


# Final Report
print("\nFinal Report:")
for user in users:
    print(f"Name: {user['name']} | Age: {user['age']} | Registered: {user['registered']} | Vaccinated: {user['vaccinated']}")

print(f"\nTotal authorized users: {authorized_count}")


