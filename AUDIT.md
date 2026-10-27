# Project Audit

This audit describes the current Python implementation in `factorial.py`.

| Check | Status | Notes |
|---|---|---|
| Calculates factorial | Yes | Uses repeated multiplication in a loop. |
| Accepts user input | Yes | Reads an integer from the terminal. |
| Handles zero | Yes | Returns `1`, consistent with `0! = 1`. |
| Rejects negative numbers | Yes | Prints a message and stops. |
| Handles non-integer input | Yes | Catches `ValueError` and prints a helpful message. |
| Requires Python 3 | Yes | Uses standard Python syntax and f-strings. |
| Requires external libraries | No | Only the Python standard library is used. |
| Includes a license | No | No license file is included. |

## Verification Examples
- Input `5` should print `Factorial of 5 = 120`.
- Input `0` should print `Factorial of 0 = 1`.
- Input `-2` should report that factorial is not defined for negative numbers.
- Input `hello` should report that a whole number is required.
