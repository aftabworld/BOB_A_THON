# Program to check if a number is even

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

# Get input from user
num = int(input("Enter a number: "))

# Check if the number is even
if is_even(num):
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Made with Bob
