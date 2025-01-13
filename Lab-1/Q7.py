''' Manipulate strings using various built-in functions.
Create a string variable and find length of the string.
Convert string to uppercase and lowercase.
Check if a substring exists in the string.
Split the string into a list of words. '''

str = "Anshika is practicing python programming"
print("Length of the string is ",len(str))
print("String in uppercase is ",str.upper())
print("String in lowercase is ",str.lower())
substring = "python"
print("Substring in given string  ",substring in str)
print("Splitting string in words ",str.split())
