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
-> Dictionary is a collection in python, where the data is stored in the form of a key-value pair, that is, it maps key to its value. Often, you will not know all the keys present in the dictionary and you might end up with a typing error which may lead to runtime error due to missing keys in the dictionary.

D1 = {'first_name' : 'Zafar', 'age' : 21, 'height' : 4.8 , 'job' : 'Engineer', 'company': 'Microsoft'}

'''
D1 = {
        'first_name' : 'Zafar', 
        'age' : 21, 
        'height' : 4.8 ,
        'job' : 'Engineer', 
        'company': 'Microsoft'
    }
finder = input("Enter key name which you have find given dict : ")


D1.setdefault(finder)
print(D1)