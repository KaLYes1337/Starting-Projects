def calculator():
    firstNumber = int(input("Enter number: "))
    secondNumber = int(input("Enter number: "))
    operator = input("Enter operator: + - * /: ")

    if operator == "+":
        print(round(firstNumber + secondNumber, 1))
    elif operator == "-":
        print(round(firstNumber - secondNumber, 1))
    elif operator == "/":
        if secondNumber ==0:
            print("You can not divide by 0")
        else:
            print(round(firstNumber / secondNumber, 1))
    elif operator == "*":
        print(round(firstNumber * secondNumber, 1))


calculator()
