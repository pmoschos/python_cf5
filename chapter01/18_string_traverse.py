message = "Coding Factory"

# zero index
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

# immutable
# message[0] = 'c'

# len(): returns the size of a collection
print(f"Number of letters inside the {message}: {len(message)}")

# Enhanced for
for char in message:
    print(char)

# range(n): επιστρέφει 0 έως n - 1
for i in range(10):
    print(i)

# Simple for
for i in range(len(message)):
    print(message[i], end=" ")
print()
