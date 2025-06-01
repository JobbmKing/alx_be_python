# Ask the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for rows
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop for each column in the row
    for _ in range(size):
        print("*", end="")  # Print stars side by side
    print()  # Move to the next line after each row
    row += 1

