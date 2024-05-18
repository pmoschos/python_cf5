#import hello
# from hello import my_add_function
from my_calculations import my_add_function as my_add, num1

num2 = 10

#res = hello.my_add_function(num1, num2)
# res = my_add_function(num1, num2)
res = my_add(num1, num2)

print(f"The sum of {num1} and %d is: {num2}")

print(__name__)