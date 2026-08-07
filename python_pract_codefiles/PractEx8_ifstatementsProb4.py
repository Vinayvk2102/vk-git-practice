# Title: The Cyber Secure Password Validator
# Problem Statement: Let's simulate a two-step secure login check using nested if statements. 
# Write a program that sets a system password variable inside the code (e.g., sys_pass = "secure123").
# The program first asks the user to input their password.
#
# If the password matches sys_pass, it proceeds to a second security question: "Enter your 4-digit PIN: ". 
# If the PIN is exactly 8055, print "Access Granted: Welcome VK Boss.". 
# If the PIN is wrong, print "Access Denied: Invalid Security PIN."
# If the initial password input was completely wrong from the start, the program shouldn't even ask for the PIN; 
# it should immediately print "Access Denied: Incorrect Password. You are not authorized to access this system. if you try multiple time i will self destruct this system." and end.

print("Welcome to the Vk Cyber Secure Password Validator")

sys_pass = "vk1234"
sys_pin = 8055

user_pass = input("Please enter your password to access the system: ")
if user_pass == sys_pass:
    print("Password Accepted: Proceeding to PIN verification.")
    user_pin = int(input("Please enter your 4-digit PIN: "))
    if user_pin == sys_pin:
        print("Access Granted: Welcome to the system - VK Boss!")
    else:
        print("Access Denied: Incorrect PIN. Go away or I'll self destruct the system!")
else:
    print("Access Denied: Incorrect password. \nGo away you are not authorized to access this system. \nIf you try multiple times I'll self destruct the system!")