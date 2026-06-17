'''
Problem 7: Safe Number Parsing Unit
Problem Statement: Write a function named safe_parse_int that takes a string argument and attempts
to turn it into an integer inside a try / except block. If the conversion succeeds, return the integer. If it triggers a error, return -1.
Expected Test Code: print(safe_parse_int("Hello Bob")) outputs -1, while print(safe_parse_int("123")) outputs 123.
Small Hint: Put the int() transformation code inside the try: indentation tier and the error fallback assignment inside the except: tier.
'''

def safe_parse_int(x: str) ->int:
    try :
        return int(x)
    except:
        return -1

print(safe_parse_int("123"))
print(safe_parse_int("Hello Bob"))