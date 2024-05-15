# Populate
fruits = ["Apple", "Banana", "Cherry", "Apple"]
print("Initial list of fruits:", fruits)


# Add
fruits.append("Berry")  # Adding a single element
print("After appending 'Berry':", fruits)

fruits.extend(["Fig", "Grape"])  # Adding multiple elements
print("After extending with ['Fig', 'Grape']:", fruits)

fruits.insert(2, "Coconut")  # Inserting an element at a specific index
print("After inserting 'Coconut' at index 2:", fruits)


# Update
fruits[1] = "Blueberry"  # Updating an element at a specific index
print("\nAfter updating index 1 to 'Blueberry':", fruits)

fruits[2:4] = ["Melon", "Dragonfruit"]  # Updating a slice of the list
print("After updating slice from index 2 to 4:", fruits)


# Delete
removed_fruit = fruits.pop(3)  # Removing an element by index
print(f"\nAfter popping index 3 (removed {removed_fruit}):", fruits)

fruits.remove("Blueberry")  # Removing an element by value
print("After removing 'Blueberry':", fruits)


# Read: Using list slicing to access parts of the list
print("\nSliced list (first three elements):", fruits[:3])
print("Sliced list (last three elements):", fruits[-3:])


# Using index() to find the position of an element
position = fruits.index("Melon")
print(f"\nThe position of 'Melon' in the list is: {position}")

# Difference between remove() and pop()
# - remove() deletes the first occurrence of the value specified.
# - pop() removes and returns the item at the specified index, or the last item if no index is specified.