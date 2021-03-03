def calculate(num_1, num_2, operation):
    if operation not in ["+", "-", "/", "*", "mod", "pow", "div"]:
        return "incorrect operation"
    elif operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "pow":
        return num_1 ** num_2
    if num_2 != 0:
        if operation == "/":
            return num_1 / num_2
        elif operation == "mod":
            return num_1 % num_2
        elif operation == "div":
            return num_1 // num_2
    else:
        return "Division by 0!"


print(calculate(float(input()), float(input()), input()))
