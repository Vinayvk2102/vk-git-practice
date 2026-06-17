'''
Problem 9: Leap Year Diagnostic Tool
Problem Statement: Write a function named is_leap_year that takes a year (integer) as input and returns True if it is a leap year, and False otherwise.
The Leap Year Rule: A year is a leap year if it is perfectly divisible by 4, except when it is divisible by 100.
However, if it is also divisible by 400, it is still a leap year.
Expected Test Code: print(is_leap_year(2000)) outputs True; print(is_leap_year(1900)) outputs False.
Small Hint: This is a classic tech interview puzzle. It requires ordering your mathematical checks using modulo (% 400, % 100, % 4) in a clean, non-overlapping if-elif-else framework.
e, Run and Debug online from anywhere in world.
'''

def is_leap_year(x: int) -> bool:
    if x % 100 == 0:
        if x % 400 == 0:
            return True
        else :
            return False
    elif x % 4 == 0:
        return True
    else :
        return False

print(is_leap_year(2000))
print(is_leap_year(1900))