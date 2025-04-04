def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except TypeError:
        print("Error: Invalid types - both arguments must be numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test cases
safe_divide(10, 2)      # Valid division
safe_divide(10, 0)      # ZeroDivisionError
safe_divide("10", 2)    # TypeError
safe_divide(10, "2")   # TypeError