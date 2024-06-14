# Python divides the operators in the following groups:

# ✅ Arithmetic operators
''' +,-,*,/,%,**,// '''
# ######################################

#     Assignment operators
''' =,+=,-=,*=,/=,%=,//=,**,&=,|=,^=,>>=,<<=,:= '''

#1) =
# x = 5
# print(x)

# 2) +=
# x = 5
# x+=10  # x = x+10  = 5+10 = 15
# print(x)

# 3) -=
# x = 10
# x-=5  # x=x-5 = 10-5 = 5
# print(x)


# 4) *=
# x = 5
# x*=3 # x=x*3 = 5*3 = 15
# print(x)

# 5) /=
# x=12
# x/=3  #  x = x/3 = 12/3 = 4.0
# print(x)

# 6) %=
# x = 13
# x%=2 # x = x%2 = 13%2 = 1
# print(x)


# 7) //=
# x = 15
# x//=5 # x = x//5 = 15//5 = 3
# print(x)

# 8) **=
# x = 4
# x **=2  # x = X**2 = 4**2 =16
# print(x)


# remaining due to not cover logical and bitwise operator
# 9) &=
# 10) |=
# 11) ^=
# 12) >>=
# 13) <<=
# 14) :=




# ######################################
#     Comparison operators
'''==,!=,<,<=,>,>='''
###########################################
#     Logical operators
'''and,or,not'''
'''
1) and operator
 false = 0   true = 1
eq1         eq2         o/p
false       false       false
true        false       false
false       true        false
true        true        true
'''
# x = 1
# y = 1

# print(x and y)

'''
2) OR Operator 
 false = 0   true = 1
eq1         eq2         o/p
false       false       false
true        false       true
false       true        true
true        true        true
'''
# x = 0
# y = 0
# print(x or y)

'''
3) NOT Operator
eq          o/p
1           0
0           1
'''
# x = 1
# print(not x)
############################################

#     Identity operators
'''is , is not'''
# value1  = 12
# value2 =  12

# print(value1==value2) #True    (check Both value are or  not)
# print(value1 is value2) #True  (check Both Value are  refer to the same memory )

# print(id(value1))
# print(id(value2))


# print(value1 is not value2)#False (check Both Value are  refer to the different memory or not )

######################################
#     Membership operators
'''in ,not in'''

# value3 = "Prem"
# value4 = "z"

# print(value4 in value3) #False

# print(value4 not in value3) #True 

###########################################
#     Bitwise operators
'''&,|,~,^,<<,>>'''
# value5 = 1
# value6 = 3
# print(value5 & value6)

# value7 = 3   #  0011
# value8 = 5   #  0101

# print(value7 & value8) #0001   = 1

# print(value7 | value8) #0111   = 7

# print(~value7)  

'''
OR
0       0       0
0       1       1
1       0       1
1       1       1
AND
0       0       0       
0       1       0
1       0       0
1       1       1
'''

'''
        2^3   2^2   2^1    2^0
         8     4     2      1

0   =    0     0     0      0
1   =    0     0     0      1
2   =    0     0     1      0
3   =    0     0     1      1
4   =    0     1     0      0
5   =    0     1     0      1
6   =    0     1     1      0
7   =
8   =
9   =
10  =
11  =
12  =
13  =
14  =
15  =

'''