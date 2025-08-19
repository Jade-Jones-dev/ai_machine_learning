import random

print("Let's play a game... ")

while True:
    roll_the_dice = input('Do you want to roll? (Y/N): ')
    if roll_the_dice.lower() == 'y':
        print(f'You rolled a {random.randint(1, 6)}')
    else:
        print("Goodbye") 