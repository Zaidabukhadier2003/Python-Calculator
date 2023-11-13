import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base):
    return math.log(x, base)

def calculate():
    print("Advanced Calculator:")
    print("Available operations:")
    print("1. Basic Operations (+, -, *, /)")
    print("2. Exponentiation (^)")
    print("3. Square Root (√)")
    print("4. Factorial (!)")
    print("5. Trigonometric Functions (sin, cos, tan)")
    print("6. Logarithm (log)")
    print("7. Exit")

    while True:
        choice = input("Enter choice (1-7): ")

        if choice == '7':
            print("Exiting the calculator.")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                if choice in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = power(num1, num2)
                elif choice == '3':
                    result = square_root(num1)
                elif choice == '4':
                    result = factorial(num1)
                elif choice == '5':
                    angle = float(input("Enter angle in degrees: "))
                    if angle.is_integer():
                        angle = int(angle)
                    if angle % 90 == 0 and (angle // 90) % 2 == 1:
                        print("Invalid input for tangent. Exiting.")
                        return
                    result = sin(angle)
                elif choice == '6':
                    base = float(input("Enter logarithm base: "))
                    if base <= 0 or base == 1:
                        print("Invalid input for logarithm base. Exiting.")
                        return
                    num1 = float(input("Enter number: "))
                    result = log(num1, base)

                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid input. Please enter a valid choice.")


calculate()
