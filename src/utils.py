"""
Utility functions for the calculator application.
"""


def is_number(value):
    """
    Check if a value can be converted to a number.

    Args:
        value: The value to check

    Returns:
        bool: True if the value can be converted to a number, False otherwise
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def format_result(result, decimal_places=2):
    """
    Format a number to a specified number of decimal places.

    Args:
        result: The number to format
        decimal_places: Number of decimal places (default: 2)

    Returns:
        str: The formatted number as a string
    """
    if not is_number(result):
        return str(result)

    format_string = f"{{:.{decimal_places}f}}"
    formatted = format_string.format(float(result))

    # Remove trailing zeros after decimal point
    if '.' in formatted:
        formatted = formatted.rstrip('0').rstrip('.')

    return formatted