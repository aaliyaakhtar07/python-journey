import random

def game():
    print("You are playing a game...")
    score = random.randint(0, 100)
    #Fetch the highscore from the file
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore == ""):
            highscore = 0
        else:   
            highscore = int(highscore)
    print(f"Your score: {score}")
    print(f"High score: {highscore}")   
    if(score > highscore):
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score
game()