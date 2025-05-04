"""
Simple calculator module with basic arithmetic operations.
"""


class Calculator:
    """
    A simple calculator class for basic arithmetic operations.
    """

    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b

    def divide(self, a, b):
        """
        Divide a by b and return the result.

        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b