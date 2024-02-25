def intscts(f, x):                  # define higher-order function intscts that takes a function f and a value x

    def funct(m):                   # define another function funct that take single function m as parameter.
        return f(x) == m(x)         # funct returns True if applying f to x the same result as applying m to x
    return funct

def square(n):
    return n * n

def triple(n):
    return n * 3

def increment(n):
    return n + 1

def identity(n):
    return n

def get_function_from_choice(choice):  # This function ask user input to the corresponding function

    operations = {
        'square': square,
        'triple': triple,
        'increment': increment,
        'identity': identity
    }
    return operations.get(choice, lambda n: n) # returns the function with choice or lambda function returns its input if choice not found in dictionary

while True:                            # infinite loop to allowing user interaction until exit
    try:
        x = int(input("Type the value for 'x': "))
        sel_fun1 = input("Type the first function (square/triple/increment/identity): ").lower()
        f = get_function_from_choice(sel_fun1)
        
        fun_comp = intscts(f, x)       # comparison function using the chosen f and input x
        
        sel_fun2 = input("Type the second function for comparison (square/triple/increment/identity): ").lower()
        result = get_function_from_choice(sel_fun2)
        
        print("Result is: ", fun_comp(result))
        
    except ValueError:
        print("Invalid input! Type a valid integer for 'x'.")
        continue

    user_sel = input("\nWant to try another comparison? (y/n): ").lower()
    if user_sel != 'y':
        print("\nExit the program...")
        break
