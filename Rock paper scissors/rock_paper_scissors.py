import random

def play():
    ''' Plays one round of the game '''
    user_input = input("'r' for rock, 's' for scissors, 'p' for paper")
    computer_choice = random.choice(['r','s','p'])
    
    def game(user, opponent):
        ''' Determines who wins the game (r>s s>p p>r) '''
        if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'r'):
            print("You win!")
        elif (user == opponent):
            print("It's a draw")
        else:
            print("You lost!! OOps!")
            
    return game(user_input, computer_choice)
    
play()