
from operator import add,neg        # import add and neg function from puthon module

def combine_funcs(op):              # high order function with argument 'op'
    def combined(f, g):             # function with argument f & g (input value x)in the "combine_funcs" function
        def val(x):                 # function with argument x in the 'combined' function
            return op(f(x), g(x))
        return val                  # return the function 'val' from 'combined'
    return combined                 # return the dunction 'combined' from 'combine_fincs'

add_func = combine_funcs(add)       # call 'combine_funcs' function for add function as the argument

h = add_func(abs, neg)              # calls 'add_func' for abs and neg as arguments.
print(h(-5))                        # call the function 'h' with '-5' argument



# Program print at Output: 10
# Reason:
'''1. "abs" function make the absolute value; makes "-5" to "5" '''
'''2. "neg" function make the sign inverse value; makes "-5" to "5" '''
'''3. "h()" function call "combined_funcs()" return the sum of "5" and "5". So that, "5+5 = 10";Output is 10.'''

# code detail:
''' > The combine_funcs() function takes an operator as input and returns a function,
      that combines two other functions using that operator.
    > The add_func function is created by calling combine_funcs(add) with abs and neg as arguments.
    > The h function is created by calling add_func(abs, neg) with argument abs and neg.
    > The print(h(-5)) statement prints the result of calling the h() function with the argument -5.'''