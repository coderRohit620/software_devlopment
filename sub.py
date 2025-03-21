class calculator:
    def sub_number(a,b):
        return a-b
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))   

    sub_result = sub_number(num1,num2)
    print("Subtraction: ",sub_result)
