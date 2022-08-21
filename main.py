def add(a, b):
    pass

def multiply():
    pass

def subtract():
    pass

def divide():
    # use conditionals to check for 0
    if 0:
        return "division by 0"
    pass

# the input params have to be positive integeres only or 0
# the result has to be of type float

numbers = [2, 4, 6, -9, 0, 1, 56, 7, -2, 5]

# dictionary where keys are array indexes, and values are results of operations 
result = {
    "0": [6.0, 8.0, -2.0, .5]
}

for index, number in enumerate(numbers):
    print(index, number)