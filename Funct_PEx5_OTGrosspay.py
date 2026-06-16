''' 
Problem 5: The Refactored Overtime Gross Pay Calculator
Problem Statement: Let's refactor your previous assessment problem into a clean, reusable function! 
Write a function named compute_pay that takes two parameters: hours and rate. 
It should compute and return the gross pay, giving 1.5 times the hourly rate for all hours worked strictly above 40.
Expected Test Code: print(compute_pay(45, 10.50)) should output 498.75.
Small Hint: The logic inside the function will be exactly like your fixed assessment script, 
but you pass the parameters at the top and return the final variable value.
'''

def compute_pay(hours: float, rate: float) ->float:
    if hours >= 0:
        if hours <= 40:
            return hours*rate
        else :
            return ((hours-40)*1.5*rate)+(40*rate)
    else :
        return "wrong_entry"

print(compute_pay(65,10.50))

