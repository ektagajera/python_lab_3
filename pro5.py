class Calculator:
    def __init__(self):
        # Private attributes
        self._value1 = 0
        self._value2 = 0

    def set_values(self, value1, value2):
        """Public method to set values for calculation."""
        self._value1 = value1
        self._value2 = value2

    def get_values(self):
        """Public method to get values for calculation."""
        return self._value1, self._value2

    def add(self):
        """Public method to perform addition."""
        return self._value1 + self._value2

    def subtract(self):
        """Public method to perform subtraction."""
        return self._value1 - self._value2

    def display_results(self):
        """Public method to display results of operations."""
        print("Values: ", self.get_values())
        print("Addition: ", self.add())
        print("Subtraction: ", self.subtract())

# Create an instance of Calculator
calc = Calculator()

# Set values
calc.set_values(10, 5)

# Display results
calc.display_results()
