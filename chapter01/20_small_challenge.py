# print the message as follows

# Challenge 1
# F
# aa     
# ccc    
# tttt   
# ooooo
# rrrrrr
# yyyyyyy

message = "Factory"

for i in range(len(message)):
    print(message[i] * (i + 1))

# Challenge 2
# F******
# aa*****
# ccc****
# tttt***
# ooooo**
# rrrrrr*
# yyyyyyy

for i in range(len(message)):
    print(message[i] * (i + 1), end="*" * (len(message) - i - 1))
    print()

