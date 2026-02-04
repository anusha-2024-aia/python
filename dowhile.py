while True:
    # Code to be executed (guaranteed to run at least once)
    user_input = input("Enter a positive number to continue, or a negative number/0 to exit: ")
    number = int(user_input)
    
    print(f"You entered: {number}")

    # Check the condition at the end of the loop body
    if number <= 0:
        break  # Exit the loop if the condition to stop is met

print("Loop terminated.")
