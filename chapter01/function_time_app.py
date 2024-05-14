def convert_seconds(seconds):
    # Constants for time calculations
    SECONDS_IN_A_MINUTE = 60
    SECONDS_IN_AN_HOUR = 3600
    SECONDS_IN_A_DAY = 86400

    # Calculate number of days
    days = seconds // SECONDS_IN_A_DAY
    seconds_remaining = seconds % SECONDS_IN_A_DAY

    # Calculate number of hours
    hours = seconds_remaining // SECONDS_IN_AN_HOUR
    seconds_remaining %= SECONDS_IN_AN_HOUR

    # Calculate number of minutes
    minutes = seconds_remaining // SECONDS_IN_A_MINUTE
    seconds_remaining %= SECONDS_IN_A_MINUTE

    # Remaining seconds
    seconds = seconds_remaining

    return days, hours, minutes, seconds

def main():
    # Take input from the user
    total_seconds = int(input("Enter the number of seconds: "))

    # Convert the total seconds into days, hours, minutes, and seconds
    days, hours, minutes, seconds = convert_seconds(total_seconds)

    # Display the result
    print(f"{total_seconds} seconds is equal to:")
    print(f"{days} days")
    print(f"{hours} hours")
    print(f"{minutes} minutes")
    print(f"{seconds} seconds")

if __name__ == "__main__":
    main()
