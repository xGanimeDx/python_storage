print("Welcome to my computer quiz!")
# TODO: while loop for iterating during all questions
#       store question in some data structure (dictionary) or in file (json)

playing = input("Do you want to play? \n")
if playing.lower() != "yes":
    quit()

score = 0

answer = input("What does CPU stand for?\n")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?\n")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?\n")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for?\n")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You answered on ", score, " questions")
print("You answered ", (score/4) * 100, "%")