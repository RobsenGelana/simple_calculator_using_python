from art import logo

#creating a function for the operations

#addition
def add(number1, number2):
    return number1 + number2

#Subtraction
def subtraction(number1, number2):
    return number1 - number2


#division
def divide(number1, number2):
    return number1 / number2

#multiplication
def multiply(number1, number2):
    return number1 * number2

#create a dictionary
operations = {
    '+': add,
    '-': subtraction,
    '/': divide,
    '*': multiply,
}

def calculator():
    print(logo)
    num1 = int(input("Enter a number: "))
    for operator in operations:
        print(operator)
    end_program = True 
    while end_program:
        operator = input("Enter operator: ")
        num2 = int(input("Enter a second number: "))

        calculation = operations[operator]
        first_answer = calculation(num1, num2)

        #Test code
        print(f"{num1} {operator} {num2} = {first_answer}")

        # Asking the user if they want to continue with the calculation
        user_input = input(f"If you want to continue with {first_answer} the operation Type yes or no: ").lower()
        if  user_input == 'yes':
            num1 = first_answer
        elif user_input == 'q':
            break
        else:
            end_program = False
            calculator()
calculator()
