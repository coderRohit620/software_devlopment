from add import Add
from div import Division
from mul import Multiply
from sub import Subtract

class Calculator:
    def compute(self, choice, a, b):
        if choice == "1":
            return Division(a, b).calculate()
        elif choice == "2":
            return Multiply(a, b).calculate()
        elif choice == "3":
            return Subtract(a, b).calculate()
        elif choice == "4":
            return Add(a, b).calculate()
        else:
            return "Invalid choice"

    def run(self):
        print("Press 1 for Division")
        print("Press 2 for Multiplication")
        print("Press 3 for Subtraction")
        print("Press 4 for Addition")
        
        choice = input("Enter your choice: ")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        print("Result:", self.compute(choice, a, b))

# Run the calculator
calc = Calculator()
while True:
    calc.run()