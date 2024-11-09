import random

def number_guessing_game():
    # Welcome message
    print("\n=== Welcome to the Number Guessing Game! ===")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")

    # Generate the random number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get player's guess
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            
            # Validate the guess is in range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                attempts -= 1
                continue
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You've guessed the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1
            continue

# Run the game
if __name__ == "__main__":
    number_guessing_game() 