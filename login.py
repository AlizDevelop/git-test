while True:
    user_input = input("Enter a command (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    else:
        print(f"You entered: {user_input}")