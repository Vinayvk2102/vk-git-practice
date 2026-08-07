''' 
Problem 4: Maximum of Three
Problem Statement: Write a function named find_max that takes three numeric arguments and returns the largest of the three. Do not use Python's built-in max() function—build the comparison logic yourself using if-elif-else.
Expected Test Code: print(find_max(12, 45, 19)) should output 45.
Small Hint: Use comparison operators like >= to see if the first number is greater than or equal to both the second and third numbers.
'''

def find_max(x: float, y: float, z: float) ->float:
    if x >= y and x >=z:
        return x
    elif y >= x and y >= z:
        return y
    else : return z

print(find_max(12,45,19))