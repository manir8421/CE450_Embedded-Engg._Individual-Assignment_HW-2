
def f():

    return lambda: lambda x: lambda: x

print (f()()(3)())

'''
>>> f() is call the function "f" and return the first lambda function
>>> f()() the first lambda function turn to and return the second lambda function.
>>> f()()(3) the second lambda functinn and calld with argument "3" capture this value as "x" 
    then return to third lambda function.
>>> f()()(3)() the third lambda function called, which returns the value of "x", the value is "3".
'''