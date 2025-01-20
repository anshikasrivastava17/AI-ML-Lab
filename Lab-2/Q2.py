''' Create and manipulate dictionaries.
o	Create a dictionary to store information about a person (name, age, city).
o	Access values using keys.
o	Add a new key-value pair to the dictionary.
o	Modify an existing value.
o	Check if a key exists in the dictionary.
o	Get a list of all keys and values. '''

person = {
    "name": "Anshika",
    "age": 20,
    "city": "Lucknow"
}
print("Accessing values using keys")
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

print("\nAdding new key value pair")
person["email"] = "anshikasrivastava561@gmail.com"
print("Updated dictionary with email:", person)

print("\nModifying existing value")
person["age"] = 21
print("Modified age:", person)

print("\nChecking if key exists")
if "city" in person:
    print("Key 'city' exists in the dictionary")

print("\nList of all keys and values")
keys = person.keys()
values = person.values()
print("Keys:", list(keys))
print("Values:", list(values))
