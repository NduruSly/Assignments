names = ["Alice", "Bob", "Charlie"]

# Write to file
with open("names.txt", "w") as file:
    for name in names:
        file.write(f"{name}\n")

# Read from file and print
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())