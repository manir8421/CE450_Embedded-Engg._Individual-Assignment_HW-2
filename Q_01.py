

def abndnt(x):

    for input in range(1, int(x ** 0.5) + 1):         # oop iterates through numbers starting from 1, It's used to find the divisors of x
        if x % input == 0:                            # checks if x is divisible by the current number
            if input * input == x:                    # checking i is the square root of x
                print(f"{input} * {input}")
            else:
                print(f"{input} * {x // input}")

    
    divisors = set()                                  # an empty set named divisors to store all unique divisors
    for m in range(1, int(x ** 0.5) + 1):             # iterating through potential divisors to populate the divisors set
        if x % m == 0:                                # Checks if m is a divisor of x 
            divisors.add(m)                           # Adds m to the divisors set
            if m * m != x:                            # checking square root
                divisors.add(x // m)                  # Adds divisor to the set

    sum_of_divisors = sum(divisors) - x               # Calculation sum of divisors

    return sum_of_divisors > x                        # Checking sum divisors is greater than x


while True:                                           # start the loop and run until choose no(n) to exit

    input_number = int(input("\nEnter a positive integer: "))   # input from keyboard for integer value

    if input_number > 0:                              # checking the input is positive integer or not
        result = abndnt(input_number)
        print("Result is: ", result)
    else:
        print("Invalid input! Type a integer greater than 0.")
    
    continue_input = input("\nWould you like to check another number? (y/n): ").lower()  # ask user to input again/not
    if continue_input != 'y':
        break                                         # Exit the loop
