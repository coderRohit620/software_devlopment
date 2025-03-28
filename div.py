# div.py
class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def calculate(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b