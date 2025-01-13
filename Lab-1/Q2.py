''' Create variables of different data types (integer, float, string, boolean) and perform basic operations on them.
Assign values to variables of different data types. 
Perform arithmetic operations on numeric data types. 
Concatenate strings using + operator.
Use logical operators to evaluate boolean expressions '''

integer = int(input("Enter the integer number "))
float = float(input("Enter the float number "))
string = input("Enter the string ")
boolean = bool(input("Enter the boolean value "))

print("Addition of two numbers",integer + float)
print("Subtraction of two numbers",integer - float)
print("Multiplication of two numbers",integer * float)
print("Division of two numbers",integer / float)
print("Modulus of two numbers",integer % float)

print(string + " from Anshika\n") #concatenation

#logical operators
print("AND operation",boolean and True)
print("OR operation",boolean and True)
print("NOT operation",not boolean)
