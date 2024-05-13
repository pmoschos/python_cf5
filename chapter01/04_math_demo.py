import math

name = "Alice"
age = 20

print("CF")
print("PI =", math.pi)

print("String Concatanation")
# print(name + " is" + age + " years old.") TypeError
print(name + " is" + str(age) + " years old.")
print("-------------------------")

# Python 2 style
print("Python 2 style")
print("PI = %6.2f" % math.pi)
print("%s is %d years old" %(name, age))
print("-------------------------")

# Pyton 3 style using string format
print("Pyton 3 style using string format")
print("Age is {0:2d}".format(age))
print("PI = {0:.3f}".format(math.pi)) # Ερώτηση: Το 0 τί σημαίνει?
print("PI = {0:.3f} and age = {1}".format(math.pi, age))
print("-------------------------")

print("{0} is {1}".format(name, age), end=" ")
print("years old.")

print("{0:*^10}:{1:>20}".format(name, age))
print("{0:*^10}:{1:<20}".format(name, age), end= "|")
print("-------------------------")

# Pyton 3 style using f-strings and variable interpolation
print("Pyton 3 style using f-strings")
print(f"{name} is {age} years old.")
