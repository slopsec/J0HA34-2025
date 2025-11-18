
# Grading program
# Display a café menu

print("What would you like?")
print("""1 - Coffee - £2.50
2 - Tea - £1.80
3 - Cake - £3.00
""")

choice = int(input("Make choice:"))

# Match - will check choices
match choice:
    case 1:
        print("Here your coffee.")
    case 2:
        print("Here is your tea.")
    case 3:
        print("Here is your cake.")
    case _:   # Default case
        print("Sorry, I cannot understand what you want!")
