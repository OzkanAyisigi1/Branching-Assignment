# Welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight from user
weight = float(input("Please enter the package weight:\n"))

# Check if package is too heavy
if weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package dimensions from user
width = float(input("Please enter the package width:\n"))
height = float(input("Please enter the package height:\n"))
length = float(input("Please enter the package length:\n"))

# Calculate total dimensions
total_dimensions = width + height + length

# Check if package is too big
if total_dimensions > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping quote
# Formula: (width * height * length * weight) / 100
quote = (width * height * length * weight) / 100

# Display the quote formatted as currency
print(f"Your estimated total for shipping this package is: ${quote:.2f}")
print("Thank you!") 