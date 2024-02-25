def fancy_prnt(n):

    try:
        upper_limit = int(input("Type upper limit of the range\t: ")) - 1
    except ValueError:
        print("Invalid input! Type a valid integer for the upper limit.")
        return                                                       # Exit if input is invalid

    lower_limit = 0                                                  # Set the lower limit at "0"

    if upper_limit < lower_limit:                                    # Checking the upper limit is valid or invalid
        print("Upper limit must be greater than 0")
        return

    for m in range(lower_limit, upper_limit + 1):
        if m % n == 0:
            print("Buzz!")
        else:
            print(m)

while True:                                                          # start loop for ask Buzz number and upper limit input
    try:
        buzz_number = int(input("\nType the 'Buzz!' number\t\t: "))  # Ask for the 'Buzz!' number
    except ValueError:
        print("Invalid input! Type a valid integer for the 'Buzz!' number.")
        continue
    
    fancy_prnt(buzz_number)

    continue_choice = input("\nWant to try another range? (y/n): ").lower()
    if continue_choice != 'y':
        print("\nExiting the program.")
        break
