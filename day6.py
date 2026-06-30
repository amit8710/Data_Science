# Loops
# Dictionaries => are used to store value in key:value pairs.
# To print aparticular data add the key inside ["key"]
# len(thisdict) => print the number of items in the dictionary.
# dict(...) => constructor is used to make dictionary.
# get(.) methods => which will givee the same result
# del => keyword is used to delete the dict and clear() method is used to empties the dict
#Example
# thisdict = {
#     "brand": "TATA",
#     "model": "SumoGold",
#     "Year": 2013
# }
# print(thisdict["brand"]) 
# print(thisdict.get("model")) => get(.) methods
# print(thisdict.keys()) => keys() method which will print all the keys
# print(thisdict.values()) => values() method is used to print all the value from the dict
# print(thisdict.items()) => items() method is used to print all the keys and valuees from the dict
# thisdict.update({"Year": 2018}) update() method is used to update the values.
# del thisdict["model"]
# print(thisdict)


#range ()=> It generates the sequensce of numbers
# Treat range() as aiterable
# range(start,stop,step),  if you only give 1 value, that will be for stop ,start will be from 0 automatically.
# stop value is always exclusive(include na hunya), start value is always inclusive(include hunya)
 
# for i in range(6):
#     print(i)
    
# In range (), if you give 2 values, first will be for start,2nd will be stop

# for i in range(5,10):
#     print(i)

#In range (), if you have 3 value, first will be start, 2nd will be for stop,3rd will be step it will increase according to it .

# for i in range(5,20,2):
#     print(i)

#What if step is negative?
 # We will move towared back, and start should always greater than stop
 # if step is negative, start > stop

# for i in range(5,1,-2):
#     print(i)

#List Indexing and Slicing
#Indexing => Accessing only one element from list acccording to the index
#Index always starts from 0
#group_data_type_name[index_number]
# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(list1[8])
#Slicing => Accessing the sequense of element from ordered group data type according to the index.
# Slicing generate the subset of group data type through index
#grou_data_type_name[start_index:stop_index:stop]
#start_index is inclusive, stop_index is exclusive.
#Here step value is always 1.If you didnt give start and end then it will print the whole list


# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(list1[5,7]) # answer => [6,7]
# print(list1[-1]) #-1 is the last element in the list 
# print(list1[-1:-5:-1]) #ans => [10, 9, 8, 7]


