import random
def play():
    user=input("Whats your choice? 'r' for rock, 'p' for paper,'s' for scissor\n")
    computer=random.choice(['r','p','s'])
    print('Your choice is',user)
    print('Opponent\'s choice is',computer)

    if user==computer:
        return "It\'s a tie"

    if is_win(user,computer):
        return 'You win'
    return 'You Lose!'



def is_win(player,opponent):
    if((player=="r" and opponent=="s") or (player=="s" and opponent=="p") or(player=="p" and opponent=="r")):
        return True
    
print(play())



















#copyrights to @pranithamdevarakonda
