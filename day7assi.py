# List Comprershension example
# list1 = [1,2,3,4,5,6,7,8,9,0]
# print(list1)
# list2 = [i**2 for i in range(1,11)]
# print(list2)

# list3 = [i for i in range(1,50,2)] #Using list comprehension print all odd numbers from 1-50.
# print(list3)

# list4 = ['positive' for i in range(1,6)]# printing 5 times positive
# print(list4)

# list5 = ["Even" if i % 2 == 0 else "Odd" for i in range(1,21)]
# print(list5)

# While loop example
# total = 0

# while True:
#     num = int(input("Enter a number:"))
    
#     if num == 0:
#         break
#     total += num
    
#     print("Sum of all numbers entered:",total)


#Create an ATM Program:

balance = 10000

while True:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your total balance is ",balance)
    elif choice == "2":
        amount = float(input("Enter a amount: "))
        if amount > 0:
            balance += amount
            print("Deposit successfuly!!!1")
            print("Your new Total balane is ",balance)
    elif choice == "3":
        amount = float(input("Enter a amount: "))
        if amount <= 0:
            print("Error")
        elif amount > balance:
            print("Insufficent balance!!")
        else:
            balance -= amount
            print("Amount withdraw ")
            print("Your remaing balance is ", balance)
    elif choice == "4":
        print("Thank you!!")
        break
    else:
        print("Invalid Choice! Please try again.")
