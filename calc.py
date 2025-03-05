import logging

# Konfiguracja
logging.basicConfig(level=logging.INFO, format="%(message)s")

def addition(*args):
    return sum(args)

def subtraction(a, b):
    return a - b

def multiplication(*args):
    result = 1
    for num in args:
        result *= num
    return result

def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Mapowanie inputu na funkcje
operations = {
    "1": ("Addition", addition),
    "2": ("Subtraction", subtraction),
    "3": ("Multiplication", multiplication),
    "4": ("Division", division),
}

def calculator():

    operation = input(
        "Enter the operation by using the corresponding number:\n"
        "1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: "
    )

    if operation not in operations:
        print("Invalid operation choice.")
        return

    op_name, op_func = operations[operation]


    if operation in ("1", "3"):  
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
    else:  
        numbers = list(map(float, input("Enter operand 1 and operand 2 separated by space: ").split()))
        if len(numbers) != 2:
            print("Please enter exactly two numbers.")
            return

    logging.info(f"{op_name} of {', '.join(f'{num:.2f}' for num in numbers)}")
    
    try:
        result = op_func(*numbers)
       
