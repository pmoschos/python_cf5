# List CRUD Functions

# Populate a list
ages = [19, 23, 34, 45]
print("Initial list of ages:", ages)

# Read: Iterating over a list and accessing both the index and the value
print("\nIterating with index and value:")
for index, value in enumerate(ages):
    # Using enumerate() to get both index and value while iterating
    print(f"Index {index}: {value}")

# Iterating with enhanced for loop
print("\nIterating with enhanced for loop:")
for age in ages:
    # Simple iteration over the list values
    print(age, end=' ')
print()

# for loop does not have its own scope in Python
# The variable 'age' used in the for loop is still accessible here
print(f"age = {age}")
