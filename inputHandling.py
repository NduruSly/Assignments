while True:
    try:
        num = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print(f"Valid number entered: {num}")