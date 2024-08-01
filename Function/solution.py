'''
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
Sample Output:
25
48
'''
# ans = lambda a : a+15
# print(ans(10))


# ans = lambda a,b : f'{a+15} {b+15}'
# print(ans(10,30))

# for i in [10,20,30,40,50]:
#     ans = lambda a : a+15
#     print(ans(i))
#----------------------------------------------------------
'''
2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
'''
# import random  
# n = int(input("Enter the Value of N : "))
# ans = lambda a : a * random.randint(1,10)

# print(ans(n))

#----------------------------------------------------------
'''
3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
# l1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print(l1)
# print(sorted(l1,key= lambda a : a[1]))

#----------------------------------------------------------
'''
4. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''
# l2 =[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


# print(l2)
# print(sorted(l2,key= lambda a : a['color'][0]))

#----------------------------------------------------------
# 5. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
# #----------------------------------------------------------

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
#--------------------------------------------------
# 7. Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output:
# True
# False
# str1 = "sdfg"
# str1.startswith('df')
#----------------------------------------------------------

# 8. Write a Python program to extract year, month, date and time using Lambda.
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# import datetime as dt

# today = dt.datetime.today()
# l1 = '-'.join(str(today).split(' ')).split('-')

# var = lambda a : print(a)
# [var(item) for item in l1]

#---------------------------------------------------
# 10. Write a Python program to create Fibonacci series up to n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]

# li = []
# z = 0
# a=0
# b=1
# c = 0
# n=int(input("Enter no:"))
# def fibonaci(a,b,c,n,z):
#     if (z == n):
#         return li

#     c=a+b
#     # li.append(a)
#     var = lambda x : x.append(a)
#     var(li)
#     a=b
#     b=c     
#     z+=1    

#     return fibonaci(a,b,c,n,z)
# print(fibonaci(a,b,c,n,z))


# 13. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

# l1 = [1, 2, 3, 5, 7, 8, 9, 10]

# even = list(filter(lambda a : a%2==0,l1))

# print("Length of Even : ",len(even))
# print("Length of Odd : ",len(l1)-len(even))


#-------------------------------------------------

# 19. Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
# Orginal list of strings:
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['bcda', 'cbda', 'adcb']

l1 = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']

temp = []
s1 = 'abcd'
for i in l1:
    flag = 1
    for j in s1:
        var = lambda a,b : a not in b
        if(var(j,i)):
            flag = 0
            break
    if(flag==1):
        temp.append(i)
print(temp)