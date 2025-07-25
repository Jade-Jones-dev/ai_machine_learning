print("Welcome to my computer quiz")

playing = input('Do you want to play? ')

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")

score = 0

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score +=1
else:
    print("Incorrect!")

answer = input("What does gpu stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct")
    score +=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score +=1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct")
    score +=1
else:
    print("Incorrect!")

print("Your score is " + str(score))

