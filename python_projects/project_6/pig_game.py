import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


value = roll()
print(value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("there must be between 2 and 4 players")
    else:
        print("Invalid please try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        current_score = 0

        while True:

            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1 turn done")
                break
            else:
                print("You rolled a:", value)

            print("Your score is:", current_score)
