print("Secure Access Control System")

users = []  # list of users

while True:

    # User's data
    name = input("Enter your name: ")
    age = int(input("Now, enter your age: "))

    registered = input("Are you registered? (yes/no): ").strip().lower()
    vaccinated = input("Are you vaccinated? (yes/no): ").strip().lower()

    # Creating user's dictionary
    new_user = {
        "name": name,
        "age": age,
        "registered": registered,
        "vaccinated": vaccinated
    }

    # Adding to the list
    users.append(new_user)

    # Access verification
    if age >= 12 and registered == "yes" and vaccinated == "yes":
        print(f"Access authorized. Welcome, {name}!")
    else:
        print(f"Access denied. We're sorry, {name}.")

    # Continue option
    continue_option = input("Do you want to add another user account? (yes/no): ").strip().lower()

    if continue_option != "yes":
        break

# Final Report
print("\nFinal Report:")
for user in users:
    print(user)



