print("===== SIMPLE CALCULATOR ===")

while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Exit")

    try:
        choice = int(input("\nEnter a choice(1-8):"))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 8.")
        continue

    if choice == 8:
        print("Thank you for using the calculator!!")
        break

    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
    except ValueError:
        print("Invalid number input!")
        continue

    if choice == 1 :
        result = num1 + num2
        print("Result:",result)

    elif choice == 2:
        result = num1 - num2
        print("Result:",result)
        
    elif choice == 3:
        result = num1 * num2
        print("Result:",result)
        
    elif choice == 4:
        if num2 == 0:
            print("Error!! Division by zero")
        else:
            result = num1 / num2
            print("Result:", result)
        
    elif choice == 5:
        if num2 == 0:
            print("Error!! Modulus by zero")
        else:
            result = num1 % num2
            print("Result:",result)
            
    elif choice == 6:
        result = num1 ** num2
        print("Result:",result)

    elif choice == 7:
        if num2 == 0:
            print("Error!!! Floor division by zero")
        else:
            result = num1 // num2
            print("Result:", result)
            
    else:
        print("Invalid choice! Please select between 1 and 8.")