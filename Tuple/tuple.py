"""
Python Tuple is a collection of objects separated by commas. 
In some ways, a tuple is similar to a Python list in terms of indexing, nested objects, and repetition but the main difference between both is : 
    - Python tuple is immutable, unlike the Python list which is mutable.
"""

# Empty Tuple : 
# myTuple = ()
# print(myTuple,type(myTuple))

# myTuple = (1,2,3,4,5)
# print(myTuple)

# myTuple = ("Z","A","F","A","R")
# print(myTuple)

# myTuple = (True,False)
# print(myTuple)

# myTuple = (10j,11j)
# print(myTuple)

#length      1    2    3 45   6     7 
# myTuple = (True,False,1,1,2,"Zafar",11j)
# #index      0     1   2 3 4    5    6
# #          -7                -2    -1
# print(myTuple)

# print(len(myTuple))
# print(myTuple[6])
# print(myTuple[len(myTuple)-1])

# print(myTuple[-8])

# myTuple = (1,2,3,4,5,6,1,1,1,1)

# print(myTuple.count("1"))
# print(myTuple.index(1))
# print(myTuple.index(1,2))
# print(myTuple.index(1,2,7))

# myTuple[0] = 12
# print(myTuple)


# for i in range(0,len(myTuple)):
#     print(myTuple[i],i)

# print(len(myTuple))


#Write a Python program to add an item to a tuple.
myTuple = (1,"1")
# myList = list(myTuple)
myDict = dict(myTuple)
print(myDict)


# myList.append(10)
# print(tuple(myList))

# myList.remove(1)
# print(myList)

#Write a Python program to convert a tuple to a string.
# myStr = ''
# for i in myTuple: 
#     myStr+=str(i) 
# print(myStr)

