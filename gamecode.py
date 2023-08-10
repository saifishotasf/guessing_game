import random

def guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guessing Game! Try to guess the number between 1 and 100.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < target_number:
            print("Try higher!")
        elif guess > target_number:
            print("Try lower!")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've reached the maximum number of attempts. The number was {target_number}.")

guessing_game()
