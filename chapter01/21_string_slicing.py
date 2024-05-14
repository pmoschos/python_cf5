s = "Coding Factory"

s1 = s[7]  # F
s2 = s[:6] # Coding
s3 = s[7:] # Factory
s4 = s[:]  # Coding Factory
# s4 = s[::]  # Coding Factory

# negative slicing
s5 = s[:-1] # Coding Factor
s6 = s[:-2] # Coding Facto

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

# reverse string
# r_s = s[-1::-1]
r_s = s[::-1] # yrotcaF gnidoC
print(r_s)

# question
s_q = s[7:7] # nothing
print(s_q)