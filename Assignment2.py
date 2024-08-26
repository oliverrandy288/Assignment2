# Task 1: Code Correction (Decisions at the Crossroad)

print("Task 1: Code Correction")
number = int(input("Enter a number: "))  # Convert input to integer

if number > 0:
    print("The number is positive.")
elif number == 0:  # Use '==' for comparison
    print("The number is zero.")
else:  # 'else' does not need a condition
    print("The number is negative.")

print("\n")  # New line for separation

# Task 2: Identify the Greatest and Smallest (The Greatest Showdown)

print("Task 2: Identify the Greatest and Smallest")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Finding the greatest number
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

# Finding the smallest number
smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

print(f"The smallest number is {smallest}. The largest number is {largest}.")

print("\n")  # New line for separation

# Task 3: Leap Year Checker (Leap Year Explorer)

print("Task 3: Leap Year Checker")
year = int(input("Enter a year: "))

# Checking if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
