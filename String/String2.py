mystr = "                   ROYAL TECHNOSOFT PVT LTD           "

# 3)     covert in a lowercase 
# print(mystr.casefold())
# print(mystr)

# 4)
# print(mystr.center(30)) #default
# print(mystr.center(30," ")) #default
# print(mystr.center(30,"*"))

# 5)     
# print(mystr.endswith('D'))

# 6)
# print(mystr.find("T"))
# print(mystr.find("Z")) # -1
# print(mystr.find("T",13))
# print(mystr.find("T",18,23))
# print(mystr.find("T",18,-2))


# 7)
# mystr.format
# st1 = "For only {price:.2f} dollars!"
# print(st1.format(price = 4))

# 8)
# mystr.join
# print(mystr.join("Royal"))

# 9)
# mystr.ljust
# print(mystr.ljust(30,"*"))

# 10)
# mystr.lower
# print(mystr.lower())

# 11)
# mystr.lstrip
print(mystr.lstrip(),"Z")


# 12)
# print(mystr.rjust(30,"*"))

# 13)
print(mystr.rstrip(),"Z")

# 14)
print(mystr.strip(),"Z")