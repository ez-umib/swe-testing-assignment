swe-testing-assignment

swe-testing-assignment is a simple calculator project built with Python. It includes a Calculator class for basic math operations, automated tests with pytest, and a graphical user interface (GUI) using Tkinter.

Features

Basic operations: add, subtract, multiply, divide

Handles errors like division by zero

clear() function to reset the current result

Simple and intuitive GUI with numeric and operation buttons

Automated tests to ensure correct functionality

Installation

Make sure you have Python ≥ 3.7 installed.

Clone the project:

git clone <repository-url>

Navigate to the project folder:

cd swe-testing-assignment

Install pytest (if not already installed):

pip install pytest
Running the Calculator
GUI Version
python3 -m app.gui

Opens the calculator window.

Use the buttons for numbers and operations.

C clears the display, = calculates the result.

Python Usage (CLI)
from app.calculator import Calculator

calc = Calculator()

print(calc.add(5,3))        # 8
print(calc.subtract(10,4))  # 6
print(calc.multiply(6,7))   # 42
print(calc.divide(8,2))     # 4
Running Tests

Run all tests with:

pytest

Tests cover:

Adding positive and negative numbers

Division with decimal numbers

ValueError when dividing by zero

Operations with very large numbers

Notes

The divide function raises a ValueError if attempting to divide by zero.

The GUI uses eval() for quick calculations, so avoid unsafe external inputs.

clear() only resets the current result; it does not delete the Calculator object.