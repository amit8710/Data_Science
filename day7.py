#List Comprehension => it is used to create lists using loops and conditions in a single line (loop , condition used garya ra list banuna)
#Writing the for loop or if else inside the list

# Syntax : [new_value for variable  in iterable]

# list1 = [1,2,3,4,5,6,7,8,9,0]

# # list2 = [i for i in range(101)] It will print all the number from 0-100

# list2 = [i for i in range(101) if i % 2 == 0] # it will print the even number.(simple if single condition)
# print(list2)

# list4 = ["even" if i % 2 ==0 else "Odd" for i in range(101)] # it is an example of if-else condition.
# print(list4)


#While Loop => While loop is used when we dont know the start and end value.
# while condition:
#       block of code

#Biggest thing to note:
#Infinite loop can be created from while loop
#break => when break encounters, it exit the loop

# for i in range(5):
#     if i == 3:
#         print("Break encounterd")
#         break
#     print(i)
# else:
#     print(i)

#Continue => when continue encounters, it skips the current iteration and move forward to the next interation.

# for i in range(5):
#     if i == 3:
#         print("Continue encounterd")
#         continue
#     print(i)
# complete this calcluater using while loop 

while True:

    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("Your calculator is closed.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero.")

    elif choice == "5":
        print("Result:", num1 % num2)

    else:
        print("Invalid choice")
        
        