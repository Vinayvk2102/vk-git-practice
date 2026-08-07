"""
Title: Gross Pay Calculator with Overtime
Problem Statement: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 

Test Case: Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
Note: Use input() to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
"""

# 1. Capture inputs cleanly and convert directly to floats
hrs = input("Enter Hours: ")
h = float(hrs)

rate = input("Enter the hourly rate: ")
hourly_pay = float(rate)

# 2. Compute gross pay based on a single threshold fork
if h <= 40:
    gross_pay = h * hourly_pay
else:
    # 40 hours at normal rate + remaining hours at 1.5x premium rate
    overtime_hours = h - 40
    gross_pay = (40 * hourly_pay) + (overtime_hours * 1.5 * hourly_pay)

# 3. Output the raw calculation
print(gross_pay)