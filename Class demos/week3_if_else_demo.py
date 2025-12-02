

# Correct answer
answer = "Python"

# Get user input
user_input = input("What is today's subject?")

# if statement
if user_input == answer:
    print("Correct.")

    q2 = input("Do you like it? y/n")

    # The statement below is nested -- 
    # Will be met only if running in this block
    if q2 == "y":
        print("Good for you.")

elif user_input == answer.lower():
    print("Okay but the case is incorrect.")

else:
    print("Incorrect.")

print("Bye.")

