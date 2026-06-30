# ATM Management System

credentials = [
    {
        "username": "amit",
        "password": "amit8710",
        "balance": 1000
    },
    {
        "username": "suman",
        "password": "12345",
        "balance": 500
    }
]


# Register Function
def register():
    username = input("Enter Username: ")

    # Check if username already exists
    for user in credentials:
        if user["username"] == username:
            print("Username already exists!")
            return

    password = input("Enter Password: ")

    new_user = {
        "username": username,
        "password": password,
        "balance": 0
    }

    credentials.append(new_user)
    print("Registration Successful!")


# Deposit Function
def deposit(current_user):
    amount = int(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    current_user["balance"] += amount

    print("Deposit Successful!")
    print("Current Balance:", current_user["balance"])


# Withdraw Function
def withdraw(current_user):
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if amount > current_user["balance"]:
        print("Insufficient Balance!")
    else:
        current_user["balance"] -= amount
        print("Withdrawal Successful!")

    print("Current Balance:", current_user["balance"])


# Check Balance Function
def check_balance(current_user):
    print("Available Balance:", current_user["balance"])


# ATM Menu
def atm_menu(current_user):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(current_user)

        elif choice == "2":
            deposit(current_user)

        elif choice == "3":
            withdraw(current_user)

        elif choice == "4":
            print("Logged Out Successfully!")
            break

        else:
            print("Invalid Choice!")


# Login Function
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    for user in credentials:
        if user["username"] == username and user["password"] == password:
            print("Login Successful!")
            atm_menu(user)
            return

    print("Invalid Username or Password!")


# Main Program
while True:
    print("\n===== ATM MANAGEMENT SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank you for using the ATM System!")
        break

    else:
        print("Invalid Choice. Please try again.")