from art import logo


def add(num1, num2):
    """returns Addition of two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """returns Subtraction of two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """returns Multiplication of two numbers"""
    return num1 * num2


def divide(num1, num2):
    """returns Division of two numbers"""
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("Enter 1st number: "))
    
    for key in operations.keys():
        print(key)
    
    should_continue = True

    # continue with previous result if user type 'y', start new calculation if user type 'n' otherwise exit.
    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("Enter next number: "))
        answer = operations[operation](num1=num1, num2=num2)

        print(f"{num1} {operation} {num2} = {answer}")
        
        new_calc = input(f"Type 'y' continue with {answer}, or type 'n' to start new calculation."
                         + " Type any other key to stop: ").lower()

        if new_calc == "y":
            num1 = answer
        elif new_calc == "n":
            should_continue = False
            calculator()
        else:
            print("Thank you for using calculator")
            break


if __name__ == "__main__":
    calculator()
