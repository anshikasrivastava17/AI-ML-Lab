'''Write a program to check if a given number is prime.'''

number = int(input("Enter a number to find if prime or not: "))
count = 0
for i in range(1,number+1):
    if(number%i==0):
        count=count+1

if(count==2):
    print("The given number",number,"is prime")
else:
    print("The given number",number,"is not prime")
