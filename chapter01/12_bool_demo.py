a = True
b = False

print(type(a), a)
print(type(b), b)
    

result = a or b  # `b` is not evaluated because `a` is `True`
print(result)  # Output: True

# Knowledge out of the box
print("True + True = ", True + True)

