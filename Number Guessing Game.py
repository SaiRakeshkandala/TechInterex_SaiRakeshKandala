import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    
    # Step 1: Set the range and generate a random number
    lower_bound = 1
    upper_bound = 100
    target_number = random.randint(lower_bound, upper_bound)
    
    # Step 6: Initialize the attempt counter
    attempts = 0
    5
    while True:
        # Step 3: Take player input
        try:
            guess = int(input(f"Enter your guess ({lower_bound}-{upper_bound}): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # Increment the attempts counter
        attempts += 1
        
        # Step 4: Compare guess to target number
        if guess < target_number:
            print("Too low, try again!")
        elif guess > target_number:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break

    # Step 7: Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing! Goodbye.")

# Start the game
play_game()
