# Function is a block of code which only runs when it is called, it can return data as result, it helps avoding code repetiton.
#syntax
# def function_name():
    # print()
# function_name :function call

# (return) statement is used to return the value return = print same ho function ma 
#return  example
# def greating():
#     return "Namaste"
# # message = greating()
# print(greating())

# (pass) statement is used to create afunction placeholderr without any code.
# example

# def my_function():
#     pass

#parameters : is the variablee listed inside the (parameter) in function definitaion.
#argument: is the actual value that is sent to the fucntion when it is called.
# A function expects 2 argument and gets 2 arguments

#Common example
# def my_function(name): #name is parameter
#     print("Hello",name)
# my_function("Amit") # amit is argument

# Type of funcion 
# 1. Built-in Function :- function already availablee in Python.
# 2. User DEfined Function;- function which is created by the programmer.

# Global Variables: which is declared outside function and can be used throughout the program.

# example
balance = 10000 # global variables
# def display():
#      print("Your total balance is", balance)
# display()

#Local Variable is declared inside the function and can only be used that function.
# Example

# def dispaly():
#     name = "Amit" #local variables
#     print("Hello",name)
    
# dispaly()


# Addition Function

# def add(num1, num2):
#     print("Total Sum is", num1 +num2)
# add(5,10)

# Employee Salary System.

Company_Name = "HimalyanPeakTreks"

def my_function():
    name = "Amit"
    salary = 150000
    bonus = (10 / 100) * salary
    total = salary + bonus
    print("Company:",Company_Name)
    print("Employee Name:",name)
    print("Basic Salary:",salary)
    print("Bonous:",bonus)
    print("Total Salary:",total)
    
my_function()
    
    
    
