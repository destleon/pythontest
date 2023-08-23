while True:                         #a way to create a loop that continues running forever, or until you explicitly tell it to stop
    number_1 = input("What is the first number? Type 'done' to exit: ")

    if number_1 == "done":
        break  # Exit the loop if the user types "done"

    number_1 = int(number_1)  # Convert the input to an integer

    number_2 = int(input("What is the second number? "))
    operator = input("What operation would you like to perform? Type +, -, /, *: ")

    addition = number_1 + number_2
    multiplication = number_1 * number_2
    subtraction = number_1 - number_2
    division = number_1 / number_2

    if operator == "+":
        print(number_1, "+", number_2, "=", addition)
    elif operator == "-":
        print(number_1, "-", number_2, "=", subtraction)
    elif operator == "/":
        print(number_1, "/", number_2, "=", division)
    elif operator == "*":
        print(number_1, "x", number_2, "=", multiplication)
    else:
        print("Invalid operator")

