from random import choice

def check(pick):
    player = pick["player"]
    computer = pick["computer"]
    print(f"computer chose {computer.upper()} \nyou chose {player.upper()} \n")
    
    if player.lower() == computer.lower():
        return "TIE !!!!"
    elif player.lower() == "rock" and computer.lower() == "paper":
        return "computer wins!!!"
    elif player.lower() == "paper" and computer.lower() == "scissors":
        return "computer wins!!!"
    elif player.lower() == "scissors" and computer.lower() == "rock":
        return "computer wins !!!"
    else:
        return "player wins"
    

def get_pick():
    player_pick = input("CHOOSE YOUR PICK: ROCK OR PAPPER OR SCISSORS:\n")
    computer_pick = choice(["rock", "paper", "scissors"])
    pick = {"player": player_pick, "computer": computer_pick}
    return check(pick)
    
if __name__ == "__main__":
    result = get_pick()            
    print(result)