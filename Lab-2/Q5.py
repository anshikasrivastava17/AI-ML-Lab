''' Create a program to find the factorial of a number using a loop and conditional statements.'''

number = int(input("Enter a number to find its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial is 1")
else:
    result = 1
    for i in range(1, number + 1):
        result *= i
    print("Factorial of the number",number,"is",result)
