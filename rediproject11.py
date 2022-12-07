#Is a Game in Ghana where a friend is asked questions about you


print("Welcome to it takes two!")

playing = input("Do you want to play? ")




if playing.lower() != "yes":
    quit()

print("Okay! let play: )")
score = 0

answer = input("what is my name? ")
if answer == "kwaku opare":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
   


answer = input("What is my age? ")
if answer.lower() == "i am 30 years old":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

    answer = input(" ")
if answer.lower() == "football":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is my favourite game? ")
if answer.lower() == "football":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Where do I come from? ")
if answer.lower() == "ghana":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is my favorite food? ")
if answer.lower() == "rice and stew":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What is my favorite colour? ")
if answer.lower() == "red":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")





print("You got " + str(score) + "questions correct!")
print("You got " + str((score/4) * 100) + "%.")
