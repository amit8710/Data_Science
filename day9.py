#Login register using username and password

# credentials = []

# def operation(method):
#     username =  input("Enter your username:")
#     password = input("Enter your password")
#     if method == 'login':
#         for i in credentials:
#             if username in i  and  i.get(username) == password:
#                 print("Login succesfully!!")
#                 break
#     else:
#         pass
#         print("Login failed...")
# while True:
#     print("Enter 1 for register")
#     print("Enter 2 for login")
#     print("3.Exits")
#     choice = input("Enter a number:")
    
#     match choice:
#         case '1':
#             operation('register')
#         case '2':
#             operation('login')
#         case '3':
#             print("Thank You......")
      
credentials = [] # empty list used to store all register users.

# register fuction
def register ():
    username = input("Enter Username:")
    password = input("Enter Password")
    
    credentials.append({username:password}) # saving data
    print("Resgister Succesfuly")      
    
    
def login():
    username = input("Enter Username:")
    password = input("Enter Password: ")
    
    found = False # falg variables (It indicates that it have not found the user)
    
    for i in credentials:  #Loop 
        if username in i and i.get(username) == password: #checking the username and password
            print("Login Successfully")
            found = True
            break
        
    if found == False:
        print("Invalid USername or Password")
while True:
    print("Enter 1 for register")
    print("Enter 2 for login")
    print("3.Exits")
    choice = input("Enter a number:")
    
    match choice:
        case '1':
             register()
        case '2':
            login()
        case '3':
            print("Thank You!!!")
            break
        
    
    