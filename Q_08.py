

def cyc(g1, g2, g3):                      # define cyc function, which functions g1, g2, and g3 as arguments
    def apply_functions(n):                 # Inside cyc, define another function apply_function take an integer n
        def apply_to_x(x):                  # apply_functions, define a nested function apply_to_x take value x. This function apply the cycle g1, g2, and g3 to x, n times
            result = x
            for _ in range(n):              # Starts loop for n times,functions in a cyclic order to result
                if _ % 3 == 0:
                    result = g1(result)
                elif _ % 3 == 1:
                    result = g2(result)
                else:
                    result = g3(result)
            return result
        return apply_to_x
    return apply_functions

# Define the functions
def add_one(x):         # Define mathematical functions to used in the cycle: add_one adds 1 to its input.
    return x + 1

def times_two(x):       # Define mathematical functions to used in the cycle: times_two multiplies to its input
    return x * 2

def add_three(x):       # Define mathematical functions to used in the cycle: add_three adds 3 to its input
    return x + 3

def get_input():        # Define function to user for input from keyboard
    n = int(input("\nNumber of times the cycle of functions will be applied 'n'\t: "))
    x = int(input("Type from keyboard for an input integer value for 'x'\t\t: "))
    return n, x

def run_code():         # collect user input by get_input(), sets up the cycle of functions, and apply it to x n times and print result.
    n, x = get_input()
    my_cyc = cyc(add_one, times_two, add_three)
    h = my_cyc(n)
    result = h(x)
    print("Result is:", result)

while True:           # loop for ask user to run the code again or not
    run_code()
    choice = input("\nWant to run the code again? (y/n): ")
    if choice.lower() != "y":
        break
