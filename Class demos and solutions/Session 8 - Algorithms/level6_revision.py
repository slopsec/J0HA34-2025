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


# Find maximum
# max() can do a similar
# 1. if list is one element, return sole element
# 2. Otherwise put element 1 into temporary variable
# Loop from elt 2 to end
# Replace temporary variable with relevant value if greater
def find_max_level6(some_list):
    # Empty list
    if len(some_list) == 0:
        return None     # nothing to return
    if len(some_list) == 1:
        return some_list[0] # Return only element
    
    temp_max = some_list[0]
    for i in range(1, len(some_list)):
        if some_list[i] > temp_max:
            temp_max = some_list[i]
    
    return temp_max


# Counting occurrences
# You have a list of values
# A search term
# Loop through list and increase counter when search term 
# ecountered
def count_occurrences(some_list, term):
    count = 0
    for current_value in some_list:
        if current_value == some_list:
            count += 1
    
    return count

# Linear search
# Search algorithm on an unsorted collection of data
# Time complexity O(n)
def linear_search(some_list, term):
    # Iterate through list
    for i in range(len(some_list)):
        # if current value matches term return index
        if some_list[i] == term:
            return i
    return None


def main():
    # Test input validation
    # n = input_integer_val("Enter a student score 0-100", 0, 100)
    maximum = find_max_level6([10,20,5,50,30])
    print(maximum)

    names = ["Jim", "Mark", "Arthur", "Lorna", "Aurelien"]
    print(linear_search(names, "Arthur"))
    print(linear_search(names, "Fiona"))


if __name__ == "__main__":
    main()