

def smth(g, dx):
    return lambda x: (g(x - dx) + g(x) + g(x + dx)) / 3  # return lambda function with paramenters x and g

square = lambda x: x ** 2                                # define square as a lambda function
result = round(smth(square, 1)(0), 3)
print(f"Output is: {result}")

'''
>>> The smth function aims to smooth the input function g around a point x by taking
    an average of g applied to three points: x - dx, x, and x + dx.
>>> It returns a lambda function that calculates (g(x - dx) + g(x) + g(x + dx)) / 3.
>>> lambda function that takes an input x and returns square (x ** 2).
>>> smth function is called with square as the function of g and 1 as the value of dx.
>>> it returns a new lambda function, when given an x, and calculate (square(x - 1) + square(x) + square(x + 1)) / 3.
>>> The returned lambda function called with x = 0.
>>> Substituting x = 0 into the lambda function's formula, where (square(-1) + square(0) + square(1)) / 3.
>>> Calculating each term: square(-1) = (-1) ** 2 = 1, square(0) = 0 ** 2 = 0, and square(1) = 1 ** 2 = 1.
>>> average of these values is: (1 + 0 + 1) / 3 = 2 / 3.
>>> The result: 2 / 3 = 0.667.
>>> print the Output is: 0.667.
'''