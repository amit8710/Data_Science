# credintials = []
# # add function
# def add():
#     print("Student Detals...")
#     name = input("FullName:")
#     age = input("Age: ")
#     faculty = input("FacultyName:")
    
#     credintials.append({
#         "name": name,
#         "age" : age,
#         "faculty": faculty        
#         })
#     print("Added sucessfully")
    
# #Search function

# def search():
#     name = input("Enter Student name:")
    
#     found = False
    
#     for student in credintials:
#         if student["name"] == name:
#             print("Name:",student["name"])
#             print("Age: ",student["age"])
#             print("Faculty: ",student["faculty"])
            
#             found = True
#             break
#     if  found == False:
#         print("Student not found")        
    
# def display():
#      for student in credintials:
#          print(student)
#          break
    
    
# while True:
#     print("1.Add Student")
#     print("2.Search Student")
#     print("3.Display Students")
#     print("4.Exit")
    
#     choice = input("Enter Your Choice: ")
    
#     match choice :
#         case '1' :
#             add()
#         case '2' :
#             search()
#         case '3':
#             display()
#         case '4':
#             print("Thank You!!")
#             break
            
            
# To-Do App

task = []

def add():
    tasks = input("Enter Your Tasks: ")
    task.append({tasks})
    print("Added Succesfully")
    
def view():
    # for i in task:
    #     print(task)
    #     break
    if len(task) == 0:
        print("No task available.")
    else:
        for i in range(len(task)):
            print(f"{i+1}. {task[i]}")
            
def delete():
    if len(task) == 0:
        print("No tasks to delete.")
    else:
        view()
        index = int(input("Enter task number to delete: "))
        task.pop(index - 1)
        print("Task deleted successfully!")
    
while True:
    print("1.Add Task: ")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")
    
    choice = input("Enter our Choice: ")
    
    match choice:
        case '1':
            add()
        case '2':
            view()
        case '3':
            delete()
        case '4':
            print("Thank You!!")
            break
        case _:
            print("Invalid choice")