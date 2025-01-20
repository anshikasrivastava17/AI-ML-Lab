''' Demonstrate the difference between mutable and immutable data types.
o	Create a list and a tuple.
o	Try to modify an element in both the list and the tuple.
o	Observe the results and explain the difference. '''

list = [1, 2, 3, 4, 5]
tuple = (6, 7, 8, 9, 10)
list[2] = 10
print("Modified list:",list)  
try:
    tuple[2] = 10
except TypeError as e:
    print("Error:", e)
print("Original tuple:", tuple)
