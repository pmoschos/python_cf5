# Tuple demo with student names
students = ("Alice", "Bob", "Charlie")

# Tuples are unmodifiable!
print("Original tuple of students:", students)
# Trying to change a tuple will result in an error
# students[0] = "Dave"  # Uncommenting this line will raise a TypeError

# Enumerate through the tuple
print("\nEnumerating through the tuple:")
for index, student in enumerate(students):
    print(f"Index {index}: {student}")

# Iterate through the tuple
print("\nIterating through the tuple:")
for student in students:
    print(student)

# Tuple unpacking
print("\nTuple unpacking:")
first, second, third = students
print("First student:", first)
print("Second student:", second)
print("Third student:", third)