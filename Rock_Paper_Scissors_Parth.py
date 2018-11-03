import random

def play():
    player_a = input("Enter Rock, Paper, or Scissors (R,P,S): ")
    #print("I Choose: ", player_a)
    computer = random.choice(["R", "P", "S"])
    print("Warriors Choose: ", computer)

    score = 0
    if player_a == computer:
        score = 0.5
        print("Tied")
    elif player_a == "R" and computer == "S":
        score = 1
        print("You won a dollar")
    elif player_a == "S" and computer == "P":
        score = 1
        print("You won a dollar")
    elif player_a == "P" and computer == "R":
        score = 1
        print("You won a dollar")
    elif player_a != "R" and player_a != "P" and player_a != "S":
        score = -1
        print("Dismiss")
    else:
         print("Warrior won a dollar")
    return score

times = input("How many games to play? ")
times = int(times)

MyDollars = 0
dismissGame=0
for game in range (times):
    score=play()
    #print(score)
    if(score==-1):
        dismissGame = dismissGame + 1
    else:
        MyDollars = MyDollars + score
    ComputerDollars = times - MyDollars - dismissGame

if MyDollars > ComputerDollars:
    print("You won the game!")
elif MyDollars < ComputerDollars:
    print("Computer won the game.")
elif MyDollars == ComputerDollars:
    print("It is a tie")

