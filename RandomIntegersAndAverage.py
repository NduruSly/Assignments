import random

numbers = [random.randint(1, 100) for _ in range(10)]
average = sum(numbers) / len(numbers)
print(f"Numbers: {numbers}\nAverage: {average}")