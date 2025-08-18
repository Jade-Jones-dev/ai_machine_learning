import random

number_to_guess = random.randint(1, 100)
guesses = 0

print("Let's play a game. Guess the number between 1 and 100")

while True:
    guess = input("Enter your guess: ")
    guess = int(guess)
    
    if guess <= 0 or guess > 100:
        print("Your guess must be between 1 and 100")
        quit()

    guesses += 1
    if guess == number_to_guess:
        print("You got it!")
        break
    elif guess > number_to_guess:
        print("Too high...")
    else:
        print("Too low...")

print(f"You got the number {number_to_guess} in {guesses} guesses")



