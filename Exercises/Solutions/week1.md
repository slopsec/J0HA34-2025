## Week 1 — Basics (printing, variables, strings, input)
**Reminder:** **LESSON** = follow along and reproduce the code shown. **TRY** = attempt the task yourself; solution shown below.

1. **LESSON — Your first output**
   - **Task:** Create a tiny Python programme that displays a message to the screen.
   - **Code:**
```python
print("My first Python")
```

2. **TRY — Two alerts → two lines**
   - **Task:** Write a Python programme that outputs two different messages on separate lines.
   - **Solution (Python):**
```python
print("Python is fun!")
print("I love it!!!")
```

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
print(5 + 7)
print(9 - 3)
print(4 * 6)
print(8 / 2)
print(7 // 3)
print(7 % 3)
print(2 ** 3)
```

5. **TRY — Use another operator**
   - **Task:** Write a programme that uses one of: `/`, `*`, or `-` to perform a calculation and display the result.
   - **Solution (Python):**
```python
a = 21
b = 7
print(a / b)
print(a * b)
print(a - b)
```

6. **LESSON — Quotation marks and escaping**
   - **Task:** Output text that mixes single and double quotes. Show how to escape characters (e.g., in *isn't*).
   - **Code:**
```python
print('She said "hello"')
print("He said 'it isn\'t fair'")
print('He said "it isn\'t fair"')
print("""Line 1\nLine 2\nLine 3""")
```

7. **LESSON — Joining text and f-strings**
   - **Task:** Join a first name and surname using concatenation and an f-string.
   - **Code:**
```python
first = "Johnny"
last = "Brown"
print(first + " " + last)
print(f"Hi {first} {last}")
```

8. **TRY — Build a message**
   - **Task:** Store a name and a cost in variables and display: `Hi <name>, your total cost is £<cost>`.
   - **Solution (Python):**
```python
name = "Alex"
cost = 50
print(f"Hi {name}, your total cost is £{cost}")
```

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
    - **Solution (Python):**
```python
first = input("First name: ")
surname = input("Surname: ")
age = int(input("Age: "))
music = input("Favourite type of music: ")
print(f"{first} {surname}, your age is {age} and you like {music} music.")
```

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
    - **Solution (Python):**
```python
first = input("First name: ")
print(first.upper())
print(f"Your first name has {len(first)} letters.")
```

13. **TRY — Letters in a full name**
    - **Task:** Ask for first and second names. Display how many letters are in each and the total.
    - **Solution (Python):**
```python
first = input("First name: ")
second = input("Second name: ")
total = len(first) + len(second)
print(f"Hi {first} {second}, you have {total} letters in your name.")
```

14. **TRY — Lucky number**
    - **Task:** Ask for the month number you were born (e.g., 3 for March) and your full name. Multiply the number of letters in your full name by the month number and display the “lucky number”.
    - **Solution (Python):**
```python
month = int(input("Enter your birth month (1–12): "))
full_name = input("Enter your full name: ")
letters = len(full_name.replace(" ", ""))
print(f"Your lucky number is {letters * month}")
```

15. **TRY — Meal, tip, and change**
    - **Task:** Store a meal price, calculate a 15% tip, compute the total, then ask how much cash is given and display the change due.
    - **Solution (Python):**
```python
meal_price = float(input("Meal price £: "))
tip = meal_price * 0.15
total = meal_price + tip
cash = float(input("Cash given £: "))
print(f"Change due: £{cash - total:.2f}")
```

16. **TRY — Weekly pay with tax**
    - **Task:** Ask how many hours were worked. Pay is £7.00 per hour. Deduct 5% tax. Output gross pay, tax, and net pay.
    - **Solution (Python):**
```python
hours = float(input("Hours worked: "))
gross = hours * 7.00
tax = gross * 0.05
net = gross - tax
print(f"Gross: £{gross:.2f}, Tax: £{tax:.2f}, Net: £{net:.2f}")
```

17. **LESSON — Lists (unordered list equivalent)**
    - **Task:** Store a few items in a list and print them neatly.
    - **Code:**
```python
foods = ["Soup", "Pizza", "Sweetcorn"]
print("Food I Like:")
for food in foods:
    print(f"- {food}")
```

18. **TRY — Favourite foods (3 items)**
    - **Task:** Ask the user for three favourite foods and display them as a bullet list.
    - **Solution (Python):**
```python
foods = [input("Food 1: "), input("Food 2: "), input("Food 3: ")]
for f in foods:
    print("-", f)
```

19. **TRY — Lottery wishlist (10 items)**
    - **Task:** Ask for 10 things you would buy if you won the National Lottery. Display a heading (“Here is your wishlist”) and list the items.
    - **Solution (Python):**
```python
wishlist = [input(f"Item {i}: ") for i in range(1, 11)]
print("Here is your wishlist:")
for i, item in enumerate(wishlist, 1):
    print(f"{i}. {item}")
```

20. **TRY — Area of a room**
    - **Task:** Ask for the length and breadth of a room and display the length, breadth, and calculated area.
    - **Solution (Python):**
```python
length = float(input("Length (m): "))
breadth = float(input("Breadth (m): "))
area = length * breadth
print(f"Length: {length} m, Breadth: {breadth} m, Area: {area} m²")
```

