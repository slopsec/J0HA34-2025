''' Revision - the standard algorithms covered at L6/Higher Computing
    - Input validation
    - Find min/max
    - Count occurrences
    - Linear search
'''


# Input validation example (here 0-100 integer)

def input_integer_val(message, low, high):
    score = 0
    try:        # for now just a message
        score = int(input(message))
        while score < low or score > high:
            score = int(input("Incorrect input.", message))
    except ValueError:
        print("You did not enter an integer.")
        # This will be a loop in the future
    
    return score


def main():
    
    # Test input validation
    n = input_integer_val("Enter a student score 0-100", 0, 100)



if __name__ == "__main__":
    main()