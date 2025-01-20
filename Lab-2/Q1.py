'''Create and access tuples.
Create a tuple of colors.
Access elements using indexing.
Try to modify an element in the tuple (to demonstrate immutability).
Find the number of occurrences of a specific element in the tuple. '''

colors = ("Red", "Violet", "Magenta", "Yellow", "Green", "Red","Black")
print("First color:", colors[0])  #indexing  
print("Last color:", colors[-1])
print("Showing that tuple is immutable")
#colors[3]="white"
red_count = colors.count("Red")
print("Number of times 'red' appears:", red_count)
