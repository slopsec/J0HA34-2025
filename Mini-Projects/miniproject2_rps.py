# Basic rock paper scissors


def determine_winner(user_choice):

    '''
    How are we going to solve this?
    '''

    pass

def get_input():
    print("Welcome to R,P,S")

    choice = 0
    
    while choice <1 or choice >3:
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")

        choice = int(input("Make your selection: "))

    return choice

def main():
    user_score = 0
    computer_score = 0

    # Get input
    user_move = get_input()



if __name__ == "__main__":
    main()