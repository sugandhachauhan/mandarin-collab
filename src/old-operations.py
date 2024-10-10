'''
This is an older version of the code in operations.py
and it could be deleted but we haven't done it because
we were not using version control a year ago.
'''
#creating a function named 'sum' to return the sum of two input variables received as arguments
def sum(a, b):
    return a + b

#creating a function named 'sub' to return the difference of two input variables received as arguments
def sub(a, b):
    return a - b
#creating function named 'div' to return the product of division of two variables
def div(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")
#creating function to return the product of multiplication of two variables
def mult(a, b):
    return a * b 
