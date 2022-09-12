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


operations = {
    '+': add,
    '-': subtraction,
    '/': divide,
    '*': multiply,
}