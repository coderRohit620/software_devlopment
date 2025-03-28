class Remainder:
    def mod_number(a, b):
        return a % b
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))   
    
    remainder_result = mod_number(num1, num2)
    print("Remainder: ", remainder_result)