import random
while(True):
    try:
        level=int(input("Level: "))
        if level<=0:
            continue
    except :
        pass
    else:
        break

correct_answer=random.randint(0,level)

while(True):
    try:
        guess=int(input("Guess: "))
        if guess<=0:
            continue
        if guess<correct_answer:
            print("Too small!")
        elif guess>correct_answer:
            print("Too large!")
        else:
            print("Just right!")
            break
    except:
        pass