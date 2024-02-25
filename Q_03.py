def adder(f1, f2):                          # higher-order function that takes two functions f1 and f2 as arguments.

    def added_function(x):                  # Inside adder, define another function added_function with argument x
        return f1(x) + f2(x)                # added_function return the sum of results applying f1 and f2 to x
    return added_function                   # adder returns added_function,creating new function that sum of f1(x) and f2(x).

def identity(n):                            # Define simple function 'identity' return the same input of its argument n
    return n

def square(n):                              # Define function square that returns the square of its argument n
    return n ** 2

def calc(m):                                # Define function calc that takes a function m as its argument
    try:
        x = int(input("\nType a value for 'x'\t: "))
        result = m(x)                       # function m to x and stores the result in result
        print(f"Result is\t\t: {result}")
    except ValueError:
        print("Invalid input! Type a valid integer.")

# Create functions from adder
a1 = adder(identity, square)                # function a1 that adds the result of identity(x) and square(x)
a2 = adder(a1, identity)                    # function a2 that adds the result of a1(x) and identity(x)
a3 = adder(a1, a2)                          # function a3 that adds the result of a1(x) and a2(x)

# start loop for which ask user to choose an operation
while True:
    choice = input("\nSelect an option from below:"
                   "\n1. a1 (identity + square)"
                   "\n2. a2 (a1 + identity)"
                   "\n3. a3 (a1 + a2)"
                   "\n4. Exit\nYour selection is: ")
    
    if choice == '1':
        calc(a1)
    elif choice == '2':
        calc(a2)
    elif choice == '3':
        calc(a3)
    elif choice == '4':
        print("\nExit the program.")
        break
    else:
        print("\nInvalid input! Type from the provided options.")
