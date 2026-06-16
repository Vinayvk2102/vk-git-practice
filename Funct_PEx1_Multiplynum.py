'''
Problem 1: The Multiplier Unit
Problem Statement: Write a function named multiply_numbers that takes two parameters, multiplies them together, and returns the result.
Expected Test Code: print(multiply_numbers(4, 5)) should output 20.
Small Hint: Use the def keyword to declare the function and ensure you use return, not print, to send the result back.
'''
def multiply_numbers(x,y): #Spaces around operators: Put spaces around the = and * operators.
    z = x*y         #Spaces after commas: Put a space after the comma in your parameters (x, y).
    return(z)   #Return is a statement, not a function: In Python, return doesn't need parentheses. Write return z instead of return(z)
    
print(multiply_numbers(3, 6))

