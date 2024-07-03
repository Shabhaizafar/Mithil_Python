# remove :
# Python list remove() method removes a given element from the list.

# myList = [10,20,30,40,50,60,60,70] 
# element = 60 
# count = myList.count(60)

# for i in range(0,count):
#     myList.remove(element)
# print(myList)

# zip : 
# stocks = ['GEEKS', 'For', 'SDfg']
# prices = [2175, 1127,2345,6789]

# ans = zip(stocks,prices)

# # li = list(ans)
# # print(li[0][0])

# new_dict = { stocks : prices for stocks,prices in zip(stocks,prices) }

# # new_dict = {stocks: prices for stocks,
# # 			prices in zip(stocks, prices)}
# print(new_dict)


myList = []

n = int(input("Enter the Number of Values : "))

for i in range(0,n):
    print("1) int\n2)str\n3)bool")
    choice = input("Enter Your Choice : ")
    if((choice) == 'int'):
        myList.append(int(input(f"Enter Value {i+1}")))
    elif((choice) == 'str'):
        myList.append(input(f"Enter Value {i+1}"))
    elif((choice) == 'bool'):
        myList.append(bool(input(f"Enter Value {i+1}")))

print(myList)

