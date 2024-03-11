def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def stop():
    print("Stopping the calculator...")
    quit()

operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide,
    '5': stop
}

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Stop")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in operations:
        if choice == '5':
            operations[choice]()
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = operations[choice](num1, num2)
        print("Result:", result)
    else:
        print("Invalid input. Please enter a valid number.")
