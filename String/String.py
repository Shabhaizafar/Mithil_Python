# what is a String ?
# A String is a data structure in Python Programming that represents a sequence of characters.
# It is an immutable data type, meaning that once you have created a string, you cannot change it.
# Python String are used widely in many different applications,
#  such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.

# ----------------------------------------------------------------
# Single Quote
# mystr = 'Prem'

# Double Quote
# mystr = "Prem"

# print(mystr)
# print(type(mystr))

# length                 14                      
# mystr = "Prem Prajapati wertyujhgtyhbhjn"
# index  0123         13
# print(mystr)
# ----------------------------------------------------------------
# # immutable
# # mystr[0] = "Z"
# # print(mystr)

# # print(len(mystr))

# print(mystr[len(mystr)-1])

# -------------------------------------------------------------------
# Methods : 

mystr = "royal Technosoft pvt ltd"

# Print String 
print(mystr)

#1) mystr.capitalize()
# print(mystr.capitalize())

#2) mystr.count()
# print(mystr.count('o'))
# print(mystr.count('oy'))
print(mystr.count('o',3))  #3 index (for starting point)

print(mystr.count('o',3,13))  #13 index  (for Ending point)

print(mystr.count(''))  


