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
operator = input("Enter operator: ")
num2 = int(input("Enter a second number: "))

calculation = operations[operator]
first_answer = calculation(num1, num2)

#Test code
print(f"{num1} {operator} {num2} = {first_answer}")
