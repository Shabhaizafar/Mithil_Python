# lamda arguments : expression

# wap to print square of Given number using lamda expression.

# ans = lambda a : print(a*a)
# ans(12)

# /////////////////////////////////////////////////////////////
# Create a lambda function that adds two numbers.
# x = int(input("Enter the Value of N1 :"))
# y= int(input("Enter the Value of N2 :"))
# var = lambda a,b : print(a+b)

# var(x,y)
# /////////////////////////////////////////////////////////////
# Write a lambda function to check if a given number is even or odd.

# y= int(input("Enter the Value of N2 :"))
# var = lambda a : a%2==0

# print("Given Number is Even ?",var(y))
# /////////////////////////////////////////////////////////////

# Use a lambda function to square a list of numbers.
# l1 = [1,2,3,4,5]
# var = []
# for i in l1 : 
#     v = lambda i : pow(i,2)
#     var.append(v(i))

# print(var)


# /////////////////////////////////////////////////////////////

# Sort a list of tuples based on the second element using a lambda function.
# l1 = [(1, 2), (3, 5), (-1, 10), (0, 0), (7, 3), (-5, 2), (8, 1), (4, 9), (6, -2), (2, 6)]
# print(sorted(l1, key= lambda a : a[1] ))


# /////////////////////////////////////////////////////////////
# Filter a list of integers to get only odd numbers using a lambda function.
# l1 = [1,2,3,4,5]
# filterlist = list(filter(lambda a : a%2!=0,l1))
# print(filterlist)


# /////////////////////////////////////////////////////////////

# Convert a list of Celsius temperatures into Fahrenheit using a lambda function.

l1 = [1,2,3,4,5]

#method 1 :
# filterlist = []
# for i in l1:
#     var  = lambda a : a*(9/5)+32
#     filterlist.append(var(i))
# print(filterlist)

#method 2 :
# print(list(map(lambda a: a*(9/5)+32,l1)))
# /////////////////////////////////////////////////////////////

# Use a lambda function to extract the last word from a list of strings.
# str1 = "Royal Technosoft"
# li = str1.split(' ')
# var = lambda a : a[-1]
# print(var(li))


# /////////////////////////////////////////////////////////////

# Write a lambda function to find the maximum value in a list of integers.
# l1 = [1,20,3,4,5]
# var = lambda a : max(a)
# print(var(l1))



# /////////////////////////////////////////////////////////////

# Sort a list of strings based on the last character using a lambda function.
# l1 = ["Zafar","Raj","Mithil","Ajay"]

# print(sorted(l1, key= lambda a : a[-1]))


# /////////////////////////////////////////////////////////////

# Write a lambda function to find the intersection of two lists.
# /////////////////////////////////////////////////////////////

