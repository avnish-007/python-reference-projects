# 🎮 Hangman Game in Python

A classic, interactive console-based Hangman game built using Python. Guess the hidden fruit name letter by letter before running out of attempts!

---

## 📌 Features

- **Dynamic Visuals:** Multi-stage ASCII hangman illustration updated with each guess.
- **Input Validation:** Prevents invalid inputs (numbers, symbols, multiple letters) and warns about duplicate guesses without penalizing attempts.
- **Built-in Fruit Word Bank:** Pre-loaded collection of fruit names chosen at random.
- **Zero External Dependencies:** Built purely with Python's standard library (`random`).

---

## 🛠️ Requirements

- **Python 3.6+**

No additional libraries or packages need to be installed.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/hangman-python.git
   cd hangman-python
   ```

2. **Run the game:**
   ```bash
   python "Hangman Game in Python.py"
   ```

---

## 🎯 How to Play

1. The game selects a random fruit name and displays blank spaces (`_`) for each letter.
2. Enter one letter per turn.
3. If the letter is in the word, it reveals all matching positions.
4. If the letter is incorrect, a part of the hangman is drawn and your remaining guesses decrease.
5. You have **6 incorrect guesses** before the game is over.
6. Guess all letters correctly to win!

---

## 📂 Project Structure

```text
.
├── Hangman Game in Python.py  # Main game script with complete gameplay logic
├── README.md                  # Project documentation and guide
├── .gitignore                 # Standard Python gitignore rules
└── LICENSE                    # Open-source MIT license
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments & Credits

- Original game concept and tutorial reference by [GeeksforGeeks](https://www.geeksforgeeks.org/python/hangman-game-python/).

