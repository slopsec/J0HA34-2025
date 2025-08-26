## Week 1 — Basics (printing, variables, strings, input)
**Reminder:** **LESSON** = follow along and reproduce the code shown. **TRY** = attempt the task yourself; no code is shown.

1. **LESSON — Your first output**
   - **Task:** Create a tiny Python programme that displays a message to the screen.
   - **Code:**
     ```python
     print("My first Python")
     ```

2. **TRY — Two alerts → two lines**
   - **Task:** Write a Python programme that outputs two different messages on separate lines.

3. **LESSON — Storing values in variables**
   - **Task:** Recreate an example that stores a value in a variable and displays it.
   - **Code:**
     ```python
     score = 0
     print(score)
     ```

4. **LESSON — Numbers & basic arithmetic**
   - **Task:** Demonstrate addition, subtraction, multiplication, division, floor division, remainder, and powers.
   - **Code:**
     ```python
     print(5 + 7)     # addition
     print(9 - 3)     # subtraction
     print(4 * 6)     # multiplication
     print(8 / 2)     # division (float)
     print(7 // 3)    # floor division
     print(7 % 3)     # remainder
     print(2 ** 3)    # exponent
     ```

5. **TRY — Use another operator**
   - **Task:** Write a programme that uses one of: `/`, `*`, or `-` to perform a calculation and display the result.

6. **LESSON — Quotation marks and escaping**
   - **Task:** Output text that mixes single and double quotes. Show how to escape characters (e.g., in *isn\'t*).
   - **Code:**
     ```python
     print('She said "hello"')
     print("He said \'it isn\'t fair\'")
     print('He said "it isn\'t fair"')
     print("""Line 1\nLine 2\nLine 3""")
     ```

7. **LESSON — Joining text and f-strings**
   - **Task:** Join a first name and surname using concatenation and an f-string.
   - **Code:**
     ```python
     first = "Johnny"
     last = "Brown"
     print(first + " " + last)               # concatenation
     print(f"Hi {first} {last}")             # f-string
     ```

8. **TRY — Build a message**
   - **Task:** Store a name and a cost in variables and display: `Hi <name>, your total cost is £<cost>`.

9. **LESSON — Reading input & converting types**
   - **Task:** Ask for two whole numbers and output their total.
   - **Code:**
     ```python
     a = int(input("Enter a whole number: "))
     b = int(input("Enter another whole number: "))
     print(f"Total: {a + b}")
     ```

10. **TRY — Small profile**
    - **Task:** Ask for first name, surname, age, and favourite type of music. Output a sentence with those details.

11. **LESSON — String methods**
    - **Task:** Ask for a name, then output the uppercase, lowercase, title case, and the number of characters.
    - **Code:**
      ```python
      name = input("What is your name? ")
      print(name.upper())
      print(name.lower())
      print(name.title())
      print(f"Your name has {len(name)} characters.")
      ```

12. **TRY — Uppercase + letter count**
    - **Task:** Ask for the user’s first name. Display the uppercase version and how many letters are in it.

13. **TRY — Letters in a full name**
    - **Task:** Ask for first and second names. Display how many letters are in each and the total.
