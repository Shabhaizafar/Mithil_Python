# 1. Write a  Python program to create a set.
# s1 = {10,12,14,16,18,1,4,2,7}
# print(s1)
# s2 = set([1,2,3])
# print(s2)
#--------------------------------------

# 2. Write a  Python program to iterate over sets.
# s1 = {10,12,14,16,18,1,4,2,7}
# for i in s1:
#     print(i,end=',')

# List
# l1 = [1,2,3,4]
# for i in range(0,len(l1)):
#     if(i==len(l1)-1):
#         print(l1[i])
#     else:
#         print(l1[i],end=',')

#--------------------------------------

# 3. Write a Python program to add member(s) to a set.
# s1 = {10,12,14,16,18,1,4,2,7}
# print(s1)
# while(1):
#     i = input("Do you went to Add new Value (yes/no): ").lower()
#     if(i=='yes'):
#         v = int(input("Enter Value :"))
#         s1.add(v)
#     else:
#         break

# print(s1)
    

#--------------------------------------

# 4. Write a Python program to remove item(s) from a given set.
# s1 = {10,12,14,16,18,1,4,2,7}
# print(s1)
# while(1):
#     i = input("Do you went to remove Value (yes/no): ").lower()
#     if(i=='yes'):
#         v = int(input("Enter Value :"))
#         s1.remove(v)
#     else:
#         break

# print(s1)
    

#--------------------------------------

# 5. Write a Python program to remove an item from a set if it is present in the set.
# s1 = {10,12,14,16,18,1,4,2,7}
# print(s1)
# while(1):
#     i = input("Do you went to remove Value if Exist ? (yes/no): ").lower()
#     if(i=='yes'):
#         v = int(input("Enter Value :"))
#         s1.discard(v)
#     else:
#         break

# print(s1)

#--------------------------------------

# 6. Write a Python program to create an intersection of sets.

#--------------------------------------

# 7. Write a Python program to create a union of sets.

#--------------------------------------

# 8. Write a Python program to create set difference.

#--------------------------------------

# 9. Write a Python program to create a symmetric difference.

#--------------------------------------

# 10. Write a  Python program to check if a set is a subset of another set.

#--------------------------------------

# 11. Write a  Python program to create a shallow copy of sets.

# Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.
# s1 = {1,2,3}
# s2 = s1.copy()

#--------------------------------------

# 12. Write a Python program to remove all elements from a given set.

#--------------------------------------



#--------------------------------------

# 14. Write a Python program to find the maximum and minimum values in a set.

#--------------------------------------

# 15. Write a  Python program to find the length of a set.

#--------------------------------------

# 16. Write a  Python program to check if a given value is present in a set or not.
# s1 = {1,2,3}
# print(1 in s1)

#--------------------------------------

# 17. Write a Python program to check if two given sets have no elements in common.

#--------------------------------------

# 18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.


#--------------------------------------

# 19. Write a Python program to find elements in a given set that are not in another set.

#--------------------------------------

# 20. Write a Python program to remove the intersection of a second set with a first set.   difference_update()

#--------------------------------------

# 21. Write a  Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use  Python set data type.

# for i in s1:
#     for j in l1:

#--------------------------------------


# a = 2
# b = 3

# print(f'a + b = {a + b = }')
# a = 2
# b = 3

# print(f'{a + b =}')
# a = 10000000

# print("-------------Royal---------")
# print(f'{a:_>20}:')
# print(f'{a:-<20}:')
# print(f'{a:.^20}:')
# print(f'{a:_}')
# print(f'{a:,}')
# print(f'{a:_}')




#--------------------------------------

# 23. Write a Python program to find the longest common prefix of all strings. Use the Python set.
l1 = ["royal","loyal","koya"]
mylist2 = []
final = []
for i in l1:
    myList = []
    for j in range(0,len(i)):
        myList3 =[]
        for k in range (0,len(i)+1):
            if (i[j:k] == ''):
                continue
            else:
                myList.append(i[j:k])
        myList3.append(myList)
    mylist2.append(myList)


# print(mylist2)
for j in mylist2[0]:
    
    
            

# maxprefix = final[0]
# # print(maxprefix)
# for i in final:
#     if(len(maxprefix)<len(i)):
#         temp = maxprefix
#         maxprefix = i
#         i = temp 


# print(maxprefix)





#--------------------------------------

# 24. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

#--------------------------------------

# 25. Given two sets of numbers, write a  Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the  Python set.

#--------------------------------------

# 26. Write a Python program to find all the anagrams and group them together from a given list of strings. Use the Python data type.

#--------------------------------------

# 27. Write a Python program to find all the anagrams in a given list of strings and then group them together. Use the Python data type.

#--------------------------------------

# 28. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

#--------------------------------------

# 29. Write a  Python program to find the third largest number from a given list of numbers.Use the Python set data type.

#--------------------------------------

# 30. Write a  Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.






# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# print(s1)
# print(s2)

# # s3 = s1.symmetric_difference(s2)
# # print(s3)
# s1.symmetric_difference_update(s2)
# print(s1)

# s4 = s1.difference(s2)
# print(s4)

