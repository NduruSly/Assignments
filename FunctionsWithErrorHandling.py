def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both values must be numbers.")
    return None

print(divide_numbers(10, 2))
print(divide_numbers(5, 0))