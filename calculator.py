class Calculator:
    """
    Calculator
    A utility class providing static methods for basic arithmetic operations.
    Methods
    -------
    calculate_sum(a, b):
        Returns the sum of a and b.
    calculate_difference(a, b):
        Returns the difference between a and b.
    calculate_product(a, b):
        Returns the product of a and b.
    calculate_quotient(a, b):
        Returns the quotient of a divided by b. If b is zero, returns an error message.
    calculate_percentage(a, b):
        Returns the percentage value of a with respect to b, calculated as (a / b) * 100.
    """
    @staticmethod
    def calculate_sum(a, b):
        return a + b  # Fixed: should be addition

    @staticmethod
    def calculate_difference(a, b):
        return a - b

    @staticmethod
    def calculate_product(a, b):
        return a * b

    @staticmethod
    def calculate_quotient(a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

    @staticmethod
    def calculate_percentage(a, b):
        if b == 0:
            return "Error! Division by zero."
        return (a / b) * 100  # Fixed: correct percentage calculation
