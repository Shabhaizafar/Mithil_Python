"""
1. Check if a Given Key Already Exists in Dictionary
-> If you have learned about Python dictionaries, you will know that you can check if a given key exists or not in multiple ways. 

D1 = {'first_name' : 'Krutarth', 'age' : 22, 'height' : 5.0 , 'job' : 'Developer', 'company': 'Google'}
"""
# D1 = {
#     'first_name' : 'Krutarth', 
#     'age' : 22, 
#     'height' : 5.0 , 
#     'job' : 'Developer', 
#     'company': 'Google'
# }
# finder = input("Enter key name which you have find given dict : ")

# 1) 
# if(D1.get(finder)):
#     print(f'{finder} Exist in a Given Dict.')
# else:
#     print(f"'{finder}' doesn't Exist in a Given Dict.")

# 2)
# for i in D1: 
#     if i is finder : 
#         print(f'{finder} Exist in a Given Dict.')


# 3)      
# if finder in D1.keys():
#     print(f'{finder} Exist in a Given Dict.')
# else:
#     print(f"'{finder}' Doesn't Exist in a Given Dict.")

#-----------------------------------------------------------------#
'''
2. Handle Missing Keys in Dictionary
->Often, you will not know all the keys present in the dictionary and you might end up with a typing error which may lead to runtime error due to missing keys in the dictionary.

D1 = {'first_name' : 'Zafar', 'age' : 21, 'height' : 4.8 , 'job' : 'Engineer', 'company': 'Microsoft'}

'''
# D1 = {
#         'first_name' : 'Zafar', 
#         'age' : 21, 
#         'height' : 4.8 ,
#         'job' : 'Engineer', 
#         'company': 'Microsoft'
#     }
# finder = input("Enter key name which you have find given dict : ")


# D1.setdefault(finder)
# print(D1)

#---------------------------------------------------------#
"""
3. Extract Unique Values in a Given Dictionary
-> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

D1 = {	'list1': [4, 7, 10, 20], 
      	'list2': [7, 16, 9, 10], 
     	'list3': [13, 10, 4, 8], 
     	'list4': [7, 20, 6, 11]
         }
Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]
"""
# D1 = {	'list1': [4, 7, 10, 20], 
#       	'list2': [7, 16, 9, 10], 
#      	'list3': [13, 10, 4, 8], 
#      	'list4': [7, 20, 6, 11]
#         }
# finaloutput = []
# for i in D1:
#     finaloutput.extend(D1[i])

# print(list(set(finaloutput)))


#-------------------------------------------------------------#
# 4. Print the Sum of Key Value Pairs in a Given Dictionary
# -> You need to create a list which has the sum of key-value pairs of a given dictionary. 

# D1 = {2: 8, 5: 20, 3: 15}

# HINT-> This can be done using a for loop and append() function. 

#-----------------------------------------------------------#
# 5. Replace Dictionary Values From Other Dictionary
# -> Let’s say you are given two dictionaries. You need to write a python program that will replace the values in the first dictionary with the values from the second dictionary if the key is present in the second dictionary. 

# # initializing D1 - first dictionary
# D1 = {'first_name' : 'Rutvi', 'age' : 21, 'height' : 4.0 , 'job' : 'Software Engineer', 'company': 'Uber'}
 
# # initializing D2 - - first dictionary
# D2 = {'age' : 35, 'job' : 'senior data analyst'}
# D1 = {
#     'first_name' : 'Rutvi',
#     'age' : 21, 
#     'height' : 4.0 , 
#     'job' : 'Software Engineer', 
#     'company': 'Uber'
#     }

# D2 = {
#     'age' : 35, 
#     'job' : 'senior data analyst',
#     'Gender' : "Female"
#     }

# for i in D1:
#     if i in D2 : 
#         D1[i] = D2[i]
# print(D1)

#-----------------------------------------------------------#
# 6. Update or Change the Keys in a Given Dictionary
# -> try these 2 ways
# i)  Using assignment operator
# ii) Using pop() method

# D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

# D1 = {
#     'Niraj': 23, 
#     'Krutarth': 29, 
#     'Pushpa': 33, 
#     'Sures': 40
# }
# ii) Using pop() method

# v = D1.pop('Sures')
# D1['Suresh'] = v 
# print(D1)

#-------------------------------------------------------------#
# 7. Delete a List of Keys in a Given Dictionary 
# D1 = {
#     'Niraj': 23, 
#     'Krutarth': 29, 
#     'Pushpa': 33, 
#     'Sures': 40
# }
# li = ["Niraj","Sures"]
# for i in li:
#     if i in D1:
#         del D1[i]
#         # D1.pop(i)

# print(D1)

#------------------------------------------------------#

# 8. Count the Frequency of List Items Using a Dictionary
# -> You can solve this in many ways. Any ideas? Well, you can just use looping constructs or use the list() count method or you can start with an empty dictionary and use the dict.get() method. Probably many other ways!

# D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}
D1 = {
    'Niraj': 23, 
    'Krutarth': 29, 
    'Pushpa': 33, 
    'Sures': 40
}