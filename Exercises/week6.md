## Functions with parameters & scope

**Reminder:** **LESSON** = reproduce the code. **TRY** = attempt the task without seeing the code.

1. **TRY — Pass a name to a function**
   - **Task:** Ask for the user’s name. Pass the name into a function that outputs it in a message.

2. **TRY — Age check in a function**
   - **Task:** Ask for age. Pass the value into a function that prints “You are old enough to get into nightclubs” if age ≥ 18.

3. **TRY — Area function**
   - **Task:** Ask for the length and breadth of a room. Pass these into a function that returns the area.

4. **LESSON — Local vs global scope**
   - **Task:** Demonstrate a global variable and a local variable of the same name; show that prints inside vs outside the function differ.
   - **Code:**
     ```python
     message = "outside the function"  # global

     def my_message():
         message = "inside the function"  # local
         print(message)

     my_message()
     print(message)
     ```

5. **TRY — Times table (parameters)**
   - **Task:** Ask for a number. Output its times table up to ×12.
   

## Switch-style menus & loops
**Reminder:** **LESSON** = reproduce the code. **TRY** = attempt the task without seeing the code.

1. **LESSON — Number choice**
   - **Task:** Ask the user to choose 1, 2 or 3. Output which number they chose; otherwise show an “invalid entry” message.
   - **Code:**
     ```python
     ans = input("Enter 1, 2 or 3: ").strip()
     if ans in ("1","2","3"):
         print(f"You have chosen the number {ans}.")
     else:
         print("This was not a valid entry.")
     ```

2. **TRY — Number choice → functions**
   - **Task:** Change the previous programme so that 1 runs a function asking for a name and printing it; 2 asks for two numbers and prints their total; 3 prints a closing message.

3. **TRY — Secret code (while loop)**
   - **Task:** Keep asking for a secret code (1234) until the correct code is entered.

4. **TRY — Secret code (do/while style)**
   - **Task:** Re-write the previous exercise so the prompt runs at least once, then repeats until correct.

5. **TRY — Login attempts**
   - **Task:** Ask for username and password. Allow up to three attempts. If exceeded, print “You have tried too many times”.

6. **TRY — Menu loop with functions**
   - **Task:** Ask repeatedly for 1/2/3. 1 → ask and print name; 2 → add two numbers and print the total; 3 → print “goodbye” and stop; other → show an error and ask again.