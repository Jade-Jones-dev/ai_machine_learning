name = input("Type your name: ")
print("Welcome", name, "to your adventure.")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. What way do you want to go? "
).lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim thought it. Type walk to walk around or swim to swim through it: ")
    if answer == "swim":
        print("You swam across and were eaten by a alligator")
    elif answer == "walk":
        print(" You walked for many miles ran out of water and you lost the game")
    else:
        print("You didn't give a valid response you lose!")

elif answer == "right":
    answer = input("you come to a bridge. It looks wobbly do you want to walk across it or head back? type walk to walk over it and head to head back: ")
    if answer == "walk":
        answer = input("You cross the bridge and meet a stranger do you talk to them? yes, no? ")
        if answer == "yes":
            print("You talk to the stranger and they gave you gold. You win")

        elif answer == "no":
            print("You lose")
        else:
            print("You didn't give a valid response you lose!")
    elif answer == "head":
        print("You got attacked walking back you lose")
    else:
        print("You didn't give a valid response you lose!")

else:
    print("You didn't give a valid response you lose!")

print("Thankyou for trying the game", name)