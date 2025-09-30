from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_dict = {"+": add, "-": sub, "*": multiply, "/": divide,}

# math = True
# while math:
#     number1 = int(input("Whats the first number bruv: "))
#
#     continuing = True
#     while continuing:
#
#         for symbol in math_dict:
#             print(symbol)
#         operator = input("What operator do you want m8? ")
#         number2 = int(input("Whats the next number bruv: "))
#
#         result = math_dict[operator](number1, number2)
#         print(result)
#
#         cont = input(f"Do you want to continue with {result} or restart? Y/N").lower()
#         if cont == "y":
#             continuing = True
#             number1 = result
#         elif cont == "n":
#             continuing = False
#         else:
#             break

def calculator():
    number1 = int(input("Whats the first number bruv: "))
    continuing = True
    while continuing:

        for symbol in math_dict:
            print(symbol)
        operator = input("What operator do you want m8? ")
        number2 = int(input("Whats the next number bruv: "))

        result = math_dict[operator](number1, number2)
        print(result)

        cont = input(f"Do you want to continue with {result} or restart? Y/N").lower()
        if cont == "y":
            continuing = True
            number1 = result
        elif cont == "n":
            continuing = False
            calculator()
        else:
            break

calculator()
