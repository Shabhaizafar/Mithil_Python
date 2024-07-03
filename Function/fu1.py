# void Func();
# {
#     Func();
# }
# void Func(){

# }

"""

syntax : 
def Function_name():
    pass


Function_name()      
"""
# def say_Hello():
#     print("Hello Everyone, My Name is say_Hello.")

# say_Hello()

'''
1) without arg and without rtn
2) with arg and without rtn
3) without arg and with rtn
4) with arg and with rtn
'''
# 1) without arg and without rtn
# def print_Number():
#     print(12345)

# print_Number()


# 2) with arg and without rtn

# def Add_num(n1,n2):  # n1,n2 Perameter
#     print(n1+n2)

# Add_num(12,13)   # 12,13 Argument


# def Add_num(n1,n2,n3):  # n1,n2 Perameter
#     print(n1+n2)

# Add_num(12,13)   # 12,13 Argument




# def Add_num(n1,n2):  # n1,n2 Perameter
#     print(n1+n2)

# Add_num(int(input("Enter Value 1 : ")),int(input("Enter Value 2 : ")))   # 12,13 Argument






#-------------------------------------------------




#-------------------------------------------------
# 3) without arg and with rtn
# def All(): 
#     n1 = int(input("Enter Value of n1 :"))
#     n2 = int(input("Enter Value of n2 :"))
#     return n1+n2

# print(All())
# var = All()
# print(var)

# 4) with arg and with rtn


# ------------
# Random Number Generator: Imagine you're developing a game where you need to generate random numbers for various game mechanics, such as determining the outcome of a dice roll or picking a random event. A function that returns a random number within a specified range (e.g., 1 to 10) would be essential.

# Temperature Conversion: In a weather application, you might need to convert temperatures between Celsius and Fahrenheit based on user preferences or standard reporting. A function could take a temperature in Celsius as input and return the equivalent temperature in Fahrenheit.

# Mathematical Calculations: Consider a financial application where you need to calculate compound interest based on user input (principal amount, interest rate, and time period). A function could compute the compound interest and return the result.
# def com():
#     p=int(input("Enter Principle Amount:"))
#     i=float(input("Enter Interest rate:"))
#     t=int(input("Enter Time period:"))
#     payedAmount = p*pow((1+i/100),t)
#     return payedAmount - p 

# print(com())


# String Manipulation: In a text processing application, you might want to check if a given sentence is a palindrome (reads the same forwards and backwards). A function could take a string input, perform the palindrome check, and return True or False.
# /////////////////

# Check Stock Availability:

# Function: check_stock_availability()
# Description: This function checks if a particular product is in stock by querying a database or inventory system.
# Return Value: True if the product is available in stock, False otherwise.
# /////////////////


