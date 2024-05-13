a = 10
b = 20

result = a + b
print("a + b =", result)

print("---------")

print("Type of a:", type(a))

# Using the magic method __add__() to perform the addition
magic_result = a.__add__(b)
print("a + b =", magic_result)
