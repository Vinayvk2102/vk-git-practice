#Given three inputs that are stored in the variables a, b, and c. You need to print a a times and b b times  in a single line separated by c.

a = int(input("Enter the value of a: ")) # we are taking input for a and converting it to integer because we want to repeat the string a times and for that we need a to be an integer.
b = int(input("Enter the value of b: ")) # we are taking input for b and converting it to integer because we want to repeat the string b times and for that we need b to be an integer.
c = str(input("Enter the value of c: ")) # we are taking input for c and converting it to string because we want to separate a and b with c and for that we need c to be a string.


print((str(a)*a)+c+(str(b)*b)) # here we are converting a and b to string because we want to repeat the string a times and b times and for that we need a and b to be strings. Then we are concatenating a, c, and b to get the final output. For example if a is 3, b is 2, and c is "-", then it will print "333-22".