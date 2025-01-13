''' Write a program to take user input, process it, and display the result.
Prompt the user to enter their name. Greet the user using their name. 
Calculate and print the user's age based on their birth year. '''

name = input("Enter your name here ")
greet = f"Greetings, {name} Nice to meet you!"
print(greet)
dob = int(input("Enter your year of birth "))
print("Current age is",2025 - dob)
