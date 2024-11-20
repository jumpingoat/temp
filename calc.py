import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculator():
    # Get the operation choice
    operation = input("Enter the operation by using the corresponding number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: ")

    # Get the operands
    operand1 = float(input("Enter operand 1: "))
    operand2 = float(input("Enter operand 2: "))

    # Perform the chosen operation
    if operation == "1":
        logging.info(f"Adding {operand1:.2f} and {operand2:.2f}")
        result = addition(operand1, operand2)
    elif operation == "2":
        logging.info(f"Subtracting {operand2:.2f} from {operand1:.2f}")
        result = subtraction(operand1, operand2)
    elif operation == "3":
        logging.info(f"Multiplying {operand1:.2f} and {operand2:.2f}")
        result = multiplication(operand1, operand2)
    elif operation == "4":
        logging.info(f"Dividing {operand1:.2f} by {operand2:.2f}")
        result = division(operand1, operand2)
    else:
        print("Invalid operation choice.")
        return

    # Display the result
    print(f"The result is {result:.2f}")

# Call the calculator function
calculator()