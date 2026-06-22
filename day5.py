# Match case
#The vaiable is matched with the values in case
#  match syntax
# variable = 'value'
# match variable:
#     case "Value":
#         #code to be executed
#         pass
#     case "value":
#         #code to be executed
#         pass
#     case "Value3:":
#         #code to be executed
#         pass
#     case _:
#         print("This is defalut case.")


# Calculater using match case

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))

# choice = input("Enter 1 for add , 2 for sub:")

# match choice:
#     case '1':
#         print("Add=", num1 + num2)
#     case '2':
#         print("Sub:", num1 - num2)
#     case _:
#         print("Invalied choice.")


#user login using match example

# username = []
# choice = input("Enter 1 for register , and 2 for login:")
# user = input("Enter your username:")

# match choice:
#     case '1':
#         username.append(user)
#         print(username)
#     case '2':
#         if user in username:
#             print("Login succesfull")
            
#         else:
#             print("Invalied USername")
            
#     case _:
#         print("Invailed choise")

#Loops => it are used when we need to execute same block of code repeatedly.
#DRY => Dont Repeat Yourself

#For Loop => For loop is used when we know the start and stop condition.
#syntax
# interator is  a variable that stores the value of current loop, it is also a group of data type
# for interator in iterable: 
#     code to be executed:


#While loop => While loop is used when we dont know the strat and stop conditon.


        
