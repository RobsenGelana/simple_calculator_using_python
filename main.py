from art import logo

#print(logo)

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
    if input("If you want to continue with the operation Type yes or no").lower() == 'yes':
        operator = input("Enter operator: ")
        num3 = int(input("Enter a number to continue: "))
        calculation = operations[operator]
        second_answer = calculation(first_answer, num3)
        print(f"{first_answer} {operator} {num3} = {second_answer}")

    else:
        end_program = False
    #Test Code 

