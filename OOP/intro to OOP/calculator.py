class Calculator:
    def __init__(self, result=0):
        # TODO: Initialize the result attribute to 0
        self.result = result
        
    def add(self, number):
        # TODO: Add the number to result and return the new result
        self.result += number
        return self.result
    
    def subtract(self, number):
        # TODO: Subtract the number from result and return the new result
        self.result -= number
        return self.result
    
    def multiply(self, number):
        # TODO: Multiply result by the number and return the new result
        self.result *= number
        return self.result
    
    def divide(self, number):
        # TODO:
        # Check if number is 0
        # If it is, print error message and return unchanged result
        # Otherwise, divide result by the number and return the new result
        if number == 0:
          print(f"Initial Value: {self.result}\nError: Division by zero\nResult after division by zero: {self.result}")
          return f"Value unchanged: {self.result}"
        else:
          self.result /= number
          return self.result
    
    def clear(self):
        # TODO: Reset result to 0 and return it
        self.result = 0
        return self.result

    
    def get_result(self):
        # TODO: Return the current value of result
        return self.result
