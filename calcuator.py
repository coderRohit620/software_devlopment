# calculator.py
from add import Add
from div import Division
from mul import Multiply
from sub import Subtract

class Calculator:
    def compute(self, choice, a, b):
        if choice == "1":
            return Add(a, b).calculate()
        elif choice == "2":
            return Subtract(a, b).calculate()
        elif choice == "3":
            return Multiply(a, b).calculate()
        elif choice == "4":
            return Division(a, b).calculate()
        else:
            return "Invalid choice"

    def run(self):
        while True:
            print("Press 1 for Addition")
            print("Press 2 for Subtraction")
            print("Press 3 for Multiplication")
            print("Press 4 for Division")
            print("Press 5 to Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "5":
                print("Exiting the calculator. Goodbye!")
                break
            
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            print("Result:", self.compute(choice, a, b))

# Run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()