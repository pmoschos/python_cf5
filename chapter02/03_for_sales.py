# List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# The fruit we want to check for
fruit_to_check = "Apple"

# Search for the fruit in the list
for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list.")
        break
else:
    # This block is executed only if the loop is not broken
    print(f"{fruit_to_check} is not in the list.")

# Additional example with another fruit
fruit_to_check = "Mango"

# Search for the fruit in the list
for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list.")
        break
else:
    # This block is executed only if the loop is not broken
    print(f"{fruit_to_check} is not in the list.")


# Pythonic and powerful
print()
print("Why do Python devs never get lost? Because they always know where 'in' is!")
print("he he...") 
fruit_to_check = "Grapes"
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list.")