# Mini-project 1
# Sorting a sentence: alphabetically, by word length

# display a list of tokens
def display_tokens(token_array):
    pass

# len sort
# receive an array of tokens
def len_sort(token_array):
    pass

# Alphabetical sort
# receive an array of tokens
def sort_alphabet(token_array):
    pass

# Tokenising function
# receives a string
# returns an array of substrings
def tokenise(content):
    pass

# Input and validate (returns string)
def input_validate():
    # Input text and validate: string must not be empty or digits
    text = input("Please type in some text (several words)")
    while text=="" or text.isnumeric():
        print("Invalid entry")
        text = input("Please type in some text (several words)")
    
    return text

def main():
    # Test code
    main_text = input_validate()

# Module guard code
if __name__ == "__main__":
    main()
