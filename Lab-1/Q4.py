''' Write a program to check if a number is even is odd. 
Prompt the user to enter a number. 
Use the modulus operator to determine if number is even or odd.'''

num = int(input("Enter a number "))
if(num % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")
