import random

def number_guessing_game():
    print("Welcome to my number guessing game!")
    print("You have to guess the lucky number between 1 and 100.")
    print("If your guess is too low, you will get 'low'.")
    print("If your guess is too high, you will get 'high'.")
    print("If you guess correctly, you win!")

    # Generate a random number between 1 and 100 (lucky number)
    lucky_number = random.randint(1, 100)
    # print(lucky_number)

    # Initialize guess and live (attempts) variables
    guess = -1  # Initializing to an invalid number
    live = 0

    # Start the game loop
    while guess != lucky_number:
        try:
            # Get user input and validate it
            guess = int(input("Enter your guess (a number between 1 and 100): "))
            
            # Check if guess is within valid range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Increment the number of attempts
            live += 1

            # Check if the guess is correct or not
            if guess < lucky_number:
                print("Guess too low!")
            elif guess > lucky_number:
                print("Guess too high!")
            else:
                print(f"Congratulations! You've guessed the lucky number {lucky_number} in {live} attempts.")

            if live >= 7:
                print("Game Over!!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
# Run the game
number_guessing_game()
