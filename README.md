# swe-testing-assignment

## Project Description
`swe-testing-assignment` is a simple calculator application implemented in Python. It provides basic arithmetic operations: addition, subtraction, multiplication, division, and a clear (C) function to reset the input.  
The project demonstrates professional software testing practices and version control using Git and GitHub, with both unit and integration tests to ensure reliability and correctness.

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/ez-umib/swe-testing-assignment.git
cd swe-testing-assignment

Create a virtual environment (optional but recommended):

python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

(Currently only pytest is required for testing.)

How to Run the Application
python3 -m app.gui

A GUI window will appear with the calculator.

Enter numbers, select operations, and press = to calculate.

Press C to clear the display.

How to Run Tests
pytest

This command runs all unit and integration tests in the tests folder.

Expected output: all tests passed.

Testing Framework Research: Pytest vs Unittest
Feature	Pytest	Unittest
Ease of Use	Simple syntax, less boilerplate	Requires classes and methods
Fixtures / Setup	Powerful @pytest.fixture support	setUp and tearDown methods
Parametrized Tests	Easy to parametrize tests	Requires additional code
Plugins / Extensions	Many community plugins available	Limited plugins
Output & Reporting	Colorful, clear, detailed reports	Basic output

Choice Justification:
We chose Pytest for this project because it allows simpler test writing, better fixtures for setup, parametrized tests, and clear test reports. It is ideal for both unit and integration testing, and it keeps test code concise and readable.


---
