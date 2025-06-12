print("Welcome to my computer game")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()
    
print("Okay, let's play")

answer = input("What does CPU stand for?: ")
if answer.lower() == "central processing unit":
    print("That's correct!")
    score += 1
else:
    print("try again!")
    
answer = input("What does RAM stand for?: ")
if answer.lower() == "random access memory":
    print("That's correct!")
    score += 1
else:
    print("try again!")
    
answer = input("What does DB stand for?: ")
if answer.lower() == "database":
    print("That's correct!")
    score += 1
else:
    print("try again!")
    
answer = input("What does GPU stand for?: ")
if answer.lower() == "graphics process unit":
    print("That's correct!")
    score += 1
else:
    print("try again!")
    
answer = input("What does PSU stand for?: ")
if answer.lower() == "power supply unit":
    print("That's correct!")
    score += 1
else:
    print("try again!")
    
answer = input("What does LOL stand for?: ")
if answer.lower() == "laugh out loud":
    print("That's correct!")
    score += 1
else:
    print("try again!")
    
    
total_score = print("You answered " + str(score) + " questions correct!") 