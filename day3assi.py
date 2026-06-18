# Creating lists

# fruits = ["Apple", "Bannana", "Mango", "Grapes"]
# fruits.append("Orange")
# fruits.remove("Bannana")
# print("First Fruits:",fruits[0])
# print("Last Fruits:", fruits[-1])
# print(fruits)
# print("Total List:",len(fruits))

#Create a nested list and print ....

# marks = [80, 90, [70, 85, 95]]
# print(marks)
# print(marks[2][0])
# print(marks[2][1])
# print(marks[2][-1])

# # Create tuple

# languages = ("Python", "Java", "C++", "Python")
# print("First Language:",languages[0])
# print("Last Language:",languages[-1])
# print(languages.count("Python"))
# print(languages.index("Java"))

# Create 2 sets

# A = {1,2,3,4}
# B ={3,4,5,6}

# print(A.union(B))
# print(A.intersection(B))
# print(A.difference(B))

#Nested Dictionry

# student ={
#     "name": "Amit",
#     "marks":{
#         "Python":90,
#         "Java":85,
#         "react":88
#     }
# }
# print(student["marks"]["Python"])
# print(student["marks"]["Java"])
# print(student["marks"]["react"])

#Day 3 Assignment 

username = ["amit8710", "ram4456", "ronaldo7"]
name = input("Enter your username: ")
if name in username:
    print("Yes username is available")
else:
    print("No!! Register first.")