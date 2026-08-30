import random

# List of possible fruit words for the game
fruits = ["apple","banana","orange","mango","strawberry","grape","watermelon","pineapple","blueberry","papaya","kiwi","peach","cherry","pomegranate","guava","lemon","raspberry","avocado",]

# Randomly select a secret word from the list
word = random.choice(fruits)

# Track guessed letters and wrong attempts
guessed = []
wrong_guesses = 0
max_guesses = 6

# ASCII art representing each stage of the hangman (0 to 6 wrong guesses)
hangman = [
    """
    -----
    |    |
         |
         |
         | 
  ============
  """,
  """
  -----
  |    |
  O    |
       |
       | 
============
 """,
  """
  -----
  |    |
  O    |
  |    |
       | 
============
 """,
   """
  -----
  |    |
  O    |
 /|    |
       | 
============
 """,
   """
  -----
  |    |
  O    |
 /|\\  |
       | 
============
 """,
   """
  -----
  |    |
  O    |
 /|\\  |
 /     | 
============
 """,
   """
  -----
  |    |
  O    |
 /|\\  |
 / \\  | 
============
 """
]

# Game introduction
print("Welcome to Hangman!")
print("Hint: The word is a fruit.")

# Main game loop: runs until the player runs out of guesses
while wrong_guesses < max_guesses:
    display = ""

    # Build the hidden word display (reveal guessed letters, hide others with '_')
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    # Display current hangman visual state and word progress
    print(hangman[wrong_guesses])
    print("Word:", display)

    # Check for win condition (no hidden letters remaining)
    if "_" not in display:
        print("Congratulations! You won!")
        print("The fruit was:", word)
        break

    # Get player's guess
    guess = input("Guess a letter: ").lower()

    # Validate input (must be a single alphabetical character)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    # Prevent repeated guesses
    if guess in guessed:
        print("You already guessed that letter.")
        continue

    # Add the guess to history
    guessed.append(guess)

    # Evaluate the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Triggered if the player uses all allowed wrong guesses without winning
else:
    print(hangman[wrong_guesses])
    print("Game Over!")
    print("The fruit was:", word)