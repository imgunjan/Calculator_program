# Building a calculator using function and return value
from art import logo


# Crating a function that can add subtract muntiply and divide


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operatoions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# Creating a function name calculator


def calculator():
    print(logo)
    num1 = float(input("enter the first number :"))

    for symbol in operatoions:
        print(symbol)
    # creating the flag
    should_continue = True

    while should_continue:
        operatoions_symbol = input("pick an operation from the line above :")
        num2 = float(input("enter the next number number :"))
        calc_function = operatoions[operatoions_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operatoions_symbol} {num2} = {answer}")

        if input(f"press 'y ' to continue with the {answer} , or type 'n' for exit and start a new .") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
