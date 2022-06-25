import random

def play():


    user = input("what\'s your move? 'r' for rock, 's' for sicssors, 'p' for paper: \n")
    computer = random.choice(['r','p','s'])
    print(computer)
    if (user == computer):
        return "It\'s a tie!"

    if is_win(user, computer):
        return "You win!"
    
    return "You lost!"
# r>s, s>p, p>r
def is_win(player, oponent):
    if(player == 'r' and oponent== 's') or (player == 's' and oponent == 'p')\
        or (player =='p' and oponent== 'r'):

        return True   

print(play())