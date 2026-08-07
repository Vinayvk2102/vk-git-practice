''' 
Problem 3: Odd or Even Check
Problem Statement: Write a function named is_even that takes an integer as an argument. It returns True if the number is even, and False if the number is odd.
Expected Test Code: print(is_even(7)) should output False.
Small Hint: Use the modulo operator (%). If a number divided by 2 leaves a remainder of 0 (num % 2 == 0), it's even.
'''

def is_even(num: int):
    if num % 2 ==0:
        return True
    elif num % 2 == 1:
        return False
    else : return "wrong entry"

print(is_even(-23))
    