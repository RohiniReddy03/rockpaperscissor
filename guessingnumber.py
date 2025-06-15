def guess_game():
    number_to_guess = 42  # Fixed number
    print("Guess the number between 1 and 100! You have 5 tries.")

    for attempt in range(5):
        guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))

        if guess == number_to_guess:
            print("Correct! You win!")
            return
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Sorry, you're out of tries. The number was {number_to_guess}")

# Call the function to start the game
guess_game()

            