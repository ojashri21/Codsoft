import random

print("Rock, Paper, Scissors")

userscore = 0
computerscore = 0

while True:
    print("\nChoose : rock, paper, scissors")
    userchoice = input("Enter your choice: ").lower()
    computerchoice = random.choice(["rock", "paper", "scissors"])

    if userchoice == computerchoice:
        print("It's a tie!")
    elif userchoice == "rock":
        if computerchoice == "scissors":
            print("You win! rock beats scissors")
            userscore += 1
        else:
            print("You lose! paper beats rock")
            computerscore += 1
    elif userchoice == "paper":
        if computerchoice == "rock":
            print("You win! paper beats rock")
            userscore += 1
        else:
            print("You lose! scissors beats paper")
            computerscore += 1
    elif userchoice == "scissors":
        if computerchoice == "paper":
            print("You win! scissors beats paper")
            userscore += 1
        else:
            print("You lose! rock beats scissors")
            computerscore += 1
    else:
        print("Invalid choice! Please type rock, paper, or scissors.")

    print("Your score:", userscore, "Computer:", computerscore)

    playagain = input("Play again? (yes/no): ").lower()
    if playagain != "yes":
        print("\nFinal Score -> You:", userscore, " Computer:", computerscore)
        print("Thanks for playing! 👋")
        break