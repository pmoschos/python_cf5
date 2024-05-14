# Constants for time calculations
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_DAY = 86400

total_seconds = int(input("Enter the number of seconds: "))
# 105310 seconds is equal to: 
# 1 days, 5 hours, 15 minutes, 10 seconds

# Calculate number of days
days = total_seconds // SECONDS_IN_A_DAY
seconds_remaining = total_seconds % SECONDS_IN_A_DAY

# Calculate number of hours
hours = seconds_remaining // SECONDS_IN_AN_HOUR
seconds_remaining %= SECONDS_IN_AN_HOUR

# Calculate number of minutes
minutes = seconds_remaining // SECONDS_IN_A_MINUTE
seconds_remaining %= SECONDS_IN_A_MINUTE

# Remaining seconds
seconds = seconds_remaining


# Display the results
print(f"{total_seconds} seconds is equal to:")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")