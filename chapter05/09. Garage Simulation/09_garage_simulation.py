from collections import deque

def main():
    """
    Main function to simulate cars arriving and leaving a garage using deque.
    """
    # Create a deque to represent the garage
    garage = deque()

    # Simulate some cars arriving in the garage
    garage.append("Car 1")
    garage.append("Car 2")
    garage.append("Car 3")
    garage.append("Car 4")

    # Simulate a car leaving the garage (FIFO)
    car_left = garage.popleft()

    # Simulate some more cars arriving in the garage
    garage.append("Car 5")
    garage.append("Car 6")

    # Print the current state of the garage
    print("Current state of the garage:", list(garage))
    # Print the last car that left the garage
    print("Last car which left the garage:", car_left)

if __name__ == "__main__":
    main()
