def factorial(number):
    """Return the factorial of a non-negative integer."""
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


def main():
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return
        print(f"Factorial of {number} = {factorial(number)}")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