"""
1. **Supermarket Billing System**:
   Design a function `calculate_total_price(items)` that takes a list of items and their quantities as input, computes the total price including taxes, and returns the final bill.

2. **Weather Forecasting**:
   Create a function `get_weather_forecast(location)` that takes a location as input, retrieves the current weather data from an API, and returns a structured forecast (e.g., temperature, humidity, wind speed).

3. **Student Grade Calculation**:
   Implement a function `calculate_student_grade(scores)` that takes a list of scores as input, calculates the average score, and returns the corresponding letter grade based on a grading scale.

4. **Email Automation**:
   Develop a function `send_email(receiver, subject, body)` that takes receiver's email address, subject, and body of the email as arguments, connects to an SMTP server, and sends the email.

5. **Stock Price Analysis**:
   Write a function `analyze_stock_price(stock_data)` that takes historical stock price data as input, performs calculations such as moving averages or volatility, and returns insights or predictions.

6. **Flight Booking System**:
   Design a function `book_flight(origin, destination, date)` that takes flight details as input, checks availability, reserves seats, and returns a booking confirmation.

7. **Automated Testing Framework**:
   Create a function `run_tests(test_cases)` that takes a list of test cases, executes each test, captures results, and returns a summary report including pass/fail statuses.

8. **Personal Finance Management**:
   Implement a function `calculate_monthly_expenses(expense_list)` that takes a list of monthly expenses, computes the total expenditure, and categorizes expenses (e.g., food, utilities, entertainment).

9. **Social Media Analytics**:
   Develop a function `analyze_social_media_data(posts)` that takes social media posts as input, analyzes engagement metrics (likes, comments), and returns insights like popular topics or user engagement trends.

10. **Health Monitoring System**:
    Write a function `monitor_health(vital_signs)` that takes a person's vital signs (e.g., heart rate, blood pressure) as input, checks for abnormal values, and alerts if intervention is needed.
"""
# 1. **Supermarket Billing System**:
#    Design a function `calculate_total_price(items)` that takes a list of items and their quantities as input, computes the total price including taxes, and returns the final bill.
'''
available_product = {
    "soup" : 10,
    "chocoes" :15,
    "water bottle" : 20
}
items = {}

while(1):
    v = input("Enter Product Name : ")
    if v in available_product :
        q = int(input("Enter the Quantity :")) 
        items[v] = q 
    else :
        break

print(items)

def calculate_total_price(items):
    bill = 0
    for i in items : 
        for j in available_product :
            if(i==j):
                bill+=items[i]*available_product[j]
    return bill+bill*2.8/100
totalbill = calculate_total_price(items)
print(totalbill)
'''
# 6. **Flight Booking System**:
#    Design a function `book_flight(origin, destination, date)` that takes flight details as input, checks availability, reserves seats, and returns a booking confirmation.
"""
Allfight = {
   "UK" : {
       "2024-07-01" : {
         "12:30:00" : 20,
         "18:30:00" : 0,
         "21:30:00" : 100,
       },
       "2024-07-02" : {
         "12:30:00" : 20,
         "18:30:00" : 0,
         "21:30:00" : 100,
       }
   },
   "USA" : {
       "2024-08-01" : {
         "12:30:00" : 20,
         "18:30:00" : 0,
         "21:30:00" : 100,
       },
       "2024-08-02" : {
         "12:30:00" : 20,
         "18:30:00" : 0,
         "21:30:00" : 100,
       }
   }
}
for i in Allfight:
   print(i,Allfight[i])
origin = input("Enter your Origin place: ")
print("Destination List : ")
for i in Allfight : 
   print(i)
des = input("Enter your Destination Place: ")
for i in Allfight : 
   if i==des:
      for j in Allfight[i]:
         print(j)
fdate = input("Enter Flight Date(in YY-MM-DD): ")

def book_flight(origin, destination, date):
   for i in Allfight[destination][date] :
      if(Allfight[destination][date][i]):
         print(i,Allfight[destination][date][i])
   d = input("Enter flight Time(h:m:s) : ")
   seat = int(input("How Many Seat : "))
   if d in Allfight[destination][date]:
      if(seat<=Allfight[destination][date][d]):
         Allfight[destination][date][d] = Allfight[destination][date][d]-seat
         print("Booking Successfully Completed !!")
         print("Have a Safe journey")
      else:
         print("Sorry Sir Seats Not Available.!!")
         print(f'Only {Allfight[destination][date][d]} seats are available.')
   print(Allfight)
   

book_flight(origin,des,fdate)

"""



# 10. **Health Monitoring System**:
#     Write a function `monitor_health(vital_signs)` that takes a person's vital signs (e.g., heart rate, blood pressure) as input, checks for abnormal values, and alerts if intervention is needed.

vital_signs = {
   "Blood_pressure" : {
      "Systolic" : int(input("Enter your Systotic(mmHg) : ")),
      "Diastolic" : int(input("Enter your Diastolic(mmHg) : "))
      },
   "heart_rate":int(input("Enter your Heart_rate(bpm) : "))
   }

def monitor_health(vital_signs):
   if(vital_signs["heart_rate"]>=60 and vital_signs["heart_rate"]<=100):
      print("Heat bit Normal !!!")
   elif(vital_signs["heart_rate"]<=60):
      print("Heart Bit Too low !!!")
   else:
      print("Heart bit too High !!!")
    
   

monitor_health(vital_signs)