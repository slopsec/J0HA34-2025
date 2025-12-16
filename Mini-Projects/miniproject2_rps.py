import random
# Basic rock paper scissors


def determine_winner(user_choice):
    ''' By using modulus arithmetic, we can reduce the number of test
    cases to three and treat the choices as mere numbers. (1,2,3)
    In contrast, using match/case or if/else would result in 9 cases (5 with optimisations)
    Or creating objects/dictionaries for each move (with the winning/losing moves) requires
    extra coding.
    '''
    computer_choice = random.randint(1,3)

    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors" }
    # Temp
    print("Computer choice:", choices[computer_choice])

    if user_choice == computer_choice:    # Draw
        return 0
    elif (user_choice+1)%3 == computer_choice%3:
        # We shift user choice by and divide by 3
        # The remainders match when computer wins
        return 1 # For computer
    else:
        return -1 # For user    


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

    replay = True

    while replay is True:
        # Get input
        user_move = get_input()
        winner = determine_winner(user_move)

        # determine output
        if winner == 0:
            print("Draw")
        elif winner == 1:
            print("Computer win.")
            computer_score += 1
        else:
            print("User win.")
            user_score +=1

        print("User:", user_score, " --- Computer:", computer_score)

        wish = input("Play again? (y/n)")

        if wish[0].lower() == "y":
            replay == True
        else:
            replay == False



if __name__ == "__main__":
    main()