import random
int = ["s", "w", "g"]
print("==============================================")
print("Welcome to the Snake, Water and Gun Game")
print("==============================================")

print("Rules:-", "\nChance=10", "\nMaximum Points Wins")
print("==============================================")

chance = 10
no_of_chance = 0
computer_point = 0
Player_point = 0

print("s for snake", "\nw for water", "\ng for gun")
print("==============================================")

while no_of_chance < chance:
    n = input("Snake,Water,Gun=")
    ran = random.choice(int)

    if n == ran:
        print("Tie No Points to be given ")

    elif n == "s" and ran == "w":
        print("player guess is", n, "computer guess is", ran)
        print("player wins this round")
        Player_point = Player_point+1
        print("player point is ", Player_point)

    elif n == "s" and ran == "g":
        print("player guess is", n, "computer guess is", ran)
        print("computer wins this round")
        computer_point = computer_point+1
        print("computer point is ", computer_point)

    elif n == "w" and ran == "s":
        print("player guess is", n, "computer guess is", ran)
        print("computer wins this round")
        computer_point = computer_point + 1
        print("computer point is ", Player_point)

    elif n == "w" and ran == "g":
        print("player guess is", n, "computer guess is", ran)
        print("player wins this round")
        Player_point = Player_point+1
        print("Player point is ", Player_point)

    elif n == "g" and ran == "w":
        print("player guess is", n, "computer guess is", ran)
        print("computer wins this round")
        computer_point = computer_point+1
        print("computer is ", computer_point)

    elif n == "g" and ran == "s":
        print("player guess is", n, "computer guess is", ran)
        print("Computer wins this round")
        computer_point = computer_point+1
        print("computer is ", computer_point)

    else:
        print("You have wrong input")

    no_of_chance = no_of_chance+1
    print("no_of_chance=", no_of_chance)
    print("==============================================")

print("==============================================")
print("Total points of player =", Player_point)
print("Total points of computer=", computer_point)
print("==============================================")

if Player_point == computer_point:
    print("Tie")
elif Player_point > computer_point:
    print("player won the match")
else:
    print("Computer won the match")
print("==============================================")
print("Game Over")
print("==============================================")
