# explicit typecasting in python = manually converting one data type to another using built-in functions like int(), float(), str(), bool(), etc.


age = 21
name = "Vinay"
GPA = 9.8
student = True

age = float(age)  # Typecasting age from int to float
GPA = int(GPA)   # Typecasting GPA from float to int   
student = str(student)  # Typecasting student from bool to str

print('age: ' + str(type(age)))
print('GPA: ' + str(type(GPA)))
print('student: ' + str(type(student)))

# if we convert here like boolage = bool(age) then it will return true because age is not 0 or empty string.
# but if the age is 0 then it will return false because 0 is considered as false in python. Similarly for string if it is empty then it will return false.
