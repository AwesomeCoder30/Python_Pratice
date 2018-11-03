import random

def play():
    player_a = input("Enter Rock, Paper, Scissors (R, P, S): ")
    player_b = random.choice(["R", "P", "S"])
    print("Computer Choose: ", player_b)

    # Game
    score = 0
    if player_a == player_b:
        score = 0.5

    # R > S
    elif player_a == "R" and player_b == "S":
        score = 1

    # S > P
    elif player_a == "S" and player_b == "P":
        score = 1
    # P > R
    elif player_a == "P" and player_b == "R":
        score = 1
    return score

# Ask a input for how many games to play
times = input("how many time to play? ")
times = int(times)

# Play that many games vs. the computer
score = 0
for game in range(times):
    score = score + play()

print("My Score", score)
