"""
What is Set : 
A Python set is the collection of the unordered items. 

Each element in the set must be unique, immutable, and the sets remove the duplicate elements. 

Sets are mutable which means we can modify it after its creation.

Unlike other collections in Python, there is no index attached to the elements of the set, i.e., we cannot directly access any element of the set by the index.

However, we can print them all together, or we can get the list of elements by looping through the set.
"""

# mySet = {}
# print(mySet)
# print(type(mySet))

# print(type(set()))
# mySet = set({1,2,3})
# print(mySet)
# print(type(mySet))

# l1 = [5,6,3,2,1]
# print(mySet)

# mySet = {"raj","ajay","mohak"}
# print(sorted(mySet))
# print(mySet)
# l1 = list(mySet)
# print(l1)
# s1 = set(l1)
# print(s1)


# s1 = {5,6,3,2,1}

# print(len(s1))
# for i in range(0,5) : 
#     print(i)

# s1.add(7)
# print(s1)

# s1.clear()

# print(s1)
# print(type(s1))


# s1 =set()

# s1.add(1)

# s1 = {5,3,2,1,4}
# # s1.copy
# # s2 = s1.copy()
# # print(id(s1))
# # print(id(s2))


# # s1.difference
# s2 = {8,4,5,7,6}
# diff = s1.difference(s2)
# print(diff)

# print(s2)
# diff1 = s2.difference(s1)
# print(diff1)

# print({10, 23, 1, 5, 7, 12, 3, 8, 15})

# s1 = {4,5,6}
# s2 = {4,5}
# diff = s1.difference(s2)  #1, 2, 3  #return new Set
# diff1 = s2.difference(s1)

# l1 = list(diff)
# l2 = list(diff1)
# l1.extend(l2)
# print(set(l1))

# s1.difference_update

# s1.difference_update(s2)   # change orignal  set
# print(s1)

# s1.discard
# s1.discard(6)
# print(s1)

# s1.intersection
# d =  s1.intersection(s2)
# print(d)

# s1.intersection_update
# s1.intersection_update(s2)
# print(s1)

# s1.isdisjoint
# s =s1.isdisjoint(s2)   # return true when  not same items in given sets
# print(s)

# s1.issubset
# print(s1.issubset(s2)) 

# s1.issuperset
# print(s1.issuperset(s2))


# s1.pop

# s1 = {10, 23, 1, 5, 7, 12, 3, 8, 15}
# s1 = {"red","green","white"}
# s2 = s1.pop()
# s1.pop()
# s1.pop()

# s1.pop()


# print(s1)
# ###################################################################
s1 = {10, 23, 1, 5, 7, 12, 3, 8, 15}
s2 = {1,3,5,10,50}
# print(s1)
# s1.symmetric_difference  # print different value for both and remove same values in a given set.

# s3 = s1.symmetric_difference(s2)   
# print(s3)

# s1.symmetric_difference_update
# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)



# s1.remove
# s1.remove(100)
# s1.discard(10)
# print(s1)

# s1.union
# s3 = s1.union(s2)
# print(s3)

# s1.update
# s1.update(s2)
# print(s1)



# ///////////////////
# 13. Write a Python program that uses frozensets.
# Note: Frozensets behave just like sets except they are immutable.
# 22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
