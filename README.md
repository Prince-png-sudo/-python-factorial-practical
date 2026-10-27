# Python Basics: Factorial Calculator

A beginner-friendly Python program that calculates the factorial of a non-negative integer entered by the user.

## Features
- Accepts a number from the user
- Calculates factorial using a `for` loop
- Handles `0` correctly (`0! = 1`)
- Rejects negative numbers
- Displays a helpful message if the input is not a whole number

## Requirements
- Python 3.x
- No external libraries are required

## How to Run
Open a terminal in this folder and run:

```bash
python factorial.py
```

On some Windows installations, you may need to use:

```bash
py factorial.py
```

## Example

```text
Enter a non-negative integer: 5
Factorial of 5 = 120
```

## How It Works
The program starts the result at `1`, then multiplies it by each integer from `1` through the entered number. For input `0`, the loop does not run and the result remains `1`, which is correct because `0! = 1`.
