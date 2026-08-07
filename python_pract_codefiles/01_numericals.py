# Get two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate the product
product = num1 * num2

# Check if product is less than or equal to 1000
if product <= 1000:
    result = product
else:
    result = num1 + num2

# Print the result
print("Result:", result)