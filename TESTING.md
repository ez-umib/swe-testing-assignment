TESTING.md - swe-testing-assignment

This document explains the automated tests for the Calculator project.

Test Name	Description
test_add	Tests addition of positive and negative numbers
test_subtract	Tests subtraction, including negative numbers
test_multiply	Tests multiplication of normal and large numbers
test_divide	Tests division with integers and decimals
test_divide_by_zero	Checks that dividing by zero raises ValueError
test_negative_numbers	Ensures addition works with negative inputs
test_decimal_numbers	Ensures division works with decimal numbers
test_large_numbers	Ensures multiplication works with very large numbers

Example Run:

(.venv) $ pytest
================================================= test session starts =================================================
collected 8 items                                                                                                   

tests/test_calculator.py ........                                                                              [100%]

================================================== 8 passed in 0.12s =================================================
Test Name	Type	Status
test_add	Unit	Pass
test_subtract	Unit	Pass
test_multiply	Unit	Pass
test_divide	Unit	Pass
test_divide_by_zero	Unit	Pass
test_negative_numbers	Unit	Pass
test_decimal_numbers	Unit	Pass
test_large_numbers	Unit	Pass
test_add_flow	Integration	Pass
test_clear_flow	Integration	Pass

Notes:

Tests assume a fresh Calculator instance for each test.

clear() resets the display/input to 0.

Division by zero raises a ValueError.

Integration tests cover essential GUI interaction flows.