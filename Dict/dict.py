# What is Dictionary : 
# Dictionaries are a useful data structure for storing data in Python because they are capable of imitating real-world data arrangements where a certain value exists for a given key.

# The data is stored as key-value pairs using a Python dictionary.

# This data structure is mutable
# The components of dictionary were made using keys and values.
# Keys must only have one component.
# Values can be of any type, including integer, list, and tuple.

# A dictionary is, in other words, a group of key-value pairs, where the values can be any Python object. 
# The keys, in contrast, are immutable Python objects, such as strings, tuples, or numbers.
#  Dictionary entries are ordered as of Python version 3.7. In Python 3.6 and before, dictionaries are generally unordered.

# Empty Dict 
# mydict = {}

# print(mydict)
# print(type(mydict))


# mydict = {
#   #  key        value       =   property   
#     "fname" : "Raj",
#     "lname" : "Patel",
#     "age"   :  12
# }

# print(mydict)
# print(type(mydict))


# How to Access Key's Value.
# print(mydict.get('fname'))    #Raj
# print(mydict.get())  #error
# print(mydict.get('fname','lname'))  # Always print First 
# print(mydict.get('gender'))  #None
# print(mydict["fname"])     #Raj


# How to Modify Key's Value 
# mydict['lname'] = "Shah"
# print(mydict)


# How to Add new Key-value pair
# mydict['Gender'] = "Male"
# print(mydict)

# mydict['gender'] = "Male"
# print(mydict)


# mydict = {
#     "fname" : "Raj",
#     "lname" : "Patel",
#     "age"   :  12
# }

# Print Key's name
# for i in mydict :
#     print(i)


# Print Key's name with Values
# for i in mydict :
#     print(i,mydict.get(i))

# for i in mydict :
#     print(i,mydict[i])


mydict = {
    "fname" : "Raj",
    "lname" : "Patel",
    "age"   :  12
}

# Clear dict : 
# mydict.clear()
# print(mydict).


# How to Create a Shallow Copy : 
# shallow_copy = mydict.copy()
# print(shallow_copy)
# print(id(shallow_copy))
# print(id(mydict))


# c = mydict.fromkeys(iterable="123",value="ZA")
# print(c)
# c = mydict.fromkeys(mydict)
# print(id(c))
# print(id(mydict))


# v = mydict.items()
# print(type(v))
# for i in v : 
#     print(i)

# v = mydict.keys()
# print(v)

# v = mydict.values()
# print(v)