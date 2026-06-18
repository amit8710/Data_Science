# Data Types and ther methods

# 1. int => Wholenumber data type
# 2. float => Decimal number data type    
# 3. str => Wrapped with single or double quotes
# 4. bool => True or False

#Mutable and Immutable data types

# Mutable data type => Can be changed after creation.
# Immutable data type => Cannot be changed after creation. If we need to change it , python creats a new object.
# Group data type => Those datatypes which consitts of multiple elements.(Example: list, tuple, set, dictionary, string)

#List
# List is a mutabble datatype
# List is wrapped with square brackets []
# List can have duplicate values

#List example 
# List1 = [1, "Amit",23, False]
# print(List1)

#Nested List => List inside a list

# list2 = ["Amit", 1, [1, 2, 3], "Amit", False]
# print(list2)

#Tuple => Tuple is an immutable data type
# Tuple is wrapped with parentheses ()
# Tuple can have duplicate values and it is odered datatype

# Tuple example

# tuple1 = (1, "Amit", 23, False)
# print(tuple1)

#  Nested Tuple => Tuple inside a tuple
# tuple2 = ("Amit", 1, (1, 2, 3), "Amit", False)
# print(tuple2)


# Set => Set is a mutable data type
# Set is wrapped with curly braces {}   
# Set cannot have duplicate values and it is unordered data type
# Set example

# set1 = {1, "Amit", "Basnet", False,1,2,3,4,5}
# print(set1)

# Dictionary => Dictionary is a mutable data type
# Dictionary is wrapped with curly braces {}
# Dictionary contains key and value pair
# key = Always string data type
# value = Can be any data type

# Dictionary example

dict1 = {
    "name": "Amit", 
    "age":23, 
    "is_student": False
    }
print(dict1)
