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
5. Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
#----------------------------------------------------------

6. Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]