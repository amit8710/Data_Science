#File Handling
#How to handle files from python code



#File handling flow
#1. Open the file => file = open('file path')
#2. Perform operation
#3.Close the file
#During opening the file , we need to add the node of opening the file
# read mode => r
#write mode => w
# append mode => a

#IF a file is opened in read mode, wwe could only read content from a file
#content = file.read()

#We could only write string and JSON in a file
# and while reading the file , it return in string or JSON

# If a file is opened in write mode but file doesnot exits, python creates a new file, if there exist a file it will open that file
#if file is open in write mode, it remove the previous content 

#Write mode
# file = open('abc.txt','w') #abc.txt is file, 'w' is a mode (read,write)
# file.write("Amit Basnet") #operation
# file.close() # close

#Read mode
#If file is open in read mode, but file doesnot exits then in through error.

# file = open('abc.txt','r') #abc.txt is file, 'w' is a mode (read,write)
# content = file.read()
# file.close

# print(content)

#Append mode
# If a file is opened in append mode but file doesnot exits, python creates a new file
# If a files is open in append mode, it preserves the previous content and 
# add the new content 


# file = open('abc.txt','a') #abc.txt is file, 'w' is a mode (read,write)
# file.write("AMit basnet")
# file.close


#What is difference between the append and write and the conditon in which it is used ????
import json
# Json have 2 methods
# json.dumps(dictionary) => Convert dictionary to json
# Json.loads(json) => Convert json to dictionary

def operation(method):
    
    username = input("Enter your username: ")
    password = input("Enter Your Password: ")
    
    if method == 'register':
        dict_cred = {username:password}
        json_cred = json.dumps(dict_cred)
        file = open("credentials.txt", 'a')
        file.write(dict_cred)
        file.close()
    else:
        file = open("credentials.txt", 'r')
        content = file.read()
        file.close()
        print(content)

while True:
        print("1. for Register")
        print("2. For Login")
        print("3. Exits")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            operation('register')

        elif choice == "2":
            operation('login')

        elif choice == "3":
            print("Logged Out Successfully!")
            break

        else:
            print("Invalid Choice!")


