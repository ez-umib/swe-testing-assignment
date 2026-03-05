Testing - swe-testing-assignment

This document explains the automated tests for the Calculator project and what each test covers.

Test Coverage

The tests include:

Test Name	Description
test_add	Tests addition of positive and negative numbers
test_subtract	Tests subtraction, including negative numbers
test_multiply	Tests multiplication of normal and large numbers
test_divide	Tests division with integers and decimals
test_divide_by_zero	Checks that dividing by zero raises ValueError
test_negative_numbers	Ensures addition works with negative inputs
test_decimal_numbers	Ensures division works with decimal numbers
test_large_numbers	Ensures multiplication works with very large numbers
Example Test Run
(.venv) $ pytest
================================================= test session starts =================================================
collected 8 items                                                                                                   

tests/test_calculator.py ........                                                                              [100%]

================================================== 8 passed in 0.12s =================================================

All tests passing indicates that the Calculator class functions correctly.

Notes

Tests assume a fresh Calculator instance for each test.

clear() is tested to ensure it resets the current value to 0.

Any errors like division by zero are correctly raised and caught in tests.