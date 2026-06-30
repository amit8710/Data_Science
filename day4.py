# Condtitional Statements
# Those statements that is executed according to the condition.

# If Else (Syntax): used ot check 2 condtion 
# if conditon: "Conditionis not deefined"
#     code to be exeecuted is True
# else:
#     code to be executed if conditon is false  - 

#Example
# percentage = float(input("Enter your %: "))
# if percentage > 40:
#     print("Pass")
# else:
#     print("Fail")
    
# simpel if => it conatian only if, used for only one condition.

# age = int(input("Enter your age: "))
# if age >  25:
#     print("Adult")
    
# Elif Ladder => Used when you have multiple conditions(Elif).

# percentage = float(input("Enter your %: "))
# if percentage >= 90:
#     print("A+")
# elif percentage >= 80 and percentage < 90:
#     print("A")
# elif percentage >= 70 and percentage < 80:
#     print("B+")
# else:
#     print("Fail")
    
#Nested IF Else : it conatain if else inside ifelse
#Example
num1 = int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))
num3 = int(input("Enter a num3: "))
if (num1 > num2 ):
    if (num1 > num3):
        print("The greated is :", num1)
    else:
        print("The greates is :", num3)
else:
    if num2 > num3:
        print("The greates is :", num2)
    else:
        print("The greates is:", num3)