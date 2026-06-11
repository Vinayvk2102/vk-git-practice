#Title: The Interview Eligibility Screener

#Problem Statement: A tech recruitment agency wants an automated script to do a first-pass check on candidates. The script asks two questions:
#"Do you know Python? (yes/no): "
#"How many years of programming experience do you have?: "

# A candidate is invited for an interview only if 
# they answer "yes" to Python AND have 2 or more years of experience. 
# If they qualify, print "Application Approved: Welcome to the interview loop!". 
# If they don't, print "Application Deferred: Profile does not match current criteria."


x = str(input("Do you know python? (yes/no):  "))
if x == "yes":
    y =  float(input("How many years of experience do you have? "))
    if y >= 2:
        print("Application Approved: Welcome to the interview loop!")
    else:
        print("Application Deferred: Profile does not match current criteria.")
else:    
    print("Application Rejected: Python knowledge is required for this position.")