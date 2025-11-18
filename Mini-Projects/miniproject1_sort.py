# Mini-project 1
# Sorting a sentence: alphabetically, by word length

# display a list of tokens
def display_tokens(token_array):
    for token in token_array:
        print(token, end=" ")
    print()

# len sort
# receive an array of tokens
def len_sort(token_array):
    pass

# Alphabetical sort
# receive an array of tokens
def sort_alphabet(token_array):
    # Implementing a bubble sort
    # No adaptation needed for type
    length = len(token_array)

    # Outer loop
    for i in range(length - 1):
        sorted = True
        # Inner loop -> doing the swaps
        for j in range(length - 1 - i):
            # If necessary, swap and flag as unsorted
            if token_array[j] > token_array[j+1]:
                token_array[j], token_array[j+1] = token_array[j+1], token_array[j]
                sorted = False
        
        if sorted: break

    display_tokens(token_array)
    

# Tokenising function
# receives a string
# returns an array of substrings
def tokenise(content):
    # Turn to lower case and tokenize
    content = content.lower()
    tokens = content.split()
    # Clean up
    for index in range(len(tokens)):
        temp = tokens[index]
        tokens[index] = temp.strip(" \n\t;:,.!")
    return tokens

# Input and validate (returns string)
def input_validate():
    # Input text and validate: string must not be empty or digits
    text = input("Please type in some text (several words)")
    while text=="" or text.isnumeric():
        print("Invalid entry")
        text = input("Please type in some text (several words)")
    
    return text

def main():

    main_text = input_validate()
    token_list = tokenise(main_text)
    sort_alphabet(token_list)

    # Just for testing
    print(token_list)


# Module guard code
if __name__ == "__main__":
    main()
