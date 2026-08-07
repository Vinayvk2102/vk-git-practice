'''
Problem 8: The E-Commerce Delivery Fee Calculator
Problem Statement: Write a function named calculate_shipping that takes two parameters: weight (float) and is_premium_member (boolean True/False).
If is_premium_member is True, shipping is always 0.0.
If False, shipping is 5.0 for weights under 5 kg, and 15.0 for weights 5 kg or more. Return the final shipping cost.
Expected Test Code: print(calculate_shipping(10, False)) should output 15.0.
Small Hint: Check the boolean flag first using an outer if statement, or evaluate it in parallel using logical conjunctions.
'''
def calculate_shipping(weight: float, is_premium_member: bool) -> float:
    """Calculates e-commerce shipping fees based on weight and membership status."""
    # 1. Guard Clause: Instantly handle invalid physical data
    if weight <= 0:
        raise ValueError("Weight must be greater than 0 kg.")
        
    # 2. Premium VIP Exception: Exit early
    if is_premium_member:
        return 0.0
        
    # 3. Standard Pricing Tiers (No nested code needed!)
    if weight < 5.0:
        return 5.0
    else:
        return 15.0


# --- Testing Execution Safely ---
try:
    # Testing valid non-premium heavy package
    print(calculate_shipping(10.0, False))  # Output: 15.0
    
    # Testing premium member package
    print(calculate_shipping(3.5, True))    # Output: 0.0
    
    # Testing what happens with an invalid weight
    print(calculate_shipping(-2.0, False))
    
except ValueError as e:
    print(f"Data Error: {e}")