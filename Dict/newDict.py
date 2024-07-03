# dict : 
# keys and values pairs    -----> property
# methods (function)
# unordered dict 
# mutable 
# repeatation not allowed
# syntax  : {}


# mydict = {}  

#1) print mydict 
# print(mydict)   # {}

#2) type of mydict
# print(type(mydict)) # <class 'dict'>

mydict = {
    "lname" : "Patel",
    "fname" : "Raj"
}

# 3) how to Access Any single property value
# print(mydict["fname"])

# 4) how to modify/update any single property value
# mydict["lname"] = "Shah"
# print(mydict)

# 5) how to Add new property 
# mydict["Age"] = None
# print(mydict)


# 6) how to delete property
# del mydict["lname"]
# print(mydict)

# 7) how to delete mydict 
# del mydict
# print(mydict)


# Methods  

# 1)
# mydict.clear()
# print(mydict)

# 2)
# dict2 = mydict.copy()
# print(dict2)

# 3) how to Access Any single property value
# print(mydict.get("fname"))

# 4)
# ans =mydict.items()
# print(ans)


# 5)
# keys = mydict.keys()
# print(keys)

# 6) 
# values =mydict.values()
# print(values)


# 7)
# removalproperty= mydict.pop('fname')
# print(mydict)
# print(removalproperty)

# 8)
# news = mydict.popitem()
# print(news)


# 9 )  how to modify/update any single property value
# mydict.update({"fname":"Ajay"})

# how to add new property
# mydict.update({"mname":"Rajeshbhai"})
# print(mydict)

# 10)
# mydict.setdefault("fname",12)   # never change Value if Already Exist else add new property 
# print(mydict)

# 11)
#string 
# var = mydict.fromkeys("Zafar","123456")
# var = mydict.fromkeys(mydict)
# var = mydict.fromkeys([1,2,3,4],"AZ")
# var = mydict.fromkeys((1,2,3,4),"AZ")
# print(var)




#############################################
# Difference between function and method
# function 
# def All():
#     pass
# All()

# def All():
#     print("H")


# mydict = {
#     "ABC" : All
# }

# mydict["ABC"]()
#//////////////////////////////////////////////
nested_dict = {
    'person1': {
        'name': 'Alice',
        'age': 30,
        'contacts': {
            'email': 'alice@example.com',
            'phone': '123-456-7890'
        },
        'address': {
            'city': 'New York',
            'zipcode': '10001',
            'country': 'USA'
        },
        'skills': {'Python': True, 'JavaScript': True, 'SQL': True}
    },
    'person2': {
        'name': 'Bob',
        'age': 25,
        'contacts': {
            'email': 'bob@example.com',
            'phone': '987-654-3210'
        },
        'address': {
            'city': 'San Francisco',
            'zipcode': '94102',
            'country': 'USA'
        },
        'skills': {'Java': True, 'C++': True, 'HTML/CSS': True}
    }
}
# 1) print Full dict.
# print(nested_dict)

# 2) print all property key's of main dict
n= "person1"
for i in nested_dict:
    if(i==n):
        print(i)
        for j in nested_dict[i] :
            if(type(nested_dict[i][j])==dict):
                for k in nested_dict[i][j]:
                    print("\t\t",k,":",nested_dict[i][j][k])
            else:
                print("\t",j,":",nested_dict[i][j])
        print("\n")
