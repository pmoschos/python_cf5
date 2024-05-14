# List crud functions

# Populate a list
ages = [19, 23, 34, 45]
print("Initial list of ages:", ages)

# Read: Iterating over a list and accessing both the index and the value
print("\nIterating with index and value:")
for index, value in enumerate(ages):
    print(f"Index {index}: {value}")

# Iterating with enhanced for loop
print("\nIterating with enhanced for loop:")
for age in ages:
    print(age, end=' ')
print()

# for loop does not have its own scope in Python
print(f"age = {age}")