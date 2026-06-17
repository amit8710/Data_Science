# Operators in Python Examples
 #1. Arithmetic Operators
#Simple Calculator
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))

# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)
# print("Modulus:", num1 % num2)
# print("Exponentiation: ", num1 ** num2)
# print("Floor Division:", num1 // num2)


#Simple program to check total marks and percentage of a student in 5 subjects.

# Math = int(input("Enter marks in Math: "))
# Science = int(input("Enter marks in Science:"))
# English = int(input("Enter marks in English: "))
# Social_Studies = int(input("Enter marks in Social Studies: "))  
# GK = int(input("Enter marks in General Knowledge: "))

# Total_Marks = Math + Science + English + Social_Studies + GK

# print ("Total Marks: ", Total_Marks)
# print ("Percentage: ", (Total_Marks / 500) * 100)


#Assignment Operators Assignment

# num = 30

# print("Original value :", num)

# num += 5
# print("After += :", num)

# num -= 10
# print("After -= :", num)

# num  *= 2
# print("After *= :", num)

# num /= 5
# print("After /= :", num)

# num %= 3
# print("After %= :", num)    

# num **= 2   
# print("After **= :", num)

# num //= 2
# print("After //= :", num)


# Comparison Operators example

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))

# print("Equal to (==):", num1 == num2)
# print("Not equal to (!=):", num1 !=num2)
# print("Greater than (>):", num1 > num2)
# print("Less than (<):", num1 < num2)
# print("Greater than or equal to (>=):", num1 >= num2)
# print("Less than or equal to (<=):", num1 <= num2)


# Logical Operators example


# # Voting System

# age = int(input("Enter your age:"))

# if age >= 18 and age <=60:
#     print("You are eligible to vote.")
# elif age < 18:
#     print("You are a minor.")
    
    # Identity Operator
    
# a = [1,2,3]
# b = [1,2,3]
# print (a == b)
# print (a is b )


# Membership Operators example

name = ["Amit", "Ram", "Hari", "Sita"]
print ("Amit" in name)