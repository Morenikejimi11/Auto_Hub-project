#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Defininig the function to calculate total sales
def total_sales (morning_sales, evening_sales):
    total_sales = morning_sales + evening_sales
    return total_sales


# In[2]:


#Defininig the function to calculate workers salary
def workers_salary(hourly_rate, hours_worked):
    worker_salary = hourly_rate * hours_worked
    return worker_salary


# In[3]:


#Defininig the function to calculate profit made on sales
def profit(total_sales, total_cost):
    profits = total_sales - total_cost
    return profits


# In[4]:


#Defininig the function to calculate worker tips at 2%
def workers_tips(shift_sales):
    workers_tips = 0.02 * shift_sales
    return workers_tips


# In[5]:


#Defininig the function to calculate total tips for the day
def total_tips(morning_sales, evening_sales):
    total_tips = workers_tips(morning_sales) + workers_tips(evening_sales)
    return total_tips


# In[6]:


def print_operations_menu():
    print("Choose an operation:")

def get_my_choice():
    return input("Enter your my_choice (1-5): ")

def get_total_sales_input():
    return float(input("Enter morning sales: ")), float(input("Enter evening sales: "))

def get_hourly_rate_input():
    return float(input("Enter hourly rate: ")), float(input("Enter hours worked: "))

def get_total_tips_input():
    return float(input("Enter total sales: ")), float(input("Enter total cost: "))


# In[ ]:


#Including error handling for scenarios such as division by zero.
#It didnt turn out the way i thought it will, so im commenting it.
#def profit(total_sales, total_cost):
    #try:
        #return total_sales / total_cost
    #except ZeroDivisionError:
        #print("Error: Division by zero is detected. Please make sure your total cost is not zero.")
        #return None


# In[7]:


#Creating a user interaction that provides a clear structure to the program.
def operations_menu():
    print("\nGREETINGS! YOU HAVE ENTERED THE ACCOUNTING AUTOMATION HUB!!\n")
    print('AVAILABLE SERVICE SELECTION') #Options Header
    print('Navigate the Menu Below:') #Guides users to select an option
    print('1. Total Sales') 
    print('2. Workers Salary')
    print('3. Profits')
    print('4. Total Tips')
    print('5. Exit ACCOUNTING AUTOMATE HUB')


# In[8]:


#Using a while True loop to create a user interaction that provides a clear structure to the program.
# Main program loop
while True:
    operations_menu()
    my_choice = input('Enter your my_choice (1-5): ')
    if my_choice == '5':
            print("\nUSER ENTRY CONFRIMED.")
            print("\nTerminating the Program")
            print("\nTerminating the program. Adieu!!") #For user to exit by entering '5', and it provides a friendly terminating message
            break
#Using a try-except block for input validation to catch ValueError in case the user enters a non-numeric value.
    try:
        my_choice = int(my_choice)
        if 1 <= my_choice <= 4:
            morning_sales = float(input("Enter morning sales: "))
            evening_sales = float(input("Enter evening sales: "))
        if my_choice == 2:
            hourly_rate = float(input("Enter hourly rate: "))
            hours_worked = float(input("Enter hours worked: "))
        if my_choice == 3:
            total_sales = float(input("Enter total sales: "))
            total_cost = float(input("Enter total cost: "))
            
    except ValueError:
        print("Invalid Input. Enter a number between 1 and 5.")
        continue
        
#This shows us a code modular, with separate functions for each calculation task. 
#This promotes code reuse and makes it easier to understand and maintain.

    if my_choice == 1:
        total_sales = morning_sales + evening_sales
        print('\nUSER ENTRY CONFRIMED.\nVIEW OUTCOME BELOW!!')
        result = total_sales
    elif my_choice == 2:
        workers_salary = hourly_rate * hours_worked
        print('\nUSER ENTRY CONFRIMED.\nVIEW OUTCOME BELOW!!')
        result = workers_salary
    elif my_choice == 3:
        profits = total_sales - total_cost
        print('\nUSER ENTRY CONFRIMED.\nVIEW OUTCOME BELOW!!')
        result = profits
        if total_sales < total_cost: # Check the financial status of the store based on total sales and total cost
            print('It seems like the business may be incurring a deficit, indicating a non-profitable situation.')
        elif total_sales > total_cost:
            print('It looks like the business is making a surplus. indicating the business is in a profitable state.')
        else: #total_sales == total_cost:
            print("It looks like the business has balanced its costs and income. Now, we'll observe whether it starts turning a profit or faces a loss.") 
                       #depending on how the business the business is been manage.

    elif my_choice == 4:
        total_tips = workers_tips(morning_sales) + workers_tips(evening_sales)
        print('\nUSER ENTRY CONFRIMED.\nVIEW OUTCOME BELOW!!')
        result = total_tips
    else:
        print("Invalid Input. Enter a number between 1 and 5.")
        continue

    print(f"Result: {result}\n")

if __name__ == "__operation_menu__":
    operations_menu ()

            


# # Discussing the challenges i encountered while working on this project

#  Example Code 
# #def profit(total_sales, total_cost):
#     #try:
#         #return total_sales / total_cost
#     #except ZeroDivisionError:
#         #print("Error: Division by zero is detected. Please make sure your total cost is not zero."
#               #return None
# 
#  1. Handling Division by Zero:
#   The operation main challenge in this code was addressing the possibility of dividing by zero. In the `profit` function,
#     I implemented a try-except block to catch a ZeroDivisionError and provided a meaningful error message. Ensuring that
#     the program doesn't crash when encountering such scenarios was crucial for user-friendly error handling 
#  and i dont seem to get it very well so i commented it out.
# 
# 2. User Input Handling:
# 
# Challenge: Ensuring robust user input handling, especially when expecting numeric values.
# Solution: Implemented a try-except block to catch ValueError and provided a user-friendly error message.
# Modular Code Structure:
# 
# Challenge: Structuring the code into separate functions for each calculation task.
# Solution: Successfully created modular functions for calculations, promoting code reuse and maintainability.
#     
# 3. Loop Structure:
# 
# Challenge: Using a while True loop for user interaction while maintaining a clear program structure.
# Solution: Structured the loop to present the user menu, handle user choices, and exit the program gracefully.
#     
# 4. Calculation Logic:
# 
# Challenge: Implementing accurate logic for calculations such as total sales, worker's salary, and profit.
# Solution: Ensured correct calculations for each scenario based on user input and business logic.
#     
# 5. Error Messages:
# 
# Challenge: Crafting informative and user-friendly error messages for various scenarios.
# Solution: Provided clear error messages for invalid input, guiding the user on how to correct their entries.
#     
# 8.User Experience:
# 
# Challenge: Balancing user experience with informative output messages.
# Solution: Incorporated messages to confirm user entries, display outcomes, and provide friendly termination messages.
#     
# 9. Business Financial Analysis:
# 
# Challenge: Accurately interpreting and presenting the financial status of the business.
# Solution: Implemented checks to determine if the business is incurring a deficit, making a surplus, or at a break-even point.
#     
# 10. Readability and Maintainability:
# 
# Challenge: Ensuring code readability and maintainability with clear comments and structure.
# Solution: Used meaningful comments and organized the code to enhance readability and ease of maintenance.
