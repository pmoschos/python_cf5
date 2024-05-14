# Short Circuit

username = input(f"Enter your username: ")
email = input("Enter your email: ")

# Using 'or' to set 'valid_user'
# If 'username' is truthy, use it; otherwise, use the fallback value "User"
valid_user = username or "User"

# Using 'or' to set 'valid_user'
valid_user = username or "User"

print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or ("please provide a valid email address.")))

