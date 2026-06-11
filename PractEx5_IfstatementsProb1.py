#Title: The Over-Budget Alert System

#Problem Statement: Write a program for a personal finance app. 
# The user inputs their monthly budget and their actual total expenses. 
# If the expenses are strictly greater than the budget, print "Alert: You have exceeded your budget!". 
# Otherwise, print "Great job! You stayed within your budget."

#solution:

budget = float(input("Enter your monthly budget: "))
expenses = float(input("Enter your total expenses: "))

if expenses > budget:
    print("Alert: You have exceeded your budget!")
else:
    print("Great job! You stayed within your budget.")