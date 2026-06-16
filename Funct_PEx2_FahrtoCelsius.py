'''Problem 2: Fahrenheit to Celsius Converter
Problem Statement: Write a function named to_celsius that takes a temperature in Fahrenheit as an argument, 
converts it to Celsius using the formula $C = (F - 32) \times \frac{5}{9}$, and returns the value.
Expected Test Code: print(to_celsius(32)) should output 0.0.
Small Hint: Be mindful of mathematical operator precedence (BODMAS). Use parentheses around F - 32.
'''
def to_celsius(F: float) -> float:
    return (F - 32) * (5 / 9)

print(to_celsius(32))