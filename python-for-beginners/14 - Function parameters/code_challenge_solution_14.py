# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'. The default operation is 'add'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function using named notation passing in only the numbers 6 and 4
# Should return 10
#
# Test your function using named notation with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

def calculator(first_number, second_number, operation='add'):
    if operation == 'add':
        answer = first_number + second_number
    elif operation == 'subtract':
        answer = first_number - second_number
    elif operation == 'divide':
        answer = first_number / second_number
    return answer

first_number = float(input('Please enter a number: '))
second_number = float(input('Please enter another number: '))
operation = input('Please enter an operation: ').lower()

answer = calculator(first_number, second_number, operation)
print(answer)

