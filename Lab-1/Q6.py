''' Create a list, access elements, modify elements, and perform list operations.
Create a list of fruits.
Access elements using indexing. 
Modify elements in the list.
Add and remove elements from the list.
Find the length of the list.
Sort the list in ascending and descending order. '''

fruits = ["Strawberry", "Guava", "Cherry", "Apple", "Orange", "Banana"]
print("Accessing elements using indexing ")
print("First fruit is ",fruits[0])
print("Third fruit is ",fruits[2])

print("\n Modifying element in the list")
fruits[3] = "Watermelon"
print("Modified list is ",fruits)

print("\n Adding and removing from list")
fruits.append("Mango")
fruits.remove("Orange")
print("Modified list is ",fruits)

print("\n Length of list is ",len(fruits))

print("\n Sorted list in ascending order is ",sorted(fruits))
print("\n Sorted list in descending order is ",sorted(fruits, reverse=True))
