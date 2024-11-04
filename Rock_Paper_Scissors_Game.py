import random
def get_choice():
    player_choice = input('choose rock, paper or scissors: ')
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player} computer chose {computer} ")
    if player == computer:
        return "Its a tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock! You lose"
        else:
            return "Rock beats scissors! You win!"
    elif player == "paper":
        if computer == "scissors":
            return "scissors beat paper! You lose."
        else:
            return "paper beats rock! You win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissors cuts paper! You win!"


choices = get_choice()
result = check_win(choices["player"],choices["computer"])
print(result)
print('The end')
