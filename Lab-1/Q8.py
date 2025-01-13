''' Write a program to find largest and smallest number in a list. '''

list = [75, 80, -4, 332, 23, 0, 2.1, 90]
list = sorted(list)
print("Smallest number is",list[0])
print("Largest number is",list[len(list)-1])
