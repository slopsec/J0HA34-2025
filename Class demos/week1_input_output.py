# Task 12: Ask for the user’s first name.
# Display the uppercase version and how many letters are in it.

first_name = input("What's your first name?")

upper_name = first_name.upper()
first_count = len(first_name)
print(f"Your name is {upper_name} and it contains {first_count} letters.")


# Task 13
# We already asked the first name above

last_name = input("And now your last name, please?")
last_count = len(last_name)
total = first_count + last_count

print(f"Your last name has {last_count} letters and your full name has {total}")
