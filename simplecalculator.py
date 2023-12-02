# Simple Calculator

# Function to add two numbers
def add(x, y):
    add==1
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    subtract==2
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    multiply==3
    return x * y

# Function to divide two numbers
def divide(x, y):
    divide==4
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program
while True:
    # Display a menu of operations
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter 'exit' to end the program")

    # Get user input
    choice = input("Enter your choice: ")

    # Check for exit
    if choice == "exit":
        break

    # Check for valid operation choice
    if choice not in ("1", "2", "3", "4"):
        print("Invalid input. Please try again.")
        continue

    # Get user input for numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the chosen operation
    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)

    # Display the result
    print("Result: " + str(result))
